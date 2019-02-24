"""
    This module is responsible of getting the routes based on the gphoto2 library
"""
from subprocess import check_output, CalledProcessError
import sys


def get_routes():
    try:
        config = check_output(["gphoto2", "--list-config"])
        return config.decode("utf-8").split("\n")
    except CalledProcessError:
        sys.exit(0)


routes = get_routes()


def get_route_for(key):
    try:
        return next(route for route in routes if key in route)
    except StopIteration:
        return None
