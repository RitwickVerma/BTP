
#include "ACS712.h"

int x=5;
int vsbatPin=0;
int csbatPin=1;
int vspanPin=2;
int cspanPin=3;

float R1 = 30000.0; //30k
float R2 = 7500.0; //7500 ohm resistor, I tweaked this
int value = 0;

ACS712 currsensor1(ACS712_20A, A1);
ACS712 currsensor2(ACS712_20A, A3);

void setup() {

  pinMode(LED_BUILTIN, OUTPUT);
  
  currsensor1.calibrate();
  currsensor2.calibrate();
  
  Serial.begin(9600); // Starts the serial communication
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
void loop() {
  digitalWrite(LED_BUILTIN, HIGH); 
  
   float value = analogRead(vsbatPin);
   float temp = (value * 4.5) / 1024.0;
   float vsbat = temp / (R2/(R1+R2));
   
   float csbat = currsensor1.getCurrentDC();

   value = analogRead(vspanPin);
   temp = (value * 4.5) / 1024.0;
   float vspan = temp / (R2/(R1+R2));
   
   float cspan = currsensor2.getCurrentDC();

  Serial.print("vsbat:");
  Serial.print("S");//vsbat);
  Serial.print("|");
  
  Serial.print("csbat:");
  Serial.print("W");//csbat);
  Serial.print("|");

  Serial.print("vspan:");
  Serial.print("A");//vspan);
  Serial.print("|");
  
  Serial.print("cspan:");
  Serial.print("G");//cspan);hello
  Serial.print("|");

  Serial.println("wtf:yo");
  
  delay(100);
}
