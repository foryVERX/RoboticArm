// Define color sensor pins

#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define sensorOut 8

// For IR SENSOR
int digitalPinIR = 9;
int IrData = 0;
int readFlag = 0;

// Calibration Values
// Get these from Calibration Sketch

String userInput; // user input value
int redMin = 30; // Red minimum value
int redMax = 492; // Red maximum value
int greenMin = 30; // Green minimum value
int greenMax = 612; // Green maximum value
int blueMin = 20; // Blue minimum value
int blueMax = 476; // Blue maximum value

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
    //userInput = Serial.read();
    // Start Motor
    int i = 0;
    outputIrToSerialPort();
    while (IrData == 1){
            outputIrToSerialPort();
            outputCsToSerialPort(i);
            i++;
    }
}
    //if (IrData == 0){
      //delay(1000);
      //serial_flush();
    //}


int outputCsToSerialPort(int i) {
    // Read Red value
    redPW = getRedPW();
    // Map to value from 0-255
    redValue = map(redPW, redMin,redMax,255,0);
    // Delay to stabilize sensor
    delay(0.1);
    
    // Read Green value
    greenPW = getGreenPW();
    // Map to value from 0-255
    greenValue = map(greenPW, greenMin,greenMax,255,0);
    // Delay to stabilize sensor
    delay(0.1);
    
    // Read Blue value
    bluePW = getBluePW();
    // Map to value from 0-255
    blueValue = map(bluePW, blueMin,blueMax,255,0);
    // Delay to stabilize sensor
    delay(0.1);
    // Print output to Serial Monitor
    if (i > 3){
    Serial.print("R");
    Serial.print(redValue);
    Serial.print("G");
    Serial.print(greenValue);
    Serial.print("B");
    Serial.print(blueValue);
    delay(100);
    //serial_flush();
    }

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

int outputIrToSerialPort(){
      IrData = digitalRead(digitalPinIR);
      IrData = 1 - IrData;
      delay(0.3);
      serial_flush();
      return IrData;
}
