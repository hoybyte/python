def checkDriverAge(age=0):
    age = (input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering Off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()