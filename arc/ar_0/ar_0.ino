int trigPin=13;
int x=550;
void setup() {

  pinMode(trigPin, OUTPUT);

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

  Serial.print("psseated:");
  Serial.print("1");
  Serial.print("|");

  Serial.print("bsbelt:");
  Serial.print("1");
  Serial.print("|");
  
  Serial.print("psrpm:");
  Serial.println(x);
  x++;
  
  delay(100);
}
