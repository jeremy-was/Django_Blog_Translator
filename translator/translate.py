from gettext import translation
from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='lt')
    return translation.text