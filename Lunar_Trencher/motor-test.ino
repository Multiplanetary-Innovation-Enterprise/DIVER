//Motor outputs
const int pwm = 3; //PWM pin
const int dir = 4; //non-PWM pin
//Button/switch inputs
const int stop = 2; //non-PWM pin
const int start = 7; //non-PWM pin
//Sonic sensor IO
const int trig = 12; //non-PWM pin
const int echo = 13; //non-PWM pin
//Current Sensor input
const int ampVin = 3; //analog pin: potentiometer wiper (middle terminal) connected to analog pin 3
int reading = 0; // variable to store the value read
long maxVal = 0;
int samples = 10000; // how many samples per reading

int pwm_value = 0;
int incomingByte = 0; // for incoming serial data
int userInput = 0; //a number from the serial monitor
int startState = 0; //for checking if motor must hard stop
int toggleStop = 0; //for using button as a toggle switch
int startState = 0; //for checking if motor must start
unsigned long rpmStartTime = NULL;
unsigned long rpmEndTime;
int bucketRPMs = 0;
int bucketCount = 0; //keep track of how many go by
//values ill need from the ME team for tracking RPMs
const int distBucketToBucket = 1;
const int distTrackLength = 1;
const int numberOfBuckets = 1;

void setup()
{
  Serial.begin(9600);
  //initialize outputs
  pinMode(pwm,OUTPUT);
  pinMode(dir,OUTPUT);
  pinMode(trig, OUTPUT);
  //initialize inputs
  pinMode(stop, INPUT);
  pinMode(start, INPUT);
  pinMode(echo, INPUT);
  //for current sensor
  pinMode(13, OUTPUT); 
  digitalWrite(2, HIGH);
}

void loop()
{
  digitalWrite(dir,LOW);
  analogWrite(pwm,pwm_value);

  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    
    //if button pressed, stop
    checkToStopMotor();
    //if switch is on and button is not pressed, accelerate motor
    checkToStartMotor();
    //measure rotations per minute of the bucket track
    measureBucketRPMs();
    //measure current flowing through motor
    measureMotorCurrent();
    
    //convert ascii bytes into numbers
    if (incomingByte > 47 && incomingByte < 72)
    {
      userInput = (userInput * 10) + (incomingByte - 48);
    }

    //write input to PWM, print to monitor, and reset userInput
    if (incomingByte == 10 && userInput != 0) //last byte is always 10 to signify end of data
    {
      Serial.print("Old PWM: ");
      Serial.println(pwm_value);
      pwm_value = userInput;
      Serial.print("New PWM: ");
      Serial.println(pwm_value);
      userInput = 0;
      Serial.print("UI reset to: ");
      Serial.println(userInput);
    }
  }
}

void checkToStopMotor()
{// NOTE: will require modifcation when transistors are set up with EN and BRK to make hard stopping possible
  // read the state of the pushbutton value:
  stopState = digitalRead(stop);

  // check if the pushbutton is pressed. If it is, stop the motor:
  if (buttonState == HIGH) 
  {
    toggleStop = toggleStop ^ 1;
    pwm_value = 0;
  } 
}

void checkToStartMotor()
{
  // read the state of the pushbutton value:
  startState = digitalRead(stop);

  // check if the switch is on and button is not pressed. If so, accelerate motor to max speed
  if (toggleStop == 0 && startState == HIGH) 
  {
    if (pwm_value < 255) pwm_value += 5;
    //start recording clock for tracking RPM data
    if (rpmStartTime == NULL) rpmStartTime = millis(); 
  } 
}

void measureBucketRPMs()
{
  //trigger sonic sensor and record output
  float duration, distance;
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig_pin, LOW);
  duration = pulseIn (echo_pin, HIGH);
  distance = (duration/2)/29;
  Serial.print(distance);
  Serial.println(" cm");
  //if less than 10cm from dist sensor
  if (distance < 10)
  {
    rpmEndTime = millis();
    unsigned long rpmDelta = (rpmEndTime - rpmStartTime) / 1000; //time in seconds
    bucketCount++;
    if (bucketCount == numberOfBuckets + 1) //plus 1 means it went full circle
    {
      bucketCount = 0;
      bucketRPMs = (distTrackLength / rpmDelta) / 60;
      Serial.print(bucketRPMs);
      Serial.println(" RPMs");
    }
  }
}

void measureMotorCurrent()
{
  maxVal = 0;
  // delay(500);
  // digitalWrite(13, !digitalRead(13));
  for (int counter = 1; counter < samples; counter++) { 
    reading = analogRead(analogPin); // read the input pin
    if (reading > maxVal)
    {
      maxVal = reading;
    }
  }
  Serial.println(maxVal); // debug value 
}
