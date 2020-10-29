import datetime
now = datetime.datetime.now()
birth_year = input("When were you born? ")
current_year = now.year
age = int(current_year) - int(birth_year)

print(f"You are {age} years old")
