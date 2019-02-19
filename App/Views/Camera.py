# Flask
from flask import request

# Utils
from Utils.Response import json_api_response
from Utils.Gphoto2.actions import get_config, set_config


@json_api_response
def get_camera_info():
    return {
        **get_config(key="iso"),
        **get_config(key="shutterspeed"),
        **get_config(key="aperture"),
        **get_config(key="batterylevel"),
    }


@json_api_response
def set():
    body = request.get_json()
    parameter = body.get("parameter")
    value = body.get("value")
    if parameter and value:
        res = set_config(key=parameter, val=value)
    else:
        res = { "error": "Check parameters" }
    return res

@json_api_response
def set_parameter(parameter: str, value: int):
    res = set_config(key=parameter, val=value)
    return res
