# DSLR WEB

Backend build with python and flask to receive settings of a dsrl camera in manual mode.

The configurable settings are:
 - ISO
 - Aperture
 - Shutter Speed

## Installation
The requirements ares listed at requirements.txt but basically needs python 3.6, Flask and gphoto2 to work.
### Important
**The server needs to have installed gphoto2 cli.**

## Endpoints

[GET] -> **api/v1/config**   
*Gets the info of the camera, it's current settings and options*

[POST] -> **api/v1/set**  
{
  "parameter": "iso",
  "value": "800"
}
*Sets a parameter to a value of the camera*

## Usage
To start the web server you may use init.sh script
