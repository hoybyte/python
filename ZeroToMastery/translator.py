#TODO Read inputted File Location
#TODO Translate to language
#TODO Determine which langaguge user wants

from pathlib import Path
from translate import Translator

translator = Translator(to_lang='es')
file_path = ((input(r"What file do you want translated?")))
test_path = r'C:\Github\test.txt'
language = input(f"What language do you want the file, {file_path}, to be translated to:  ")


print(file_path)
print(language)

f = open(r"C:\Github\test.txt")
content = f.read()
print(content)
f.close()


translation = translator.translate("This is my Name")
print(translation)