# Python
from contextlib import wraps
# Gphoto2
from App.Utils.Gphoto2.routes import get_route_for


def config(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = kwargs.get('key')
        route = get_route_for(key)
        if route:
            res = fn(route, *args, **kwargs)
            return res
        else:
            print("Unknown setting {}".format(key))
    return wrapper
