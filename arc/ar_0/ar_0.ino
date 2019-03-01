int trigPin=13;

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

  if (Serial.available() > 0) {
        char c = Serial.read();
        if(c=='o') digitalWrite(trigPin, HIGH); 
        else if(c=='x') digitalWrite(trigPin, LOW); 
  }
  
  Serial.println("relay:test");
  
  delay(100);
}
