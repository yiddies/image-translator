from functions import get_image_text, convert_language_input, translate_text
while True:
    try:
        img = input("Enter image: (Exit to exit) " ).strip().lower()
        #print(img_text)
        if img == 'exit':
            break
        else:
            img_text = get_image_text(img).strip()
            translate_lang = input("What language do you want to translate to? (e.g., Spanish): ")
            dest_lang = convert_language_input(translate_lang)
            
            if dest_lang is None:
                print("Invalid language input")
                continue
            
            translated_text = translate_text(img_text, dest_lang)
            print("\n" + translated_text + "\n")
        
    except (FileNotFoundError, AttributeError):
        print('File was not found')

        
