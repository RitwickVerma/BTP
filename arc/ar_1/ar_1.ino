
#include "ACS712.h"

int x=5;
int vsbatPin=2;
#define csbatPin A5
int vspanPin=4;
#define cspanPin A3

float R1 = 30000.0; //30k
float R2 = 7500.0; //7500 ohm resistor, I tweaked this
int value = 0;

ACS712 currsensbat(ACS712_20A, csbatPin);
ACS712 currsenspan(ACS712_20A, cspanPin);

void handshake()
{
  while(true)
  {
    if (Serial.available() > 0) {
        char c = Serial.read();
        if(c=='x') break;
    }
    Serial.print("1");
    Serial.println();
    
    delay(100);  
  }
}

void setup() {

  pinMode(LED_BUILTIN, OUTPUT);
  
  currsensbat.calibrate();
  currsenspan.calibrate();
  
  Serial.begin(9600); // Starts the serial communication
  handshake();
  
}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH); 
  
   float value = analogRead(vsbatPin);
   float temp = (value * 4.5) / 1024.0;
   float vsbat = temp / (R2/(R1+R2));
   
   float csbat = currsensbat.getCurrentDC()*1000;

   value = analogRead(vspanPin);
   temp = (value * 4.5) / 1024.0;
   float vspan = temp / (R2/(R1+R2));
   
   float cspan = currsenspan.getCurrentDC()*1000;

  Serial.print("vsbat:");
  Serial.print(vsbat);
  Serial.print("|");
  
  Serial.print("csbat:");
  Serial.print(csbat);
  Serial.print("|");

  Serial.print("vspan:");
  Serial.print(vspan);
  Serial.print("|");
  
  Serial.print("cspan:");
  Serial.print(cspan);

  Serial.println();
  
  delay(100);
}
