import unittest
from src.singleton import SettingsManager

class TestSettingsManagerSingleton(unittest.TestCase):

    def setUp(self):
        # Reset the singleton instance before each test
        print(f"Resetting SettingsManager._instance: {SettingsManager._instance}")
        SettingsManager._instance = None
        print(f"SettingsManager._instance after reset: {SettingsManager._instance}")

    def test_singleton_instance(self):
        settings1 = SettingsManager()
        settings2 = SettingsManager()
        self.assertIs(settings1, settings2, "SettingsManager instances are not the same")

    def test_singleton_behavior(self):
        settings1 = SettingsManager()
        settings1.set_setting("volume", 75)
        settings2 = SettingsManager()
        print(f"Volume setting in settings2: {settings2.get_setting('volume')}")
        self.assertEqual(settings2.get_setting("volume"), 75, "Singleton instance does not share the same state")

    def test_default_settings(self):
        settings = SettingsManager()
        print(f"Default volume setting: {settings.get_setting('volume')}")
        print(f"Default brightness setting: {settings.get_setting('brightness')}")
        print(f"Default difficulty setting: {settings.get_setting('difficulty')}")
        self.assertEqual(settings.get_setting("volume"), 50)
        self.assertEqual(settings.get_setting("brightness"), 70)
        self.assertEqual(settings.get_setting("difficulty"), "normal")

if __name__ == '__main__':
    unittest.main()
