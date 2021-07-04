# Take number input and print whether number is greater than 100 or not
# Tell person that number is not base ten
number = int(input("Enter a WHOLE number: "))
print ("Ok...")
while True:
    if number >= 100:
        print("Number greater than or equal to 100. Yay.")
    elif number < 100:
        print("Number less than 100. Bye.")
    else:
        print("You loser. Please follow directions.")
    
