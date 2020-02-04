MIN_DRIVE_AGE = 16
NAME = input("What is your name? ")
AGE = int(input("How old are you? "))

if AGE > MIN_DRIVE_AGE :
    print(f"{NAME} is not allowed to drive")

else:
    print(f"{NAME} is allowed to drive")
