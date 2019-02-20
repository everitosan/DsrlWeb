# Python
import unittest
# Modules
from App.Utils.Gphoto2 import routes


class TestRoutes(unittest.TestCase):
    def test_get_route_for(self):
        iso_route = routes.get_route_for("iso")
        self.assertIsInstance(iso_route, str)
