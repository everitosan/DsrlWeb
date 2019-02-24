# Python
import unittest
# Modules
from App.Utils.Gphoto2 import actions


class TestActions(unittest.TestCase):
    def __test_get_config__(self, key):
        parameter = actions.get_config(key=key)
        self.assertIsInstance(parameter, dict)
        self.assertIsNotNone(parameter.get(key))

    def __test_get_options__(self, key):
        options = actions.get_options(key=key)
        self.assertIsNotNone(options)
        self.assertIsInstance(options, list)

    def test_iso(self):
        self.__test_get_config__("iso")

    def test_shutterspeed(self):
        self.__test_get_config__("shutterspeed")

    def test_aperture(self):
        self.__test_get_config__("aperture")

    def test_get_options_aperture(self):
        self.__test_get_options__("aperture")

    def test_get_options_aperture(self):
        self.__test_get_options__("iso")

    def test_get_options_aperture(self):
        self.__test_get_options__("shutterspeed")
