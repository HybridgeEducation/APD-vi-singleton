import unittest
from src.singleton import SettingsManager, SingletonMeta

class TestSettingsManagerSingleton(unittest.TestCase):

    def setUp(self):
        # Resetea las instancias de la clase SingletonMeta en cada test
        SingletonMeta._instances = {}

    def test_singleton_instance(self):
        settings1 = SettingsManager()
        settings2 = SettingsManager()
        self.assertIs(settings1, settings2, "Las instancias de SettingsManager no son iguales")

    def test_singleton_behavior(self):
        settings1 = SettingsManager()
        settings1.set_setting("volumen", 75)
        settings2 = SettingsManager()
        self.assertEqual(settings2.get_setting("volumen"), 75, "Las instancias de SettingsManager no tienen el mismo estado")

    def test_default_settings(self):
        settings = SettingsManager()
        self.assertEqual(settings.get_setting("volumen"), 50)
        self.assertEqual(settings.get_setting("brillo"), 70)
        self.assertEqual(settings.get_setting("dificultad"), "normal")

if __name__ == '__main__':
    unittest.main()
