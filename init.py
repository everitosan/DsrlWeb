import os, subprocess, time
from flask import Flask

app=Flask(__name__)
SETTINGS_LIST = []
CONFIG_DIRS = {}
CONFIG_STATE = {'capturetarget': '1', 'download': False}

def getSettingDirection(setting_name):
	for line in SETTINGS_LIST:
		if setting_name in line:
			return line

def getConfig():
	try:
		global SETTINGS_LIST
		global CONFIG_DIRS
		#get directions of configurations
		list__config = subprocess.check_output(["gphoto2", "--list-config"])

		#split them in a list for later searchs
		SETTINGS_LIST = list__config.split("\n")

		#get the directions and save them on the config_dir dict
		CONFIG_DIRS['shutterspeed'] = getSettingDirection("shutterspeed")
		CONFIG_DIRS['iso'] = getSettingDirection("iso")
		CONFIG_DIRS['aperture'] = getSettingDirection("aperture")
		print("[*]Config values readen succesfully ...")
	except ValueError:
		return ValueError
	except:
		return "No camera detected"

@app.route("/")
def home():
	try:
		# get the current configuration of the camera
		getConfig()
		shutter_speed = os.popen("gphoto2 --get-config="+CONFIG_DIRS['shutterspeed']).read()
		iso = os.popen("gphoto2 --get-config="+CONFIG_DIRS['iso']).read()
		aperture = os.popen("gphoto2 --get-config="+CONFIG_DIRS['aperture']).read()

		return "Current settings: \n %s \n %s \n %s"%(shutter_speed, iso, aperture)

	except ValueError:
		return ValueError
	except:
		return "No camera detected"

@app.route("/trigger/<shutterspeed>/<iso>/<aperture>", methods=['POST',])
def trigger(shutterspeed,iso,aperture):
	#Validates if the config has already been read
	if len(CONFIG_DIRS) == 0:
		getConfig()

	#set the parameters
	os.system("gphoto2 --set-config  capturetarget="+CONFIG_STATE['capturetarget'])
	os.system("gphoto2 --set-config "+CONFIG_DIRS['shutterspeed']+"="+shutterspeed)
	os.system("gphoto2 --set-config "+CONFIG_DIRS['iso']+"="+iso)
	os.system("gphoto2 --set-config "+CONFIG_DIRS['aperture']+"="+aperture)

	#triggers the camera
	if CONFIG_STATE['download']:
		os.system("gphoto2 --capture-image-and-download --filename "+time.strftime("%H:%M:%S")+".cr2")
	else:
		os.system("gphoto2 --capture-image")

	return "Photo taken with: AP:%s -  ISO:%s "% (aperture, iso)

if __name__ == "main":
	app.run()
