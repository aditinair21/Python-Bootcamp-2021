#Password Generator
import random
print ("Welcome to the Password Generator. \n")
nr_hiletters = int(input ("How many lowercase letters do you want in your password? \n"))
nr_lowletters = int(input ("How many uppercase letters do you want in your password? \n"))
nr_numbers = int(input ("How many numbers do you want in your password? \n"))
nr_symbols = int(input ("How many symbols do you want in your password? \n"))
lowletters = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
hiletters = ["A", "B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=']
password= ""
for int in range (1, nr_hiletters + 1):
    password += random.choice (hiletters)
for int in range (1, nr_lowletters + 1):
    password += random.choice (lowletters)
for int in range (1, nr_numbers + 1):
    password += random.choice (numbers)
for int in range (1, nr_symbols + 1):
    password += random.choice (symbols)
#print (password)
#parts = [f_password, s_password, t_password, r_password]
p = list(password)
#print(p)
random.shuffle(p)
a = ''.join(p)
print ("Your password is", a)
    


