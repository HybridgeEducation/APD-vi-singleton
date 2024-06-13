class SingletonMeta(type):
    """
    Metaclass for Singleton. Ensure only one instance of the Singleton class is created.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # TODO: Implement the Singleton pattern
        pass

class SettingsManager(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {
            "volume": 50,
            "brightness": 70,
            "difficulty": "normal"
        }

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key)