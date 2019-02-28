
const int trigPinbl = 10;
const int echoPinbl = 13;



const int trigPinbr = 11;
const int echoPinbr = 12;

long durationbl;
int distancebl;


long durationbr;
int distancebr;

  int x=-2000,y=-6000;

void setup() {
  pinMode(trigPinbl, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinbl, INPUT); // Sets the echoPin as an Input


  pinMode(trigPinbr, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinbr, INPUT); // Sets the echoPin as an Input

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600); // Starts the serial communication
  while(true)
  {
    if (Serial.available() > 0) {
        char c = Serial.read();
        if(c=='x') break;
    }
    Serial.print("3");
    Serial.println();
    
    delay(100);  
  }
  
}
void loop() {

  digitalWrite(LED_BUILTIN, HIGH); 

  digitalWrite(trigPinbl, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinbl, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinbl, LOW);
  durationbl = pulseIn(echoPinbl, HIGH);


  digitalWrite(trigPinbr, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinbr, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinbr, LOW);
  durationbr = pulseIn(echoPinbr, HIGH);


  distancebl = durationbl * 0.034 / 2;
  distancebr = durationbr * 0.034 / 2;

  Serial.print("usbld:");
  Serial.print(x);
  Serial.print("|usbrd:");
  Serial.println(y);
  x++;
  y++;

  delay(100);
}
