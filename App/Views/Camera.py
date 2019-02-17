from Utils.Response import json_api_response
from Utils.Gphoto2.actons import get_config


@json_api_response
def get_camera_info():
    get_config(key="iso")
    return {
        "iso": 800,
        "shutter_speed": "1/100",
        "aperture": "1.2f"
    }


@json_api_response
def set_iso(iso: int):
    return {
        "iso": iso
    }
