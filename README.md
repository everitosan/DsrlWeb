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
[GET] -> **/api/v1/**   
*Gets the main info of the server.*


[GET] -> **/api/v1/config**   
*Gets the current settings of the camera*
```
{
  "iso": "800",
  "shutterspeed": "1/100",
  "aperture": "1.8"
}
```

[GET] -> **/api/v1/options/[iso | shutterspeed | aperture]**   
*Gets the available options for a specific parameter*
```
{
  "options": [
    {
      "option": "100"
    }, {
      "option": "200"
    }, {
      "option": "400"
    }
  ]
}
```

[PUT] -> **/api/v1/set/**  
*Updates a parameter to a value of the camera*
```
{
  "parameter": "iso",
  "value": "800"
}
```

[POST] -> **/api/v1/trigger/**  
*Triggers the camera*
```
{
  "status": "ok"
}
```

## Usage
To start the web server.
```ssh
$ (env) python App
```
