#TODO Read inputted File Location
#TODO Translate to language
#TODO Determine which langaguge user wants

from pathlib import Path
from translate import Translator

translator = Translator(to_lang='es')
file_path = Path(input("What file do you want translated?"))

language = input(f"What language do you want the file, {file_path}, to be translated to:  ")

print(file_path)
print(language)

# try:
#     with open(file_path, mode='r') as my_file:
#         print(my_file.readlines())
# except FileNotFoundError as err:
#     print('File does not exist')
#     raise

translation = translator.translate("This is my Name")
print(translation)