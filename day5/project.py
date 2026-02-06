import random as rd
uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '\\', '|', '`', '~']


print("Welocome to Password generator")
nr_letters= int(input("no letters in the password"))
nr_symbols = int(input("no symbols in the password"))
nr_numbers = int(input("number of numbers"))

password = []

for chr in range(1,nr_letters+1):
    password.append(rd.choice(uppercase_alphabet))
    #print(password)
for chr in range(1,nr_symbols+1):
    password.append(rd.choice(numbers ))
    #print(password)
for chr in range(1,nr_numbers+1):
    password.append(rd.choice(special_characters))
    #print(password)
print(password)
#shuffle the password
rd.shuffle(password)
print(password)
p_str =""
for i in password:
    p_str +=i
print(p_str)
