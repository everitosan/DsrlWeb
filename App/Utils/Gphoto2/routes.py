"""
    This module is responsible of getting the routes based on the gphoto2 library
"""
from subprocess import check_output


def get_routes():
    config = check_output(["gphoto2", "--list-config"])
    return config.decode("utf-8").split("\n")


routes = get_routes()


def get_route_for(key):
    try:
        return next(route for route in routes if key in route)
    except StopIteration:
        return None
