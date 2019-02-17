# Python
import json
from contextlib import wraps


def json_api_response(fn):
    @wraps(fn)
    def wrapper(*args, **kwarg):
        res = fn(*args, **kwarg)
        return json.dumps(res)
    return wrapper
