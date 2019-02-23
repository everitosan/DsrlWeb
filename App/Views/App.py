"""
    This module is in  charge of keeping some parameters external to the camera as:
    SAVE_FILE flag
    TIMER
    TIMELAPSE
"""

from Utils.Response import json_api_response
from Utils.Gphoto2.actions import get_config


def get_app_config():
    """
    Returns the configuration of the
    """
    return {
        "should_save": False,
        "timmer": 0,
        "timelapse": {
            "interval": 0,
            "timeout": 0
        },
    }

@json_api_response
def get_info():
    return {
        "version": "0.0.1",
        **get_config(key="iso"),
        **get_config(key="shutterspeed"),
        **get_config(key="aperture"),
        **get_config(key="batterylevel"),
        **get_app_config()
    }
