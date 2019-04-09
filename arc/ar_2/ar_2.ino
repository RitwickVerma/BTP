const int trigPinfl = 12;
const int echoPinfl = 11;

const int trigPinfr = 10;
const int echoPinfr = 9;

long durationfl;
int distancefl;

long durationfr;
int distancefr;


const int trigPinbl = 8;
const int echoPinbl = 7;

const int trigPinbr = 6;
const int echoPinbr = 5;

long durationbl;
int distancebl;

long durationbr;
int distancebr;


int z=0,w=0;

int x=0,y=0;

void setup() {
  pinMode(trigPinfl, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinfl, INPUT); // Sets the echoPin as an Input

  pinMode(trigPinfr, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinfr, INPUT); // Sets the echoPin as an Input*/


  pinMode(trigPinbl, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinbl, INPUT); // Sets the echoPin as an Input

  pinMode(trigPinbr, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinbr, INPUT); 

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


  /*digitalWrite(trigPinfl, LOW);
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
  distancebr = durationbr * 0.034 / 2;*/


  Serial.print("usfld:");
  Serial.print(x);//distancefl);
  Serial.print("|");

  Serial.print("usfrd:");
  Serial.print(y);//distancefr);
  Serial.print("|");

  Serial.print("usbld:");
  Serial.print(z);//distancebl);
  Serial.print("|");

  Serial.print("usbrd:");
  Serial.print(w);//distancebr);

  Serial.println();
  
  x++;
  y++;
  z++;
  w++;

  delay(100);
}
