from Views import App, Camera


def register_endpoints(app, base_api: str = "/api/v1"):
    app.add_url_rule("{}{}".format(base_api, "/"), view_func=App.get_info)
    app.add_url_rule("{}{}".format(base_api, "/config"), view_func=Camera.get_camera_info)
    app.add_url_rule("{}{}".format(base_api, "/set/iso/<int:iso>"), view_func=Camera.set_iso)
