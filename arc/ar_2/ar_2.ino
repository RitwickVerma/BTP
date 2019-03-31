const int trigPinfl = 12;
const int echoPinfl = 11;


const int trigPinfr = 10;
const int echoPinfr = 9;

long durationfl;
int distancefl;


long durationfr;
int distancefr;

int x=-1000,y=-5000;

void setup() {
  pinMode(trigPinfl, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinfl, INPUT); // Sets the echoPin as an Input


  pinMode(trigPinfr, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinfr, INPUT); // Sets the echoPin as an Input*/

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600); // Starts the serial communication
  while(true)
  {
    if (Serial.available() > 0) {
        char c = Serial.read();
        if(c=='x') break;
    }
    Serial.print("2");
    Serial.println();

    delay(100);  
  }
}
void loop() {

  digitalWrite(LED_BUILTIN, HIGH); 

  digitalWrite(trigPinfl, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinfl, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinfl, LOW);
  durationfl = pulseIn(echoPinfl, HIGH);


  digitalWrite(trigPinfr, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinfr, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinfr, LOW);
  durationfr = pulseIn(echoPinfr, HIGH);


  distancefl = durationfl * 0.034 / 2;
  distancefr = durationfr * 0.034 / 2;

  Serial.print("usfld:");
  Serial.print(distancefl);
  Serial.print("|");

  Serial.print("usfrd:");
  Serial.print(distancefr);
  Serial.println();

  "usfld:52|usfrd:89|asdsa:123|asdas:55"

  delay(100);
}
