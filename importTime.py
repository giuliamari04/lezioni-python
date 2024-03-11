import time

# for loop = a statement that will execute it's block of code a limited amount of times
#           while loop = unlimited
#           for loop = limited

for i in range(10):
    print(i)
# 123456789

for i in range(10):
    print(i+1)  
# 12345678910
    
for i in range(50,100+1):
    print(i)
#numeri da 50 a 100
    
for i in range(50,100+1,2):
    print(i)
#numeri da 50 a 100 ogni 2 numeri
    
for i in "Bro Code":
    print(i)

# code coutdown
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) # fa in modo che passi un secondo tra ogni iterazione
print("Happy New Year!")