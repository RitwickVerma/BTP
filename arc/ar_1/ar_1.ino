int x=5;
void setup() {

  pinMode(LED_BUILTIN, OUTPUT);

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

  Serial.println("wtf:yo");
  
  delay(100);
}
