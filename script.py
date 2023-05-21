from PIL import Image
import pytesseract
from googletrans import Translator
import googletrans

def get_image_text(img):
    # Get image text
    img_text = pytesseract.image_to_string(Image.open(img))
    return img_text

def translate_text(text, dest):
    # Translate the image text to dest lang
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text

def convert_language_input(language):
    # Get the ISO code for the given language
    iso_code = None
    for lang in googletrans.LANGUAGES:
        if googletrans.LANGUAGES[lang].lower() == language.lower():
            iso_code = lang
            break
    return iso_code

while True:
    try:
        img = input("Enter image: ").strip()
        img_text = get_image_text(img).strip()
        #print(img_text)
        
        translate_lang = input("What language do you want to translate to? (e.g., Spanish): ")
        dest_lang = convert_language_input(translate_lang)
        
        if dest_lang is None:
            print("Invalid language input")
            continue
        
        translated_text = translate_text(img_text, dest_lang)
        print("\n" + translated_text + "\n")
        
    except (FileNotFoundError, AttributeError):
        print('File was not found')

        
