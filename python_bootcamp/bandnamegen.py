# Band Name Generator
#1: Greet
print("Hello and welcome to the Band Name Generator. \n" + "Let's get started!\n")
name = input("Would you like a cool name or an 'meh' name? Type 1 for cool and 2 for meh. \n")
if name == '1':
    first = input ("Enter your favorite word: \n")
    second = input ("Enter your favorite time of day: \n")
    third = input ("Lastly, enter your favorite mythical creature: \n")
    print("Your band name is highly reccomended to be: ", first, second, third, ".")
elif name == '2':
    uno = input ("Enter your favorite city: \n")
    dos = input ("Enter your favorite animal or your pet's name: \n")
    print("Your band name might be: ", uno, dos, ".")
else:
    print("*Buzzer sound* Not accepted. Follow directions properly, loser.")
    
