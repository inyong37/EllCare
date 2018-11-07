#include <SoftwareSerial.h>
 
SoftwareSerial hm10(2,3); //RX, TX 연결
 
void setup() {
  Serial.begin(9600);
  hm10.begin(9600);
}
 
void loop() {
  while(hm10.available()){
    byte data=hm10.read();
    Serial.write(data);
  }
  while(Serial.available()){

    byte data=Serial.read();
    hm10.write(data);
  }
}
