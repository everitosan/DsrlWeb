# Python
from subprocess import check_output
import os
# Gphoto2
from App.Utils.Gphoto2.routes import routes
from App.Utils.Gphoto2.decorators import config


def transform_to_dict(settings: bytes):
    settings_dict = {}
    settings_string = settings.decode("utf-8")
    settings_list = settings_string.split("\n")
    for setting in settings_list:
        values = setting.split(": ")
        if len(values) >= 2:
            settings_dict[values[0]] = values[1]
    return settings_dict


def check_installed():
    res = check_output(["gphoto2", "-v"])
    return "Copyright" in res.decode("utf-8")


@config
def set_config(*args, **kwargs):
    val = kwargs.get("val")
    os.system("gphoto2 --set-config {}={}", get_config_dir(key), val)


@config
def get_config(*args, **kwargs):
    route = args[0]
    key = kwargs.get('key')
    conf = check_output(["gphoto2", "--get-config", route])
    settings = transform_to_dict(conf)
    return {
        key: settings.get("Current")
    }
