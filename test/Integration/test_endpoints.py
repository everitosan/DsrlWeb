"""
    Test the available endpoints of the api
"""
# Python
import unittest
import json
# Modules
from HttpPy.Request import make_request

URL = "http://127.0.0.1:5000/api/v1"


def get_config():
    get_config_req = {
        "type": "get",
        "url": "{}/config".format(URL),
        "verbose": True,
    }

    return make_request(get_config_req, False)


class TestEndpoints(unittest.TestCase):
    """
    Main class of the test
    """

    def __test_set_config(self, parameter, value):
        post_param_req = {
            "type": "put",
            "url": "{}/set".format(URL),
            "verbose": True,
            "body": {
                "parameter": parameter,
                "value": value
            }
        }

        make_request(post_param_req, False)
        confirm_res = get_config()
        body = json.loads(confirm_res.text)
        self.assertEqual(value, body.get(parameter))

    def test_get_config(self):
        """
        Test get the configuration of the camera
        """
        res = get_config()
        content_type = res.headers.get("Content-Type")
        body = json.loads(res.text)

        self.assertTrue("application/json" in content_type)
        self.assertIsNotNone(body.get("iso"))
        self.assertIsNotNone(body.get("shutterspeed"))
        self.assertIsNotNone(body.get("aperture"))
        self.assertIsNotNone(body.get("batterylevel"))

    def test_set_iso(self):
        """
        Test set a parameter in the camera
        """
        iso_value = "800"
        self.__test_set_config("iso", iso_value)
