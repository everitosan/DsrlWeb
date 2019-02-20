# Python
import json
from contextlib import wraps
# Flask
from flask import Response


def json_api_response(fn):
    @wraps(fn)
    def wrapper(*args, **kwarg):
        res = fn(*args, **kwarg)
        return Response(
            json.dumps(res),
            status=200,
            mimetype="application/json"
        )
    return wrapper
