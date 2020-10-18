const int pwm = 3;
const int dir = 4;
int pwm_value = 0;
int incomingByte = 0; // for incoming serial data
int userInput = 0; //a number from the serial monitor

void setup()
{
  Serial.begin(9600);
  pinMode(pwm,OUTPUT);
  pinMode(dir,OUTPUT);
}

void loop()
{
  digitalWrite(dir,LOW);
  analogWrite(pwm,pwm_value);

  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    // say what you got:
    //Serial.print("I received: ");
    //Serial.println(incomingByte, DEC);

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
