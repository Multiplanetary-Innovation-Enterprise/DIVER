from dijkstar import Graph, find_path
from math import sqrt,pi
from ROVMessaging.Subscriber import *
from inputs.Input import *



class AutonomySystem(Subscriber, Input):

    #constants
    __NAVDENSITY:float = 1.0                                                                                                        # density of nodes in graph
    __NAVSPACING:float = 1.0/__NAVDENSITY
    __SAFEDIST:float = 0.3                                                                                                          # Closest the ROV should get to a scanned point
    __MINEPOINT1:tuple = (-3,18,11)                                                                                                 # One corner of mine
    __MINEPOINT2:tuple = (3,-3,-17)                                                                                                 # Opposite corner of mine
    __GOAL:tuple = ((__MINEPOINT1.x + __MINEPOINT2.x) / 2,min(__MINEPOINT1.y,__MINEPOINT2.y),(__MINEPOINT1.z + __MINEPOINT2.z) / 2) # goal point for the ROV to seek out

    #Modes: 
    # 0 : automatic
    # 1 : manual
    __MODE = 0

    #variables
    __time = 0.0
    __ROVVelocity:tuple = (0,0,0)
    __ROVPosition:tuple = (0,0,0)
    __startHeight:float = __ROVPosition.y
    __timeElapsed:float = 0.0
    __fastpath:list = []
    __scanPoints:list = []
    __stage:int = 0 # stage of navigation
    __unhandledStageChange:bool = False #used for stage changes
    __nextNode:tuple = () # next node to go to, will be assigned after Dijkstra is ran
    __pathInd:int = 1 # which point in the path 
    __prevNode:tuple = __ROVPosition
    __hasFinished:bool = False


    #Stages:
    # 0 : Generate graph
    # 1 : Filtered graph based on nodes in Dijkstra path
    # 2 : Move between nodes in path

    def __init__(self) -> None:
        self.generate_graph()
        if self.__MODE == 0:
            self.__stage = 1
            unhandledStageChange = True
        
    def rangef(start:float, end:float, step:float) -> list:
        tempList = []
        val = start
        
        if start < end:
            while val < end:
                tempList.append(val)
                val += step
        elif start > end:
            while val > end:
                tempList.append(val)
                val += step
        else:
            pass
        return tempList



    def __process__(self):
        
        if self.__ROVPosition.y > self.__startHeight:
            if not hasFinished:
                hasFinished = True
                print("ROV has scanned mine, will now pause.")
            else:
                return

        #TODO: ADD BUTTON TO ADVANCE FROM ONE STAGE TO THE NEXT
        if not (self.__stage == 2 and not self.isWithin(self.__ROVPosition,self.__nextNode)) and not (self.__MODE == 0):
            self.__stage += 1
            print("Moving to stage " + str(self.__stage))
            self.__unhandledStageChange = True
        
        if self.__stage == 1 and self.__unhandledStageChange:
            self.__unhandledStageChange = False
            self.__fastpath = find_path()

            if self.__fastpath.is_empty():
                return
            self.__nextNode = self.__fastpath[1]
            print("Position: " + str(self.__ROVPosition))
            print("Path returned from Dijkstra: " + str(self.__fastpath))
            
                
            
            if self.__MODE == 0:
                self.__stage += 1
                print("moving to stage 2")
                self.__unhandledStageChange = True
        
        #move toward next point
        elif self.__stage == 2 and not self.isWithin(self.__ROVPosition,self.__nextNode):
            
            #TODO: PUT IN MOVEMENT CODE HERE!!!!
            movementVector:tuple = self.__nextNode - self.__ROVPosition



            if self.checkCollisions(self.__ROVPosition,self.__nextNode) or self.checkCollisions(self.__nextNode, self.__fastpath[self.__pathInd + 1]):
                    print("Detected Future Collision! Moving to Stage 0")
                    self.resetNavigation()
            
            
        #if done moving
        elif self.__stage == 2 and self.isWithin(self.__ROVPosition,self.__nextNode):
            if not self.isWithin(self.__GOAL,self.__ROVPosition,0.2):
                print("Position: " + str(self.__ROVPosition) + ", goal: " + str(self.__GOAL))
                self.__prevNode = self.__ROVPosition
                self.__nextNode = self.__fastpath[self.__pathInd]
                self.__pathInd += 1
            else:
                print("ROV REACHED GOAL!")
                self.resetNavigation()
                #get_tree().quit()

            
            
    #Ok so Godot really doesn't like running this if there are too many nodes
    def generate_graph(self):
        self.__graph = Graph(undirected=True)
        for x in self.rangef(min(self.__minePoint1.x,self.__minePoint2.x),max(self.__minePoint1.x,self.__minePoint2.x),self.__NAVSPACING):
            for y in self.rangef(min(self.__minePoint1.y,self.__minePoint2.y),max(self.__minePoint1.y,self.__minePoint2.y),self.__NAVSPACING):
                for z in self.rangef(min(self.__minePoint1.z,self.__minePoint2.z),max(self.__minePoint1.z,self.__minePoint2.z),self.__NAVSPACING):
                    for xoff in self.rangef(-self.__NAVSPACING,self.__NAVSPACING,self.__NAVSPACING):
                        for yoff in self.rangef():
                            for zoff in self.rangef():
                                if not self.checkCollisions((x,y,z),(x+xoff,y+yoff,z+zoff)):
                                    self.__graph.add_edge((x,y,z),(x+xoff,y+yoff,z+zoff),sqrt((xoff ** 2) + (yoff ** 2) + (zoff ** 2)))
                                else:
                                    try:
                                        self.__graph.remove_edge((x,y,z),(x+xoff,y+yoff,z+zoff))
                                    except:
                                        self.__graph.remove_edge((x+xoff,y+yoff,z+zoff),(x,y,z))
                                


    def getMinKey(d:dict) -> tuple:
        if d.is_empty():
            print("ERROR: getMinKey was passed empty dict")
        return d.find_key(d.values().min())

    #For Collision Detection:
        #OLD FORMULA
        #for p in scanPoints:
        #	if dist(p,midPoint) <= (dist(p1,p2) / 2.0): #or (dist(p,p1) < dist(p1,p2) / 5.0) or (dist(p,p2) < dist(p1,p2) / 5.0):
        #		collList.append(p)
        
        #NEW FORMULA
        #Source: https://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html (distance to line defined by 2 points from point)
        #Source: https://math.stackexchange.com/questions/701584/check-point-is-between-two-points (check if line is between 2 points)
        # Ends up looking like this (sorry about the crude ascii art):
        #	 ______________________
        #   /       .              \
        #  |    O              O    |
        #   \______________________/
        #
        # if point is within bubble, it will be flagged
        #
    def checkCollisions(self, p1:tuple,p2:tuple,scanData=None) -> bool:
        if scanData == None:
            scanData = self.__scanPoints
        
        midpoint = (p1 + p2) / 2.0
        for p in self.__scanPoints:
            
            #just an optimization, don't have to do all of the fancy math if it's not within range
            if self.isWithin(midpoint,p,(p1.distance_to(p2) / 2) + self.__SAFEDIST):
                
                r = (p2 - p1).normalized().dot(p - p1)
                #if point is between sides
                if r >= 0 and r <= (p2 - p1).length():
                    
                    #then rely on distance to line formula
                    if (((self.crossProduct(self.tupleSub(p,p1),self.tupleSub(p,p2))).length() * 1.0) / self.dist(p1,p2) * 1.0) < self.__SAFEDIST:
                        return True
                #otherwise, use distance to point closest to it
                elif self.isWithin(p,p1,self.__SAFEDIST) or self.isWithin(p,p2,self.__SAFEDIST):
                    return True
        return False

    def dist(v1:tuple,v2:tuple) -> float:
        return sqrt(((v1.x - v2.x) ** 2) + ((v1.y - v2.y) ** 2) + ((v1.z - v2.z) ** 2))

    #Using dist squared because sqrt is costly time wise
    def isWithin(v1,v2,d) -> bool:
        return sqrt(((v1.x - v2.x) ** 2) + ((v1.y - v2.y) ** 2) + ((v1.z - v2.z) ** 2)) <= d

    def tupleAdd(v1:tuple,v2:tuple) -> tuple:
        return (v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

    def tupleSub(v1:tuple,v2:tuple) -> tuple:
        return (v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
        
    def tupleMag(v1:tuple,v2:tuple) -> float:
        return sqrt(((v1.x - v2.x) ** 2) + ((v1.y - v2.y) ** 2) + ((v1.z - v2.z) ** 2))
    
    def crossProduct(v1:tuple,v2:tuple) -> tuple:
        return (v1.y*v2.z + v1.z*v2.y,v1.zv2.x - v1.x*v2.z,v1.x*v2.y - v1.y*v2.x)

    def resetNavigation(self):
        self.__pathInd = 1
        self.__prevNode = self.__ROVPosition
        if self.__MODE == 0:
            self.__stage = 1
        else:
            self.__stage = 0
        self.__unhandledStageChange = True

    def recieveMessage(self, message):

        if 'linAcc_x' in message.getContents() and 'time' in message.getContents():
            timeElapsed = self.__time - message.getContents()['time']
            accx = message.getContents()['linAcc_x']
            accy = message.getContents()['linAcc_y']
            accz = message.getContents()['linAcc_z']

            self.__ROVVelocity += (accx*timeElapsed,accy*timeElapsed,accz*timeElapsed)
            self.__ROVPosition += (self.__ROVVelocity.x*timeElapsed,self.__ROVVelocity.y*timeElapsed,self.__ROVVelocity.z*timeElapsed)

        if 'scanData' in message.getContents():
            #TODO: fix this once you look into the dijkstar module
            for edge in self.__graph.edges:
                if self.checkCollisions(edge[0],edge[1],scanData=message.getContents()['scanData']):
                    self.__graph.remove_edge(edge)
                    self.resetNavigation()

        if 'time' in message.getContents():
            self.__time = message.getContents()['time']