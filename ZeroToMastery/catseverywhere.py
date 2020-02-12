class Cat:
    species = 'mammal' 
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_oldest_cat(*args):
    return max(args)

Cat1 = Cat('Cat1', 2)
Cat2 = Cat('Cat2', 3)
Cat3 = Cat('Cujo', 4)

print(Cat1)
print(Cat2)
print(Cat3)

print(f"The oldest cat is {get_oldest_cat(Cat1.age, Cat2.age, Cat3.age)} years old.")

# 1 Instantiate the Cat object with 3 cats


# 2 Create a function that cinds the oldest cat
 

# 3 Print out: "The Oldest cat is x years old." x will be the oldest cat age by 
# using the function in #2