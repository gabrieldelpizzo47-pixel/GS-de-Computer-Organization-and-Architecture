int A = 2; // Falha de comunicacao
int B = 3; // Temperatura critica
int C = 4; // Baixo nivel de energia
int D = 5; // Falha em modulo operacional
int E = 6; // Perda de estabilidade

int LED_VERMELHO = 12; // Alerta
int LED_VERDE = 13;    // Normal

void setup()
{
  pinMode(A, INPUT_PULLUP);
  pinMode(B, INPUT_PULLUP);
  pinMode(C, INPUT_PULLUP);
  pinMode(D, INPUT_PULLUP);
  pinMode(E, INPUT_PULLUP);

  pinMode(LED_VERMELHO, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);

  digitalWrite(LED_VERMELHO, LOW);
  digitalWrite(LED_VERDE, LOW);

  delay(1000);
}

void loop()
{
  int a = !digitalRead(A);
  int b = !digitalRead(B);
  int c = !digitalRead(C);
  int d = !digitalRead(D);
  int e = !digitalRead(E);

  // X = (A · C) + (B · D) + (E · ¬C)
  int X = (a && c) || (b && d) || (e && !c);

  if (X == 1) {
    digitalWrite(LED_VERMELHO, HIGH); // alerta
    digitalWrite(LED_VERDE, LOW);
  } else {
    digitalWrite(LED_VERMELHO, LOW);
    digitalWrite(LED_VERDE, HIGH); // normal
  }
}
