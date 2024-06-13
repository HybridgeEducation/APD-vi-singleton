import unittest
from src.singleton import SettingsManager

class TestSettingsManagerSingleton(unittest.TestCase):
    def setUp(self):
        # Reset the singleton instance before each test
        SettingsManager._instance = None
        
    def test_singleton_instance(self):
        settings1 = SettingsManager()
        settings2 = SettingsManager()
        self.assertIs(settings1, settings2, "SettingsManager instances are not the same")

    def test_singleton_behavior(self):
        settings1 = SettingsManager()
        settings1.set_setting("volume", 75)
        settings2 = SettingsManager()
        self.assertEqual(settings2.get_setting("volume"), 75, "Singleton instance does not share the same state")

    def test_default_settings(self):
        settings = SettingsManager()
        self.assertEqual(settings.get_setting("volume"), 50)
        self.assertEqual(settings.get_setting("brightness"), 70)
        self.assertEqual(settings.get_setting("difficulty"), "normal")

if __name__ == '__main__':
    unittest.main()
