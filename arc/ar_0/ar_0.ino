int trigPin=13;
int buttPin=12;
int irPin=8;
int bsbelt=0;
int psseated=0;
int x=550;
void setup() {

  pinMode(buttPin, INPUT);
  pinMode(irPin, INPUT);

  Serial.begin(9600); // Starts the serial communication
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
void loop() {
  bsbelt=digitalRead(buttPin);
  psseated=digitalRead(irPin);
  
  Serial.print("psseated:");
  Serial.print(psseated);
  Serial.print("|");

  Serial.print("bsbelt:");
  Serial.print(bsbelt);
  Serial.print("|");
  
  Serial.print("psrpm:");
  Serial.println(x);
  x++;
  
  delay(100);
}
