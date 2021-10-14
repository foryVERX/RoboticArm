#define IR 8

int IRSensor_output;

void setup() {
  pinMode(IR, INPUT);
  Serial.begin(9600);
}

void loop() {
  IRSensor_output = digitalRead(IR);
  Serial.println(IRSensor_output);
  delay(500);
}
