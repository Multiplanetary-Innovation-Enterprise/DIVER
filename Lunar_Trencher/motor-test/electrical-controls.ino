//******************************************************************************
//* Trencher BLDC Motor controls and sensor output
//*   Currently, motor is controlled via 3 external periherals:
//*     Push button: Toggles motor stopping and starting
//*     Switch: Changes rotation of motor
//*     Potentiometer: Changes speed of motor
//* Author: Conor Porter
//* Last Modified: 11/10/2020
//******************************************************************************

//Motor outputs
const int pwm = 3; //PWM pin
const int dir = 4; //non-PWM pin

//Button/switch inputs
const int stp = 2; //non-PWM pin
const int start = 7; //non-PWM pin

//Sonic sensor IO
const int trig = 9; //non-PWM pin
const int echo = 10; //non-PWM pin

//Current Sensor input
const int ampVin = 3; //analog pin: potentiometer wiper (middle terminal) connected to analog pin 3
const int potPin = 2; //analo pin: potentiometer for controlling speed
int reading = 0; // variable to store the value read
int potRead = 0;
long maxVal = 0;
int samples = 1000; // how many samples per reading

//constants for converting amp sensor reading
const int zeroAmp = 513;
const int halfAmp = 7;
double amps = 0.0;

//Motor control variables
const float potToPWM = 4.011764706; //conversion for controlling speed of motor (1k Ohm ~ 255)
int pwm_value = 0; //relates to speed of motor
int incomingByte = 0; // for incoming serial data
int userInput = 0; //a number from the serial monitor
int startState = 0; //for checking if motor must hard stop
int toggleStop = 0; //for using button as a toggle switch
int stopState = 0; //for checking if motor must start

//RPM data variables
unsigned long rpmStartTime = NULL; //keeps track of clock
int rpmSamples = 8; //how many times to read ultrasonic sensor to get accurate value
float prevDistance = 11; //for handling noise from ultrasonic sensor
float bucketDistance = 10; //distance from sensor to buckets
double bucketRPMs = 0; //placeholder for final converted value
int bucketCount = 0; //keep track of how many go by

//value for buckets and chain for tracking RPMs
const double distBucketToBucket = 1; //1.5ft min
//495.3mm is center of sprocket to center of sprocket sprocket distance (7-8inch diameter sprocket)
// \/ roughly 5.8 ft of chain for the min \/ (93.5 links)
const double distTrackLength = 1;
const int numberOfBuckets = 4;

void setup()
{
  Serial.begin(9600);
  //initialize outputs
  pinMode(pwm,OUTPUT);
  pinMode(dir,OUTPUT);
  pinMode(trig, OUTPUT);
  //initialize inputs
  pinMode(stp, INPUT);
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
  if (Serial.available() > 0)
  {
    // read the incoming byte:
    incomingByte = Serial.read();

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

    //if button pressed, stop
    checkToStopMotor();
    //if button is not pressed, accelerate motor
    checkToStartMotor();
    //measure rotations per minute of the bucket track
    measureBucketRPMs();
    //measure current flowing through motor
    measureMotorCurrent();

}

void checkToStopMotor()
{// NOTE: will require modifcation when transistors are set up with EN and BRK to make hard stopping possible
  // read the state of the pushbutton value:
  stopState = digitalRead(stp);
  // check if the pushbutton is pressed. If it is, stop the motor:
  if (stopState == HIGH)
  {
    toggleStop = toggleStop ^ 1;
    Serial.print("Motor stopped: ");
    Serial.println(toggleStop);
    pwm_value = 0;
    while (digitalRead(stp) == HIGH); //polling loop to wait for you to let off on the button
  }
}

void checkToStartMotor()
{
  // read the state of the pushbutton value:
  startState = digitalRead(start);

  // check if the switch is on and button is not pressed. If so, accelerate motor to max speed
  if (toggleStop == 0)
  {
    controlSpeed();
    //start recording clock for tracking RPM data
    if (rpmStartTime == NULL) rpmStartTime = millis();
  }
}

void measureBucketRPMs()
{
  //trigger sonic sensor and record output
  float duration;
  float distance = bucketDistance + 1;
  for (int counter = 0; counter < rpmSamples; counter++)
  {
    digitalWrite(trig, LOW);
    delayMicroseconds(500);
    digitalWrite(trig, HIGH);
    delayMicroseconds(500);
    digitalWrite(trig, LOW);
    duration = pulseIn (echo, HIGH);
    if (distance > ( (duration/2)/29 )) distance = (duration/2)/29;
  }

  unsigned long rpmEndTime = millis();
  //if less than 10cm from dist sensor
  if (distance < bucketDistance && prevDistance > bucketDistance)
  {
    Serial.print(distance);
    Serial.println(" cm");
    Serial.print(prevDistance);
    Serial.println(" prev");
    bucketCount++;
    if (bucketCount == numberOfBuckets + 1) //plus 1 means it went full circle
    {
      double rpmDelta = ( (float) (rpmEndTime - rpmStartTime) ) / 1000; //time in seconds
      bucketCount = 0;
      bucketRPMs = 1.0 / ((rpmDelta) / 60.0);
      Serial.print("RPM: ");
      Serial.print(bucketRPMs);
      Serial.print(" ");
      Serial.println(millis());
      rpmStartTime = millis();
    }
  }
  prevDistance = distance;
}

void measureMotorCurrent()
{
  maxVal = 0;
  // delay(500);
  // digitalWrite(13, !digitalRead(13));
  for (int counter = 1; counter < samples; counter++) {
    reading = analogRead(ampVin); // read the input pin
    if (reading > maxVal)
    {
      maxVal = reading;
    }
  }
  amps = ( ( ((double) maxVal) - ((double) zeroAmp) ) / ((double) halfAmp) ) / 2.0;
  Serial.print("Current: ");
  Serial.print(amps);
  Serial.print(" ");
  Serial.println(millis());
}

void controlSpeed()
{
  potRead = analogRead(potPin);
  pwm_value = potRead / potToPWM;
}
