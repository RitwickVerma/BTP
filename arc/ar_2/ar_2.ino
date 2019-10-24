const int trigPinleft = 12;
const int echoPinleft = 11;

const int trigPinright = 10;
const int echoPinright = 9;

long durationleft;
int distanceleft;

long durationright;
int distanceright;


const int trigPinback = 7;
const int echoPinback = 6;


long durationback;
int distanceback;


int z=0,w=0;

int x=0,y=0;

void handshake()
{
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

void setup() {
  pinMode(trigPinleft, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinleft, INPUT); // Sets the echoPin as an Input

  pinMode(trigPinright, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinright, INPUT); // Sets the echoPin as an Input*/


  pinMode(trigPinback, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPinback, INPUT); // Sets the echoPin as an Input

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600); // Starts the serial communication
  // handshake();
}

void loop() {

  digitalWrite(LED_BUILTIN, HIGH); 

  digitalWrite(trigPinleft, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinleft, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinleft, LOW);
  durationleft = pulseIn(echoPinleft, HIGH);

  digitalWrite(trigPinright, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinright, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinright, LOW);
  durationright = pulseIn(echoPinright, HIGH);

  distanceleft = durationleft * 0.034 / 2;
  distanceright = durationright * 0.034 / 2;



  digitalWrite(trigPinback, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinback, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinback, LOW);
  durationback = pulseIn(echoPinback, HIGH);

  distanceback = durationback * 0.034 / 2;

  Serial.print("usld:");
  Serial.print(distanceleft);
  Serial.print("|");

  Serial.print("usrd:");
  Serial.print(distanceright);
  Serial.print("|");

  Serial.print("usbd:");
  Serial.print(distanceback);

  Serial.println();
  
  x++;
  y++;
  z++;
  w++;

  delay(100);
}