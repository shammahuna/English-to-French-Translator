from deep_translator import GoogleTranslator

def translate_text():
    text = input("Enter text to translate: ")
    print("\n1. English to French\n2. French to English")
    choice = input("Choice: ")
    
    if choice == "1":
        result = GoogleTranslator(source='en', target='fr').translate(text)
        print(f"Translation: {result}")
    elif choice == "2":
        result = GoogleTranslator(source='fr', target='en').translate(text)
        print(f"Translation: {result}")
    else:
        print("Invalid choice")

while True:
    print("\n=== English-French Translator ===")
    print("1. Translate\n2. Exit")
    choice = input("Choice: ")
    
    if choice == "1":
        translate_text()
    elif choice == "2":
        break
