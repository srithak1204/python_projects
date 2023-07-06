import random
print("Welcome to password generator!")
nof_letters=int(input("How many letters would you like in your password? "))
nof_numbers=int(input("How many numbers would you like? "))
nof_symbols=int(input("How many symbols would you like? "))
password=[]

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')',',','.','/','+','|',';',':','[',']','{','}']

for i in range(nof_letters):
    a= random.choice(letter)
    password.append(a)

for j in range(nof_numbers):
    b=random.choice(number)
    password.append(b)

for k in range(nof_symbols):
    c=random.choice(symbol)
    password.append(c)

# print(*password,sep= '',end='\n')
random.shuffle(password)
print(*password,sep= '',end='')