# DSLR WEB

Backend build with python and flask to receive settings of a dsrl camera in manual mode.

The configurable settings are:
 - ISO
 - Aperture
 - Shutter Speed

The server needs to have installed gphoto2 cli.

## Installation
The requirements ares listed at requirements.txt but basically needs python 2.7,  Flask and gphoto2 to work.

## Endpoints

[GET] -> **/**   
*Gets the info of the camera, it's current settings and options*

[POST] -> **/trigger/:shutterspeed/:iso/:aperture**  
*Triggers the camera with the included parameters*

## Usage
To start the web server you may use init.sh script
