// For IR SENSOR
int digitalPinIR = 9;
int IrData = 0;
int xi;

// Collor Sensor
#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define sensorOut 8
String userInput; // user input value
int redMin = 63;// Red minimum value
int redMax = 177; // Red maximum value
int greenMin = 86; // Green minimum value
int greenMax = 206; // Green maximum value
int blueMin = 75; // Blue minimum value
int blueMax = 177; // Blue maximum value

// Define functions
int outputToSerialPort();
int getRedPW();
int getGreenPW();
int getBluePW();

// Variables for Color Pulse Width Measurements
int redPW = 0;
int greenPW = 0;
int bluePW = 0;

// Variables for final Color values
int redValue;
int greenValue;
int blueValue;


void setup() {
  int xi = 0;
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
    // Set S0 - S3 as outputs
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);

  // Function to clear the buffer
  serial_flush();
  // Set Sensor output as input
  pinMode(sensorOut, INPUT);
  
  // Set Frequency scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  
  // Setup Serial Monitor
  Serial.begin(9600);
}

void loop() {
  IrData = digitalRead(digitalPinIR);
  IrData = 1 - IrData;
  if (IrData == 0){
    serial_flush();
    digitalWrite(13, HIGH);
  }
  else{
  digitalWrite(13, LOW);
  if(Serial.available()>0){
    userInput = Serial.readStringUntil('\n');
    if(userInput == "c"){
      xi = 0;
      outputCsToSerialPort(xi);
      xi = xi + 1;
      outputCsToSerialPort(xi);
      xi = xi + 1;
      outputCsToSerialPort(xi);
      xi = xi + 1;  
    }
  }
    }
}

int outputCsToSerialPort(int xi) {
    // Read Red value
    
    redPW = getRedPW();
    // Map to value from 0-255
    redValue = map(redPW, redMin,redMax,255,0);
    // Delay to stabilize sensor
    delay(200);
    
    // Read Green value
    greenPW = getGreenPW();
    // Map to value from 0-255
    greenValue = map(greenPW, greenMin,greenMax,255,0);
    // Delay to stabilize sensor
    delay(200);
    
    // Read Blue value
    bluePW = getBluePW();
    // Map to value from 0-255
    blueValue = map(bluePW, blueMin,blueMax,255,0);
    // Delay to stabilize sensor
    delay(200);
    // Print output to Serial Monitor
    if (xi == 2){
      Serial.print("R");
      Serial.print(redValue);
      Serial.print("G");
      Serial.print(greenValue);
      Serial.print("B");
      Serial.print(blueValue);
      Serial.println();
      delay(100);
    }
    //serial_flush();

}
      
// Function to read Red Pulse Widths
int getRedPW() {

  // Set sensor to read Red only
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  // Define integer to represent Pulse Width
  int PW;
  // Read the output Pulse Width
  PW = pulseIn(sensorOut, LOW);
  // Return the value
  return PW;

}

// Function to read Green Pulse Widths
int getGreenPW() {
  // Set sensor to read Green only
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  // Define integer to represent Pulse Width
  int PW;
  // Read the output Pulse Width
  PW = pulseIn(sensorOut, LOW);
  // Return the value
  return PW;
}


// Function to read Blue Pulse Widths
int getBluePW() {

  // Set sensor to read Blue only
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  // Define integer to represent Pulse Width
  int PW;
  // Read the output Pulse Width
  PW = pulseIn(sensorOut, LOW);
  // Return the value
  return PW;
}

void serial_flush(void) {
  while (Serial.available()) Serial.read();
}
