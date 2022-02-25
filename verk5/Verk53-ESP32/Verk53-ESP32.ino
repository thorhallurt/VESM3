#include <EspMQTTClient.h>
#include <BH1750.h>
#include <Wire.h>
#include <ArduinoJson.h>

BH1750 lightMeter;

EspMQTTClient client(
  "Taekniskolinn",
  "",
  "test.mosquitto.org",
  "",
  "",
  "thorhallurt");

void setup() {

  Serial.begin(115200);
  Wire.begin();
  lightMeter.begin();
  Serial.println(F("BH1750 Test"));

}

void onConnectionEstablished() {

  Serial.println("Conneciton established!");
  
}

void loop() {

  float lux = lightMeter.readLightLevel();
  Serial.print("Light: ");
  Serial.println(lux);
  delay(1000);

}
