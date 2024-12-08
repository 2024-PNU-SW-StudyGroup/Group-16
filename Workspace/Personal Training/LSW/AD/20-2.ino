// Slave
#include <Wire.h>
#define SLAVE 4

void setup(){
    Wire.begin(SLAVE);
    Wire.onReceive(receiveFromMaster);
    Serial.begin(9600);
}

void loop(){}

int bytes2int(byte a, byte b){
    return (a << 8) + b;
}

void receiveFromMaster(int bytes){
    byte r1 = Wire.read();
    byte r2 = Wire.read();
    int value = bytes2int(r1, r2);
    Serial.println(value);
}