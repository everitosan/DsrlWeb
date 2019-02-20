"""
    Routes of the Api
"""
from Views import App, Camera


def register_endpoints(app, base_api: str = "/api/v1"):
    """
        Defined routes
    """
    app.add_url_rule("{}{}".format(base_api, "/"), view_func=App.get_info)
    app.add_url_rule("{}{}".format(base_api, "/config"), view_func=Camera.get_camera_info)
    app.add_url_rule("{}{}".format(base_api, "/set"), view_func=Camera.set, methods=['POST'])
