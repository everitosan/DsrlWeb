import os, subprocess
from flask import Flask

app=Flask(__name__)
SETTINGS_LIST = []
CONFIG_DIRS = {}

def getSettingDirection(setting_name):
	for line in SETTINGS_LIST:
		if setting_name in line:
			return line

@app.route("/")
def home():
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

		shutter_speed = os.popen("gphoto2 --get-config="+CONFIG_DIRS['shutterspeed']).read()
		iso = os.popen("gphoto2 --get-config="+CONFIG_DIRS['iso']).read()
		aperture = os.popen("gphoto2 --get-config="+CONFIG_DIRS['aperture']).read()

		return "Current settings: \n %s \n %s \n %s"%(shutter_speed, iso, aperture)

	except ValueError:
		return ValueError
	except:
		return "No camera detected"

@app.route("/trigger/<aperture>/<iso>")
def trigger(aperture, iso):
	os.system("gphoto2 --set-config /main/imgsettings/iso="+iso)
	os.system("")
	return "Photo taken with: AP:%s -  ISO:%s "% (aperture, iso)

if __name__ == "main":
	app.run()
