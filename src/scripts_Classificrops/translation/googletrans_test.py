from googletrans import Translator
translator = Translator()
test = translator.translate('fruita dolca', src='ca')
print(test.text)