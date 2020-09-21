const int pwm = 3;
const int dir = 4;
int pwm_value = 240;

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
  Serial.print("PWM: ");
  Serial.println(pwm_value);
}
