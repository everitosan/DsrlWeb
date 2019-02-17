# Python
import unittest
# Modules
from App.Utils.Gphoto2 import actions


class TestActions(unittest.TestCase):
    def __test_get_config(self, key):
        parameter = actions.get_config(key=key)
        self.assertIsInstance(parameter, dict)
        self.assertIsNotNone(parameter.get(key))

    def test_iso(self):
        self.__test_get_config("iso")

    def test_shutterspeed(self):
        self.__test_get_config("shutterspeed")

    def test_aperture(self):
        self.__test_get_config("aperture")
