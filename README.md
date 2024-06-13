# Tarea 1: Patrón Singleton - Administrador de Settings de un Videojuego

## Instrucciones
Implementa una clase Singleton `SettingsManager` en Python. La clase debe asegurar que solo se cree una instancia de `SettingsManager`. Este `SettingsManager` gestionará configuraciones del juego como volumen, brillo y dificultad.

1. Completa la metaclase `SingletonMeta` implementando el patrón Singleton en el método `__call__`.
2. Asegúrate de que la clase `SettingsManager` use `SingletonMeta` como su metaclase.
3. La clase `SettingsManager` debe tener los siguientes métodos:
   - `set_setting(key, value)`: Establece el valor para la clave de configuración dada.
   - `get_setting(key)`: Devuelve el valor para la clave de configuración dada.

## Setup inicial
- Crea un entorno virtual
~~~bash
python3 -m venv .venv
~~~
o
~~~bash
python -m venv .venv
~~~
- Activa el entorno:
~~~bash
source .venv/bin/activate
~~~
- Instala dependencias:
~~~bash
pip install -r requirements.txt
~~~

## Entrega
- Implementa tu solución en `src/singleton.py`.
- Asegúrate de que todas las pruebas en `tests/test_singleton.py` pasen.
Las pruebas las ejecutas así:
~~~bash
pytest
~~~
- Al terminar, deberás hacer commit y subir tus cambios al repositorio

## Criterios de Evaluación
- Implementación correcta del patrón Singleton.
- Pasar todas las pruebas automatizadas.

