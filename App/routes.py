"""
    Routes of the Api
"""
from Views import App, Camera

API_VERSION = "/api/v1"


def __build__(base: str, path: str):
    return "{}{}".format(base, path)


def register_endpoints(app, base_api=None):
    """
        Defined routes
    """

    base = base_api if base_api is not None else API_VERSION

    app.add_url_rule(
        __build__(base, "/"),
        view_func=App.get_info
    )
    app.add_url_rule(
        __build__(base, "/config"),
        view_func=Camera.get_camera_info
    )
    app.add_url_rule(
        __build__(base, "/set"),
        view_func=Camera.set_config, methods=['PUT']
    )
    app.add_url_rule(
        __build__(base, "/options/<string:parameter>"),
        view_func=Camera.get_available_options
    )
