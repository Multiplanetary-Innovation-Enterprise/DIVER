from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import math
import time
from pathlib import Path


#if testing on actual ROV, uncomment below line and add "Subscriber" to the inside of the parenthesis for UI()
from  ROVMessaging.Subscriber import *
#Subscriber
#Notes:
#Resolution: 640x480
class UI(Subscriber):
    Window = Tk()
    FakeHardware = False
    
    def __init__(self) -> None:
        #Get the absolute path to the directory containing UI.py
        thisDir = Path(__file__).resolve().parent

        # configure window layout
        self.Window.title("ROV Control Panel")
        self.Window.configure(bg="#2b2b2b")

        # fullscreen mode
        self.Window.update_idletasks()
        ws = self.Window.winfo_screenwidth()
        hs = self.Window.winfo_screenheight()
        self.Window.geometry(f"{ws}x{hs}+0+0")
        self.Window.minsize(800, 600)
        self.Window.resizable(True, True)

        # main container to center content and provide padding
        self.mainframe = Frame(self.Window, bg="#2b2b2b", padx=10, pady=8)
        self.mainframe.pack(fill=BOTH, expand=True)


        #Initializes instance variables
        self.internaltemp = "NOT DETECTED"
        self.externaltemp = "NOT DETECTED"
        self.battery = "NOT DETECTED"
        self.depth = "NOT DETECTED"
        self.heading = "NOT DETECTED"
        self.camfeed = cv2.VideoCapture(0)
        _, self.frame = self.camfeed.read()
        self.logtext = "Log Started!"
        self.pressure = "NOT DETECTED"
        self.acc = "NOT DETECTED"
        self.conn_status = "DISCONNECTED"
        self.latency = "N/A"
        self.control_mode = "MANUAL"
        self.estop_engaged = False
        self.pitch = "NOT DETECTED"
        self.roll = "NOT DETECTED"
        self.core_temp = "NOT DETECTED"
        self.light_level = "NOT DETECTED"
        # wheel rotation state
        self.wheel_rpm_left = 0
        self.wheel_rpm_right = 0
        self.wheel_angle_left = 0.0
        self.wheel_angle_right = 0.0

        # tracking the six thrusters (in range [-1,1])
        self.thruster_speeds = {
            'TopFront': 0.0,
            'TopBack': 0.0,
            'FrontLeft': 0.0,
            'BackLeft': 0.0,
            'FrontRight': 0.0,
            'BackRight': 0.0
        }
        self.thruster_directions = {k: 'Stopped' for k in self.thruster_speeds}
        self.thruster_angles = {k: 0.0 for k in self.thruster_speeds}

        self._last_update_time = time.time()
        self.time = 0
        self.running = True

        # controller layout selector - TOP
        self.controller_frame = Frame(self.mainframe, bg="#1a1a1a", relief=RAISED, bd=1)
        self.controller_frame.grid_columnconfigure(1, weight=1)  # Center column expands
        
        # Left frame for layout controls
        self.left_frame = Frame(self.controller_frame, bg="#1a1a1a")
        self.left_frame.grid(row=0, column=0, padx=(8, 0), pady=6, sticky="w")
        layout_label = Label(self.left_frame, text="Controller Layout:", bg="#1a1a1a", fg="#ffffff", font=("Segoe UI", 9))
        layout_label.pack(side=LEFT, padx=(0, 5))
        self.layout_var = StringVar(value="Layout 1")
        self.layout_combo = ttk.Combobox(self.left_frame, textvariable=self.layout_var, values=["Layout 1", "Layout 2", "Layout 3"], state="readonly", font=("Segoe UI", 10), width=12)
        self.layout_combo.pack(side=LEFT, padx=(0, 5))
        self.layout_combo.bind("<<ComboboxSelected>>", self.on_layout_changed)
        # colored box showing current layout
        self.layout_color_box = Canvas(self.left_frame, width=120, height=30, bg="#222222", bd=0, highlightthickness=0)
        self.layout_color_box.pack(side=LEFT, padx=(0, 5))
        self.layout_color_box.bind("<Button-1>", self.show_full_layout)
        self.update_layout_box()
        
        # Center frame for measurements - will expand to center in window
        self.center_frame = Frame(self.controller_frame, bg="#1a1a1a")
        self.center_frame.grid(row=0, column=1, pady=6, sticky="nsew")
        
        # Sub-frame to center the measurement labels within the center_frame
        self.measurements_container = Frame(self.center_frame, bg="#1a1a1a")
        self.measurements_container.pack(expand=True, anchor=N)
        
        # Measurement labels inside the centered container
        measurements = {
            "time_label": f":{math.floor(self.time / 60)}m {self.time % 60}s",
            "internal_temp_label": f"Internal: {self.internaltemp}°C",
            "external_temp_label": f"External: {self.externaltemp}°C",
            "pressure_label": f"Pressure: {self.pressure} bar",
            "speed_label": f"Acceleration: {self.acc}m/s²",
        }
        for name, text in measurements.items():
            label = Label(self.measurements_container, text=text, bg="#1a1a1a", fg="#ffffff", font=("Segoe UI", 12))
            label.pack(side=LEFT, padx=3)
            setattr(self, name, label)
        
        # Right frame for E-STOP button
        self.right_frame = Frame(self.controller_frame, bg="#1a1a1a")
        self.right_frame.grid(row=0, column=2, padx=(250, 8), pady=6, sticky="e") #need to FIX the padding here and center the data
        self.estop_button = Button(self.right_frame, text="E-STOP", bg="#FF0000", fg="white", font=("Segoe UI", 11, 'bold'), padx=15, pady=6, command=lambda: self.toggle_estop())
        self.estop_button.pack(side=RIGHT)

        # creates label for info to be put in
        self.infolabel = Label(self.mainframe, anchor=CENTER, bg="#f0f0f0", fg="#000000",
                       font=("Segoe UI", 10), padx=8, pady=5, relief=FLAT)

        # Telemetry section header
        telemetry_header = Label(self.mainframe, text="TELEMETRY", bg="#1a1a1a", fg="#ffffff", font=("Segoe UI", 9, "bold"), relief=RAISED, bd=1)

        # status row 1 - navigation & vehicle state
        self.status_frame_row1 = Frame(self.mainframe, bg="#2b2b2b")
        status_style = dict(bg="#3a3a3a", fg="white", font=("Segoe UI", 9), padx=6, pady=4, relief=FLAT)
        self._create_status_labels(self.status_frame_row1, [
            ("battery_label", "Battery", self.battery), ("depth_label", "Depth", self.depth),
            ("heading_label", "Heading", self.heading), ("pitch_label", "Pitch", self.pitch),
            ("roll_label", "Roll", self.roll), ("core_label", "Core", self.core_temp)], status_style)

        # status row 2 - connection & control & navigation
        self.status_frame_row2 = Frame(self.mainframe, bg="#2b2b2b")
        self._create_status_labels(self.status_frame_row2, [
            ("conn_label", "Conn", self.conn_status), ("latency_label", "Latency", self.latency),
            ("mode_label", "Mode", self.control_mode)], status_style)
        
        # wheel mini-indicators (left/right) & IMU compass
        self.wheels_frame = Frame(self.status_frame_row2, bg="#2b2b2b")
        self.wheel_canvas_left = Canvas(self.wheels_frame, width=50, height=50, bg="#222222", bd=1, highlightthickness=0)
        self.wheel_label_left = Label(self.wheels_frame, text=("L: " + str(self.wheel_rpm_left) + " RPM"), bg="#2b2b2b", fg="white", font=("Segoe UI", 8))
        self.wheel_canvas_right = Canvas(self.wheels_frame, width=50, height=50, bg="#222222", bd=1, highlightthickness=0)
        self.wheel_label_right = Label(self.wheels_frame, text=("R: " + str(self.wheel_rpm_right) + " RPM"), bg="#2b2b2b", fg="white", font=("Segoe UI", 8))
        # IMU heading dial
        self.imu_canvas = Canvas(self.status_frame_row2, width=70, height=70, bg="#222222", bd=1, highlightthickness=0)

        # Content container - thrusters on left, camera on right
        self.content_container = Frame(self.mainframe, bg="#2b2b2b")
        
        # Left side: Thrusters in 3x2 grid
        self.thrusters_left_frame = Frame(self.content_container, bg="#2b2b2b")
        self.thruster_bars = {}
        # Grid layout: 3 rows x 2 columns
        thruster_grid_layout = [
            ['FrontLeft', 'FrontRight'],
            ['TopFront', 'TopBack'],
            ['BackLeft', 'BackRight']
        ]
        for row in thruster_grid_layout:
            row_frame = Frame(self.thrusters_left_frame, bg="#2b2b2b")
            row_frame.pack()
            for thr in row:
                thr_container = Frame(row_frame, bg="#2b2b2b")
                thr_container.pack(side=LEFT, padx=3, pady=3)
                label = Label(thr_container, text=thr, bg="#2b2b2b", fg="white", font=("Segoe UI", 8))
                label.pack()
                canvas = Canvas(thr_container, width=70, height=18, bg="#1a1a1a", bd=1, highlightthickness=0)
                canvas.pack()
                self.thruster_bars[thr] = canvas
        
        # Right side: Camera/Video frame
        self.camera_frame = Frame(self.content_container, bg="#000000", relief=SUNKEN, bd=1, width=750, height=625)
        self.camera_frame.pack_propagate(False)
        self.ImageFrame = Label(self.camera_frame, bg="#000000", bd=0, relief=FLAT)
        self.ImageFrame.pack(fill=BOTH, expand=True)
        
        # Pack content container sides
        self.thrusters_left_frame.pack(side=LEFT, fill=BOTH, padx=3, pady=0)
        self.camera_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=1, pady=0)
        
        self.log = Label(self.mainframe, bg="#111111", fg="white", text=self.logtext, height=4,
                 anchor=NW, justify=LEFT, font=("Consolas", 8), bd=1, relief=GROOVE)
        self.log.pack(fill=BOTH, expand=False, pady=(0, 4))

        #If buttons are necessary, use this format:
        #self.startbutton = Button(self.Window,text="Start ROV program",height=5,width=30)
        #self.endbutton = Button(self.Window,text="End ROV program",height=5,width=30)
            
        # layout: organized sections
        self.controller_frame.pack(fill=X, pady=(0, 4))
        self.infolabel.pack(fill=X, pady=(0, 6))
        telemetry_header.pack(fill=X, pady=(4, 2))
        self.status_frame_row1.pack(fill=X, pady=(0, 2))
        self.status_frame_row2.pack(fill=X, pady=(0, 6))
        self.content_container.pack(fill=BOTH, expand=True, pady=(4, 4))

        # Separator
        Label(self.status_frame_row2, bg="#2b2b2b").pack(side=LEFT, padx=2)
        # Navigation inline
        self.wheels_frame.pack(side=LEFT, padx=(2, 4))
        self.wheel_canvas_left.pack(side=LEFT)
        self.wheel_label_left.pack(side=LEFT, padx=(3, 6))
        self.wheel_canvas_right.pack(side=LEFT)
        self.wheel_label_right.pack(side=LEFT, padx=3)
        self.imu_canvas.pack(side=LEFT, padx=(4, 4))

        # Log section header
        log_header = Label(self.mainframe, text="DEBUG LOG", bg="#1a1a1a", fg="#ffffff", font=("Segoe UI", 9, "bold"), relief=RAISED, bd=1)
        log_header.pack(fill=X, pady=(4, 2))

        self.log.pack(fill=BOTH, expand=False, pady=(4, 0))

    def _create_status_labels(self, frame, fields, style):
        for name, prefix, value in fields:
            label = Label(frame, text=f"{prefix}: {value}", **style)
            label.pack(side=LEFT, padx=4, expand=True, fill=X)
            setattr(self, name, label)

    def startDummyData(self):
        self.time += 1
        self.internaltemp = 25
        self.externaltemp = 18
        self.pressure = 1
        self.acc = 9
        if self.running:
            self.Window.after(1000, self.startDummyData)

    def startMainLoop(self):
        self.startVideo()
        self.startTrackingDisplays()
        #insert dummy data for UI testing
        self.startDummyData()
        self.Window.mainloop()


    #adds log
    def addLog(self,text) -> None:
        self.logtext += ("\n" + str(text))

