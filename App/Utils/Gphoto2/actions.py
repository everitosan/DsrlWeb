"""
    This module is in charge of communictign with the camera with the
    help of Gphoto2
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
            if values[0] == "Choice":
                if settings_dict.get("Choices") is None:
                    settings_dict["Choices"] = []
                settings_dict["Choices"].append({
                    "option": values[1].split(" ")[1]
                })
            else:
                settings_dict[values[0]] = values[1]
    return settings_dict


def __retrive_config__(route):
    conf = check_output(["gphoto2", "--get-config", route])
    return transform_to_dict(conf)


@uncertainty_Gphoto2
def check_installed():
    """
    Chek if gphoto2 is installed
    """
    res = check_output(["gphoto2", "-v"])
    return "Copyright" in res.decode("utf-8")


@config
def set_config(route, *args, **kwargs):
    """
    Set configuration of a specified parameter
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
    Retrives the value of a specified parameter
    """
    key = kwargs.get('key')
    settings = __retrive_config__(route)
    return {
        key: settings.get("Current")
    }


@config
def get_options(route, *args, **kwargs):
    """
    Retrives the options available for a parameter of the camera
    """
    kwargs.get('key')
    settings = __retrive_config__(route)
    return settings.get("Choices")


def trigger():
    """
    Send command to trigger the camera
    """
    os.system("gphoto2 --capture-image")
    return {"status": "ok"}
