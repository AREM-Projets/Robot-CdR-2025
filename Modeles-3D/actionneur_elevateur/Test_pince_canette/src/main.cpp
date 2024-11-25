#include <Arduino.h>
#include <Servo.h>

Servo servo;


void setup() {
  servo.attach(A1);
  servo.write(90);
  delay(1000);
  servo.write(10);
  delay(500);
  servo.detach();
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
