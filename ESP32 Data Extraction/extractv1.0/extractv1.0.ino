/*
   Cheat Sheet:
   0 - ADC CH1 Cloud
   1 - ADC CH2 Cloud
   2 - ADC CH3 Cloud
   3 - ADC CH4 Cloud
   4 - ADC CH1 Local
   5 - ADC CH2 Local
   6 - ADC CH3 Local
   7 - ADC CH4 Local
   8 - GPIO CH1 Cloud
   9 - GPIO CH2 Cloud
   10 - GPIO CH3 Cloud
   11 - GPIO CH4 Cloud
   12 - GPIO CH1 Local
   13 - GPIO CH2 Local
   14 - GPIO CH3 Local
   15 - GPIO CH4 Local
   16 - Relay CH1 Cloud
   17 - Relay CH2 Cloud
   18 - MOSFET CH1 Cloud
   19 - MOSFET CH2 Cloud
   20 - Relay CH1 Local
   21 - Relay CH2 Local
   22 - MOSFET CH1 Local
   23 - MOSFET CH2 Local
   24 - Digital Input Monitor DI-A Local
   25 - Digital Input Monitor DI-B Local
   26 - Digital Output Monitor DO-A Local
   27 - Digital Output Monitor DO-B Local
   28 - Counter CH1
   29 - Counter CH2
   30 - Counter CH3
   31 - Counter CH4
   32 - Counter CH5
   33 - Counter CH6
   34 - Internal Access Register Address
   35 - Internal Access Register Info.
*/

String Data;
String dataArray[35];

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    Data = Serial.readStringUntil('\n');
    Serial.println(Data);


    for (int count = 0; count <= 35; count++) {
      Data = Serial.readStringUntil(',');
      dataArray[count] = Data;
    }

    Data = "";
  }

  Serial.println(dataArray[35]);
}
