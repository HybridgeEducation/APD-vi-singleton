class SingletonMeta(type):
    """
    Metaclass para la clase Singleton. Esta clase se asegura de que exista una única instancia de la clase Singleton
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # TODO: Implementa el patrón Singleton
        pass

class SettingsManager(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {
            "volumen": 50,
            "brillo": 70,
            "dificultad": "normal"
        }

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)