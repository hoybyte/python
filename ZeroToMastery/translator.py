#TODO Request file location input from user
#TODO Read inputted File Location
#TODO Translate to language
#TODO Determine which langaguge user wants

from pathlib import Path

file_path = Path(input("What file do you want translated?"))

language = input(f"What language do you want the file, {file_path}, to be translated to:  ")

print(file_path)
print(language)