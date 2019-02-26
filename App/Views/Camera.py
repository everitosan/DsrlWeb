"""
    This module is in charge of the configuration of the camera
"""
# Flask
from flask import request

# Utils
from Utils.Response import json_api_response
from Utils.Gphoto2.actions import (
    get_options, get_config, set_config as set_cli_config)


@json_api_response
def get_camera_info():
    """
    Parameters returned for /config endpoint
    """
    return {
        **get_config(key="iso"),
        **get_config(key="shutterspeed"),
        **get_config(key="aperture"),
        **get_config(key="batterylevel"),
    }


@json_api_response
def set_config():
    """
    Take the config passed over the body of the request and call the cli helper
    with those params
    """
    body = request.get_json()
    parameter = body.get("parameter")
    value = body.get("value")
    if parameter and value:
        res = set_cli_config(key=parameter, val=value)
    else:
        res = {"error": "Check parameters"}
    return res


@json_api_response
def get_available_options(parameter: str):
    """
    Get available options of the camera for parameters like:
    - iso
    - shutterspeed
    - aperture
    """
    return {
        "options": get_options(key=parameter)
    }
