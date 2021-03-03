#include<WiFi.h>
#include<FirebaseESP32.h>

#define NETWORK_SSID "Brother Laser Printer"
#define NETWORK_PASSWORD "11223344"

#define FIREBASE_HOST "https://data-acquisition-eb65d-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "dAXwu39ZmHoLEUzgM7KkNm6dtyW0HiITqUHOCvb5"

FirebaseData firebase;

String key = "/ADC";
bool repeat = true;

void setup()
{
  Serial.begin(115200);
  Serial.println();

  WiFi.begin(NETWORK_SSID, NETWORK_PASSWORD);
  Serial.print("WIFI CONNECTED");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
}
void loop()
{
  while (repeat) {
    Firebase.getInt(firebase, key + "/channel4/data");
    Serial.println(firebase.intData());
    
    repeat = false;
    Firebase.end(firebase);
  }


}
