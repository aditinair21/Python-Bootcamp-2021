# Treasure Island
print ("Welcome to Treasure Island. \n Your mission is to find the treasure before one of the pirates do. \n Hurry.")
first = input("You have three choices to reach the island. Take a boat, private jet, or swim. Type 1, 2, 3, respectively. ")
if first == "1":
    print ("Your boat is doing fine but midway across, the gas runs out. You are forced to swim but have to evade a lot of dangerous sharks. \n You reach the shore, tired, but fine.")
    print ("There is a cottage with warm, glowing windows that awaits you. But, it has been rumored to harbor a witch. \n There is a lighthouse as well, but a ghost has been said to haunt it.")
    a = input ("Choose one of the two. 1 for cottage and 2 for lighthouse. ")
elif first == "2":
    print ("Huzzah! You reach the island. But you're pretty much broke so you can't buy food or basically anything else.")
    a = input ("There is a cottage that you can stay at, but it might have a witch and requires money. A lighthouse is also present but is rumored to have a ghost. 1 for cottage 2 for lighthouse.")
elif first == "3":
    print ("You're feeling ok after your long swim since the person in the boat distracted the sharks.")
    a = input ("You can stay at a cottage that looks welcoming but might have a witch or a lighhouse that might have a ghost. 1 for cottage 2 for lighthouse.")
else:
    print("Tut, tut, tut. Should've chosen one of the three to have some fun.")
if a == "1":
    print ("Yay! You have a nice dinner and sleep well. The next morning you set off for treasure.")
    b=input ("Treasure might await you at a cove that might flood with the tide. It might also be buried in a mine. Choose 1 or 2 respectively.")
elif a == "2":
    print("Your sleep was cold and dreadful. In the middle of the night, while walking to the bathroom, you're ghost touched by the ghost and your hands are paralyzed.")
    b=input ("In the morning, treasure might await you at a cove, but the cove has some pretty high tides that can drown you. The treasure could be in a mine, but it's very claustrophobic and can collapse. 1 or 2 respectively.")
else:
    print ("WHY? If you'd chosen 1 or 2 this would've been much nicer.")
if b == "1":
    c = input("The cove floods with the water from high tide. Luckily, you find a trapdoor. You go through it and find 3 doors. Blue, 1, Green, 2, and Red, 3. Choose a door.")
elif b == "2":
    print ("In the mine, you are tired and scared. You tap on some stones and suddenly, there's an avalanche! Bruised but happy, you find a secret trapdoor!")
    c = input ("You go through and find three doors, Blue, 1, Green, 2, and Red, 3. Choose wisely.")
else:
    print ("WHY? If you'd chosen 1 or 2 this would've been much nicer.")
if c == "1":
    print("What does the blue door contain? NOTHING. You are sucked into a vacuum and are eliminated. Game over.")
elif c == "2":
    print ("What does the green door contain? I don't know and neither do you because you've gone mad from scorpion bites. Game over.")
elif c == "3":
    last = input ("Hmmm... The Red door \n It contains whatever you want it to. If you are certain that you've come for treasure, go ahead and type 'treasure'. Otherwise, you're free to leave.")
    atlast = last.lower()
    if atlast == "treasure":
        print ("Here's your treasure! \n")
        print ( ''' ******************************************************************************* 
          |                   |                  |                     | 
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  | 
|___________________|__"=._o`"-._        `"=.______________|___________________ 
          |                `"=._o`"=._      _`"=._                     | 
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************  ''')
else:
    print ("Ahh, lost the chance to treasure by not typing 1, 2, or 3.")

#Yousician guitar, drawing, reading, writing
