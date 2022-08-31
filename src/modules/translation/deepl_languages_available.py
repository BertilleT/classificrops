#print languages available with deepl API
import deepl
#word = input("Please enter a word to translate:\n")
#lang = input("Please enter a language target:\n")

DEEPL_AUTH_KEY="47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
translator = deepl.Translator(DEEPL_AUTH_KEY)
#result = translator.translate_text(word, target_lang=lang
#print(result)


print("Source languages:")
for language in translator.get_source_languages():
    print(f"{language.name} ({language.code})")  # Example: "German (DE)"

print("\n\n")
print("Target languages:")
for language in translator.get_target_languages():
    if language.supports_formality:
        print(f"{language.name} ({language.code}) supports formality")
        # Example: "Italian (IT) supports formality"
    else:
        print(f"{language.name} ({language.code})")
        # Example: "Lithuanian (LT)"