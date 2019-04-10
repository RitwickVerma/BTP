
#include "ACS712.h"

int x=5;
int vsbatPin=0;
int csbatPin=1;

float R1 = 30000.0; //30k
float R2 = 7500.0; //7500 ohm resistor, I tweaked this
int value = 0;

ACS712 sensor(ACS712_20A, A1);

void setup() {

  pinMode(LED_BUILTIN, OUTPUT);
  
  int zero = sensor.calibrate();
  
  Serial.begin(9600); // Starts the serial communication
  /*while(true)
  {
    if (Serial.available() > 0) {
        char c = Serial.read();
        if(c=='x') break;
    }
    Serial.print("1");
    Serial.println();
    
    delay(100);  
  }*/
  
}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH); 
  
   float value = analogRead(vsbatPin);
   float temp = (value * 4.5) / 1024.0;
   float vsbat = temp / (R2/(R1+R2));
   
   float csbat = sensor.getCurrentDC();
   
  Serial.print("vsbat:");
  Serial.print(vsbat);
  Serial.print("|");
  
  Serial.print("csbat:");
  Serial.print(csbat);
  Serial.print("|");

  Serial.println("wtf:yo");
  
  delay(100);
}
