//CANSAT SD Card Read/Write
#include <SPI.h>
#include <SD.h>

//Variables for SD (Copy these in new code)
const int CHIP_SELECT = 4; //TODO: Change this based on CANSAT Schematic
const String DATA_FILE = "data.txt";

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
}

void loop() {


}


//TODO: Call this in setup, with CHIP_SELECT argument
bool initializeSD(int CS){
  return SD.begin(CS);
}

//write to SD Card
//TODO: Can be called anywhere in loop(), Arguments: DATA_FILE, DATA
//Saves only int data, as CANSAT saves STATE as int
bool writeSD(String file_name, int data){

  File data_file = SD.open(file_name, FILE_WRITE);
  if(data_file){
    data_file.println(data);
    data_file.close();
    return true;
  }

  return false;
}

//Note: This might not be need for CANSAT, but can be used for testing!
void readSD(String file_name){

  int data = -144; //-144 signifies no value read. Can be used as a flag in CANSAT

  File data_file = SD.open(file_name);
  if (data_file) {
    while (data_file.available()) {
      Serial.write(data_file.read());
    }
    data_file.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening file!");
  }
}
