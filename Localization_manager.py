import json

class Localization:
    def __init__(self, lang="es"):
        # Cargar las traducciones desde el archivo JSON
        with open("texts.json", "r") as file:
            self.texts = json.load(file)
        self.current_language = lang

    def set_language(self, lang):
        # Cambiar el idioma actual
        if lang in self.texts:
            self.current_language = lang

    def get_text(self, key):
        # Obtener el texto en el idioma actual, con clave de respaldo si no existe la traducción
        return self.texts.get(self.current_language, {}).get(key, key)

# Crear una instancia global para que otros módulos puedan acceder fácilmente
localization = Localization()