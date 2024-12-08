// Master
#include <Wire.h>
#define  SLAVE 4

int trigPin = 3;
int echopin = 2;

void setup(){
    Wire.begin(SLAVE);
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echopin, INPUT);
}

void i2c_communication(int reading){
    Wire.beginTransmission(SLAVE);
    Wire.write(reading >> 8);
    Wire.write(reading & 0xFF);
    Wire.endTransmission(SLAVE);
}

void loop(){
    digitalWrite(trigPin, HIGH);
    delay(10);
    digitalWrite(trigPin, LOW);
    float duration = pulseIn(echopin, HIGH);

    float distance = duration * 340 / 10000 / 2;
    i2c_communication(int(distance));

    delay(500);
}
