# Python
import os
import subprocess
import time
# Flask
from flask import Flask

app = Flask(__name__)
SETTINGS_LIST = []
CONFIG_DIRS = {}
CONFIG_STATE = {'download': False}


def getSettingDirection(setting_name):
    for line in SETTINGS_LIST:
        if setting_name in line:
            return line


def getConfig():
    try:
        global SETTINGS_LIST
        global CONFIG_DIRS

        # get directions of configurations
        list__config = subprocess.check_output(["gphoto2", "--list-config"])
        print(list__config)

        # split them in a list for later searchs
        SETTINGS_LIST = list__config.split("\n")

        # get the directions and save them on the config_dir dict
        CONFIG_DIRS['shutterspeed'] = getSettingDirection("shutterspeed")
        CONFIG_DIRS['iso'] = getSettingDirection("iso")
        CONFIG_DIRS['aperture'] = getSettingDirection("aperture")
        CONFIG_DIRS['capturetarget'] = getSettingDirection("capturetarget")

        print("[*]Config values readen succesfully ...")
    except ValueError:
            return ValueError
    except:
        return "No camera detected"


def setCameraParameter(name, value):
    os.system("gphoto2 --set-config "+CONFIG_DIRS[name]+"="+value)


def triggerCamera():
    # triggers the camera
    if CONFIG_STATE['download']:
        os.system(
            "gphoto2 --capture-image-and-download --filename "+time.strftime("%H:%M:%S")+".cr2"
        )
    else:
        os.system("gphoto2 --capture-image")


@app.route("/")
def home():
    try:
        # get the current configuration of the camera
        getConfig()
        shutter_speed = os.popen("gphoto2 --get-config="+CONFIG_DIRS['shutterspeed']).read()
        iso = os.popen("gphoto2 --get-config="+CONFIG_DIRS['iso']).read()
        aperture = os.popen("gphoto2 --get-config="+CONFIG_DIRS['aperture']).read()

        return "Current settings: \n %s \n %s \n %s" % (shutter_speed, iso, aperture)

    except ValueError:
        return ValueError
    except:
        return "No camera detected"


@app.route("/trigger/<shutterspeed>/<iso>/<aperture>", methods=['POST', ])
def trigger(shutterspeed, iso, aperture):
    # Validates if the config has already been read
    if len(CONFIG_DIRS) == 0:
        getConfig()

    # set the parameters
    setCameraParameter('shutterspeed', shutterspeed)
    setCameraParameter('iso', iso)
    setCameraParameter('aperture', aperture)

    triggerCamera()
    return "Photo taken with: AP:%s -  ISO:%s " % (aperture, iso)


@app.route("/save_on_sd/<flag>", methods=['POST', ])
def save_on_sd(flag):
    setCameraParameter('capturetarget', flag)
    return "Save on sd card: %s" % flag


@app.route("/download_image/<int:flag>", methods=['POST', ])
def download_image(flag):
    global CONFIG_STATE

    if flag != 0 and flag != 1:
        return "Can't assign download to other value rather than 0 or 1"
    else:
        CONFIG_STATE['download'] = bool(flag)
    return "Download setted to %d" % flag


@app.route("/trigger_iso/<iso>", methods=['POST', ])
def trigger_iso(iso):
    # Validates if the config has already been read
    if len(CONFIG_DIRS) == 0:
        getConfig()

    os.system("gphoto2 --set-config "+CONFIG_DIRS['iso']+"="+iso)
    triggerCamera()
    return "Photo taken"


if __name__ == "main":
    app.run()
