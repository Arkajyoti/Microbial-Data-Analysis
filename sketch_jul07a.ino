/* Example sketch to control a stepper motor with TB6600 stepper motor driver and Arduino without a library: number of revolutions, speed and direction. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
#define dirPin 2
#define stepPin 3
// Define parameters
#define stepsPerRevolution 800 //  = 180 degree rotation
#define speedR 1500 // 1/rotation speed
#define speedR2 200 // 1/rotation speed
#define delay0 3000
#define NoOfHalfRot 1 // Number of half rotations
#define delay1 2500 // Delay b/w 2 rotations (motility)
#define delay2 5000// Inf Delay
//#define delay3 30000
void setup() {
  // Declare pins as output:
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}

void loop() {
  // Set the spinning direction clockwise:
  digitalWrite(dirPin, HIGH);

  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < NoOfHalfRot*stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedR);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedR2);
  }

  delay(delay0); // delay of 5 seconds

  // Set the spinning direction counterclockwise:
  digitalWrite(dirPin, LOW);

  // Spin the stepper motor 1 revolution quickly:
  for (int i = 0; i < NoOfHalfRot*stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedR);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedR2);
  }

  delay(delay1);

  //Second flip
  digitalWrite(dirPin, LOW);

  // Spin the stepper motor 1 revolution quickly:
  for (int i = 0; i < NoOfHalfRot*stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedR);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedR2);
  }

  delay(delay1);

  digitalWrite(dirPin, HIGH);

  // Spin the stepper motor 1 revolution quickly:
  for (int i = 0; i < NoOfHalfRot*stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(speedR);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(speedR2);
  }

  delay(delay2);
}
