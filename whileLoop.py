# while loop = a statement that will execute it's block of code, as long as it's condition remains true

# while 1==1:
#     name = print("Help! I'm stuck in a loop!")

name=""

while len(name)==0:
    name = input("Enter your name: ")

print("hello "+name)

name2= None

while not name2:
    name2 = input("Enter your name: ")

print("hello "+name2)