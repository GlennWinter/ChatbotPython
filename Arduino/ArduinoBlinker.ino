void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
  String input = Serial.readStringUntil('\n');
  
  if (input == "ON"){
  digitalWrite(13, HIGH);
  }

  if (input =="OFF"){
  digitalWrite(13, LOW);
    
}
}

