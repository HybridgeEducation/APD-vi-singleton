# Assignment 1: Singleton Pattern - Game Settings Manager

## Instructions
Implement a Singleton SettingsManager class in Python. The class should ensure that only one instance of the SettingsManager is created. This SettingsManager will manage game settings like volume, brightness, and difficulty.

1. Complete the `SingletonMeta` metaclass by implementing the Singleton pattern in the `__call__` method.
2. Ensure the `SettingsManager` class uses `SingletonMeta` as its metaclass.
3. The `SettingsManager` class should have the following methods:
   - `set_setting(key, value)`: Sets the value for the given setting key.
   - `get_setting(key)`: Returns the value for the given setting key.

## Submission
- Implement your solution in `src/singleton.py`.
- Ensure all tests in `tests/test_singleton.py` pass.

## Grading Criteria
- Correct implementation of the Singleton pattern.
- Passing all automated tests.
