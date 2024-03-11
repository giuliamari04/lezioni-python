# if statement = a block of code that will execute if it's a condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are very old, man!")
elif age >=18:
    print("You are an adult")
elif age < 0:
    print("Something is wrong with you")
else:
    print("Stay away! you are a minor!")
