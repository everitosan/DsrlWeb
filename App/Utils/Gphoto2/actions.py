"""
This module is in charge of communictign with the camera with the help of Gphoto2
"""

# Python
from subprocess import check_output
import os
# Gphoto2
from .decorators import config, uncertainty_Gphoto2


def transform_to_dict(settings: bytes):
    settings_dict = {}
    settings_string = settings.decode("utf-8")
    settings_list = settings_string.split("\n")
    for setting in settings_list:
        values = setting.split(": ")
        if len(values) >= 2:
            settings_dict[values[0]] = values[1]
    return settings_dict


@uncertainty_Gphoto2
def check_installed():
    """
    chek if gphoto2 is installed
    """
    res = check_output(["gphoto2", "-v"])
    return "Copyright" in res.decode("utf-8")


@config
def set_config(route, *args, **kwargs):
    """
    set configuration of a specified parameter
    """
    val = kwargs.get("val")
    key = kwargs.get('key')
    set_cmd = "{}={}".format(route, val)
    os.system("gphoto2 --set-config {}".format(set_cmd))
    return {
        key: val
    }


@config
def get_config(route, *args, **kwargs):
    """
    retrives the value of a specified parametr
    """
    key = kwargs.get('key')
    conf = check_output(["gphoto2", "--get-config", route])
    settings = transform_to_dict(conf)
    return {
        key: settings.get("Current")
    }
