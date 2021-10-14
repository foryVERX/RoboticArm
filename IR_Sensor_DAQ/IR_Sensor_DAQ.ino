#define IR 8

int Obstacle;

void setup() {
  pinMode(IR, INPUT);
  Serial.begin(9600);
}

void loop() {
  Obstacle = digitalRead(IR);

  if (Obstacle == LOW) {
    Serial.println("STOP");
  }
 else {
   Serial.println("All Clear");

  }
  delay(500);
}
