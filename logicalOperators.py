#logical operators (and ,or,not) = used to check if two or more conditional statement is true
temp = int(input("Whats the temperature outside?: "))

if temp >=0 and temp <=30:
    print("It's chill bro")
    print("Go outside, don't play LOL")
elif temp < 0 or temp > 30:
    print("It's bad outside bro")
    print("Climate changhe,...")

# elif not(temp < 0 or temp > 30):
#     print("It's bad outside bro")
#     print("Climate changhe,...")