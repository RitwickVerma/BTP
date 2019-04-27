#include <max6675.h>

#include <dht.h>

#define dhtPin A0
int buttPin=13;
int irPin=5;
const byte hsPin = 2;

int bsbelt=0;
int psseated=0;
float hsrpm=0;
float lastrpm=0;
float hsspeed=0;
float hsdist=0;
int count=0;


float lasttime=0,deltatime=1;

dht dhttemp;

int thermoDO = 12;
int thermoCS = 11;
int thermoCLK = 10;
int thermoVCC = 9;
int thermoGND = 8;

MAX6675 tctemp(thermoCLK, thermoCS, thermoDO);

void handshake()
{
  while(true)
  {
    if (Serial.available() > 0) {
        char c = Serial.read();
        if(c=='x') break;
    }
    Serial.print("0");
    Serial.println();
    
    delay(100);  
  }
}

void setup() {

  pinMode(buttPin, INPUT);
  pinMode(irPin, INPUT);

  pinMode(thermoVCC, OUTPUT);
  digitalWrite(thermoVCC,HIGH);
  pinMode(thermoGND, OUTPUT);
  digitalWrite(thermoGND,LOW);
  
  pinMode(hsPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(hsPin), isr, RISING);
  lasttime=millis();
  Serial.begin(9600);
  handshake();
  
}
void loop() {
  bsbelt=digitalRead(buttPin);
  psseated=digitalRead(irPin);

  hsrpm=60*1000/deltatime;
  hsspeed=(hsrpm*20/100)/60;
  hsdist=hsdist+hsspeed*deltatime/1000;
  if(lastrpm==hsrpm)
  {
    count++;
    if(count>=20)
    {
      hsrpm=0;
      deltatime=INFINITY;
      count=0;
    }
  }
  lastrpm=hsrpm;

  dhttemp.read11(dhtPin);
  
  Serial.print("psseated:");
  Serial.print(psseated);
  Serial.print("|");

  Serial.print("bsbelt:");
  Serial.print(bsbelt);
  Serial.print("|");
  
  Serial.print("hsrpm:");
  Serial.print(hsrpm);
  Serial.print("|");

  Serial.print("hsspeed:");
  Serial.print(hsspeed);
  Serial.print("|");

  Serial.print("hsdist:");
  Serial.print(hsdist);
  Serial.print("|");

  Serial.print("dhtt:");
  Serial.print(dhttemp.temperature);
  Serial.print("|");

  Serial.print("dhth:");
  Serial.print(dhttemp.humidity);
  Serial.print("|");

  Serial.print("tct:");
  Serial.println(tctemp.readCelsius());
    
  delay(100);
}

void isr() {
  deltatime=millis()-lasttime;
  lasttime=millis();
}