#starts showing video from client's camera
    def startVideo(self) ->  None:
        
        #pulls a frame as an image
        _, self.frame = self.camfeed.read()
        #Converts image to the proper colors for display
        self.displayableImage = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGBA)

        #converts image to format readable by tkinter
        self.Arrayimage = Image.fromarray(self.displayableImage)
        self.photo_image = ImageTk.PhotoImage(image=self.Arrayimage)

        #sets image in label to frame
        self.ImageFrame.photo_image = self.photo_image
        self.ImageFrame.configure(image=self.photo_image)

        #repeats this process every 1ms
        if self.running:
            self.Window.after(1,self.startVideo)

    #Checks for updates
    def startTrackingDisplays(self):
        self.infospacing = 20
        # primary info line - now update individual labels in controller frame
        self.time_label.configure(text=(str(self.time) + "s"))
        self.internal_temp_label.configure(text=("Int: " + str(self.internaltemp) + "°C"))
        self.external_temp_label.configure(text=("Ext: " + str(self.externaltemp) + "°C"))
        self.pressure_label.configure(text=("Pressure: " + str(self.pressure) + " bar"))
        self.speed_label.configure(text=("Acceleration: " + str(self.acc) + "m/s²"))
        
        # Clear the old infolabel text since measurements moved to top
        self.infolabel.configure(text="")
        
        # update status widgets
        self.battery_label.configure(text=("Battery: " + str(self.battery)))
        self.depth_label.configure(text=("Depth: " + str(self.depth)))
        self.heading_label.configure(text=("Heading: " + str(self.heading)))
        self.conn_label.configure(text=("Conn: " + str(self.conn_status)))
        self.latency_label.configure(text=("Latency: " + str(self.latency)))
        self.mode_label.configure(text=("Mode: " + str(self.control_mode)))
        self.pitch_label.configure(text=("Pitch: " + str(self.pitch)))
        self.roll_label.configure(text=("Roll: " + str(self.roll)))
        self.core_label.configure(text=("Core: " + str(self.core_temp)))
        # update wheel RPM labels and rotation based on RPM
        now = time.time()
        dt = max(0.0, now - getattr(self, '_last_update_time', now))
        self._last_update_time = now
        #  move angles using RPM = revolutions per second * 360
        self.wheel_angle_left = (self.wheel_angle_left + (self.wheel_rpm_left / 60.0) * 360.0 * dt) % 360.0
        self.wheel_angle_right = (self.wheel_angle_right + (self.wheel_rpm_right / 60.0) * 360.0 * dt) % 360.0
        self.wheel_label_left.configure(text=("L: " + str(self.wheel_rpm_left) + " RPM"))
        self.wheel_label_right.configure(text=("R: " + str(self.wheel_rpm_right) + " RPM"))

        # update thruster visual bars
        for thruster, speed in self.thruster_speeds.items():
            self.thruster_angles[thruster] = (self.thruster_angles[thruster] + abs(speed) * 360.0 * dt) % 360.0
            direction = 'CW' if speed > 0 else ('CCW' if speed < 0 else 'Stopped')
            self.thruster_directions[thruster] = direction
            self.draw_thruster_bar(self.thruster_bars[thruster], speed)

        # rotation indicator for wheels
        def draw_wheel(canvas, angle):
            canvas.delete("all")
            cx, cy, r = 25, 25, 17
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="white")
            a = math.radians(angle)
            x2 = cx + r * math.cos(a)
            y2 = cy - r * math.sin(a)
            canvas.create_line(cx, cy, x2, y2, fill="#00ffff", width=2)
        draw_wheel(self.wheel_canvas_left, self.wheel_angle_left)
        draw_wheel(self.wheel_canvas_right, self.wheel_angle_right)
        # draw IMU heading dial - raw degrees only
        def draw_imu(canvas, heading):
            canvas.delete("all")
            cx, cy, r = 35, 35, 22
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="white")
            # draw heading pointer
            a = math.radians(heading if isinstance(heading, (int, float)) else 0)
            x2 = cx + r * math.sin(a)
            y2 = cy - r * math.cos(a)
            canvas.create_line(cx, cy, x2, y2, fill="#ffcc00", width=3)
            # display heading degrees in center
            heading_str = f"{int(heading) if isinstance(heading, (int, float)) else 0}°"
            canvas.create_text(cx, cy, text=heading_str, fill="white", font=("Arial", 9, "bold"))
        try:
            h = float(self.heading)
        except Exception:
            h = 0.0
        draw_imu(self.imu_canvas, h)
        self.log.configure(text=self.logtext)

        if self.running:
            self.Window.after(1,self.startTrackingDisplays)


    def draw_thruster_bar(self, canvas, speed):
        """Draw a progress bar for thruster speed (-1.0 to 1.0)"""
        canvas.delete("all")
        width, height = 80, 20
        center_x = width / 2
        
        # Draw background
        canvas.create_rectangle(0, 0, width, height, fill="#1a1a1a", outline="#444444")
        # Draw center line
        canvas.create_line(center_x, 0, center_x, height, fill="#666666")
        
        # Determine bar position and color based on speed
        if speed > 0:
            color = "#00aa00"  # Green for forward
            bar_width = (speed * (center_x - 2))
            bar_x1 = center_x
            bar_x2 = center_x + bar_width
        elif speed < 0:
            color = "#ff4444"  # Red for reverse
            bar_width = (abs(speed) * (center_x - 2))
            bar_x1 = center_x - bar_width
            bar_x2 = center_x
        else:
            return  # No bar if speed is 0
        
        # Draw speed bar
        canvas.create_rectangle(bar_x1, 2, bar_x2, height - 2, fill=color, outline=color)

    def on_layout_changed(self, event=None):
        """Called when layout is changed via dropdown"""
        self.update_layout_box()

    def update_layout_box(self):
        """Update the colored box showing current layout"""
        layout = self.layout_var.get()
        self.layout_color_box.delete("all")
        
        # Determine color and letter based on layout
        layout_map = {
            "Layout 1": {"color": "#ff9944", "letter": "A"},
            "Layout 2": {"color": "#5566dd", "letter": "B"},
            "Layout 3": {"color": "#66cc66", "letter": "C"}
        }
        
        info = layout_map.get(layout, {"color": "#666666", "letter": "?"})
        
        # Draw colored rectangle background
        self.layout_color_box.create_rectangle(2, 2, 118, 28, fill=info["color"], outline="white", width=1)
        # Draw layout label
        self.layout_color_box.create_text(60, 15, text=f"Layout {info['letter']}", fill="white", font=("Arial", 10, "bold"))

    def show_full_layout(self, event):
        """Show full layout image in popup"""
        layout = self.layout_var.get()
        popup = Toplevel(self.Window)
        popup.title(f"{layout} - Controller Layout")
        popup.geometry("450x350")
        popup.configure(bg="#2b2b2b")
        popup.resizable(False, False)
        
        # Title bar
        title_frame = Frame(popup, bg="#1a1a1a", relief=RAISED, bd=1)
        title_frame.pack(fill=X)
        title_label = Label(title_frame, text=f"{layout} - Controller Layout", bg="#1a1a1a", fg="white", font=("Segoe UI", 11, "bold"), pady=8)
        title_label.pack()
        
        canvas = Canvas(popup, width=430, height=280, bg="#222222", bd=0, highlightthickness=0)
        canvas.pack(pady=10)
        
        # Placeholder for full image - can be replaced with actual images
        canvas.create_text(215, 140, text=f"{layout}\n\nController Image Placeholder", fill="white", font=("Arial", 12), justify=CENTER)

    def recieveMessage(self, message):
        if 'time' in message.getContents():
            self.time = message.getContents()['time']
        if 'externalTemp' in message.getContents():
            self.externaltemp = message.getContents()['externalTemp']
        if 'pressure' in message.getContents():
            self.pressure = message.getContents()['pressure']
        if 'internalTemp' in message.getContents():
            self.internaltemp = message.getContents()['internalTemp']
        if 'action' in message.getContents():
            self.action = message.getContents()['action']
        if 'Frame' in message.getContents():
            self.frame = message.getContents()['Frame']
        # If linear acceleration from an IMU is provided, compute magnitude
        # and estimate roll (rotation around X) and pitch (rotation around Y).
        if all(k in message.getContents() for k in ('linAcc_x', 'linAcc_y', 'linAcc_z')):
            ax = message.getContents()['linAcc_x']
            ay = message.getContents()['linAcc_y']
            az = message.getContents()['linAcc_z']
            self.acc = math.sqrt((ax ** 2.0) + (ay ** 2.0) + (az ** 2.0))
            try:
                # roll: rotation around X axis (radians) -> atan2(y, z)
                roll_rad = math.atan2(ay, az)
                # pitch: rotation around Y axis (radians) -> atan2(-x, sqrt(y^2+z^2))
                pitch_rad = math.atan2(-ax, math.sqrt(ay * ay + az * az))
                self.roll = round(math.degrees(roll_rad), 2)
                self.pitch = round(math.degrees(pitch_rad), 2)
            except Exception:
                self.roll = "NOT DETECTED"
                self.pitch = "NOT DETECTED"
        # optional telemetry fields
        if 'battery' in message.getContents():
            self.battery = message.getContents()['battery']
        # wheel telemetry
        if 'wheel_rpm_left' in message.getContents():
            self.wheel_rpm_left = message.getContents()['wheel_rpm_left']
        if 'wheel_rpm_right' in message.getContents():
            self.wheel_rpm_right = message.getContents()['wheel_rpm_right']

        # thruster speed telemetry
        if 'thruster_speed_top_front' in message.getContents():
            self.thruster_speeds['TopFront'] = float(message.getContents()['thruster_speed_top_front'])
        if 'thruster_speed_top_back' in message.getContents():
            self.thruster_speeds['TopBack'] = float(message.getContents()['thruster_speed_top_back'])
        if 'thruster_speed_front_left' in message.getContents():
            self.thruster_speeds['FrontLeft'] = float(message.getContents()['thruster_speed_front_left'])
        if 'thruster_speed_back_left' in message.getContents():
            self.thruster_speeds['BackLeft'] = float(message.getContents()['thruster_speed_back_left'])
        if 'thruster_speed_front_right' in message.getContents():
            self.thruster_speeds['FrontRight'] = float(message.getContents()['thruster_speed_front_right'])
        if 'thruster_speed_back_right' in message.getContents():
            self.thruster_speeds['BackRight'] = float(message.getContents()['thruster_speed_back_right'])

        # direction fallback from explicit field
        if 'thruster_direction_top_front' in message.getContents():
            self.thruster_directions['TopFront'] = message.getContents()['thruster_direction_top_front']
        if 'thruster_direction_top_back' in message.getContents():
            self.thruster_directions['TopBack'] = message.getContents()['thruster_direction_top_back']
        if 'thruster_direction_front_left' in message.getContents():
            self.thruster_directions['FrontLeft'] = message.getContents()['thruster_direction_front_left']
        if 'thruster_direction_back_left' in message.getContents():
            self.thruster_directions['BackLeft'] = message.getContents()['thruster_direction_back_left']
        if 'thruster_direction_front_right' in message.getContents():
            self.thruster_directions['FrontRight'] = message.getContents()['thruster_direction_front_right']
        if 'thruster_direction_back_right' in message.getContents():
            self.thruster_directions['BackRight'] = message.getContents()['thruster_direction_back_right']

        if 'depth' in message.getContents():
            self.depth = message.getContents()['depth']
        if 'heading' in message.getContents():
            self.heading = message.getContents()['heading']
        if 'pitch' in message.getContents():
            self.pitch = message.getContents()['pitch']
        if 'roll' in message.getContents():
            self.roll = message.getContents()['roll']
        if 'Core Temp' in message.getContents():
            self.core_temp = message.getContents()['Core Temp']
        if 'conn_status' in message.getContents():
            self.conn_status = message.getContents()['conn_status']
        if 'latency' in message.getContents():
            self.latency = message.getContents()['latency']
        if 'control_mode' in message.getContents():
            self.control_mode = message.getContents()['control_mode']
    
    def close(self):
        self.running = False
        self.camfeed.release()
        self.Window.destroy()

    def confirm_estop(self):
        """Show in-app confirmation dialog for E-STOP"""
        dialog = Toplevel(self.Window)
        dialog.title("Confirm E-STOP")
        dialog.geometry("350x150")
        dialog.configure(bg="#2b2b2b")
        dialog.resizable(False, False)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = self.Window.winfo_x() + (self.Window.winfo_width() // 2) - 175
        y = self.Window.winfo_y() + (self.Window.winfo_height() // 2) - 75
        dialog.geometry(f"+{x}+{y}")
        
        # Message
        msg_label = Label(dialog, text="Are you sure you want to\nEngage the Emergency Stop?", 
                         bg="#2b2b2b", fg="white", font=("Segoe UI", 11))
        msg_label.pack(pady=20)
        
        # Buttons
        button_frame = Frame(dialog, bg="#2b2b2b")
        button_frame.pack(pady=10)
        
        def confirm():
            dialog.destroy()
            self.estop_engaged = True
            self.estop_button.configure(bg="#FF6600", text="ENGAGED")
            self.addLog("Emergency stop ENGAGED")
        
        def cancel():
            dialog.destroy()
        
        yes_btn = Button(button_frame, text="YES, ENGAGE", bg="#cc0000", fg="white", 
                        font=("Segoe UI", 10, "bold"), padx=15, pady=8, command=confirm)
        yes_btn.pack(side=LEFT, padx=10)
        
        no_btn = Button(button_frame, text="Cancel", bg="#3a3a3a", fg="white", 
                       font=("Segoe UI", 10), padx=20, pady=8, command=cancel)
        no_btn.pack(side=LEFT, padx=10)

    def toggle_estop(self):
        # toggle emergency stop with confirmation
        if not self.estop_engaged:
            # Show in-app confirmation dialog
            self.confirm_estop()
        else:
            # Release without confirmation (quick release)
            self.estop_engaged = False
            self.estop_button.configure(bg="#FF0000", text="E-STOP")
            self.addLog("Emergency stop RELEASED")