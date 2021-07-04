# Rock Paper Scissors
import random
choice = input ("What weapon do you choose? Type 0 for rock, 1 for scissors, and 2 for paper. ")
computer = ["rock", "paper", "scissors"]
comchoice = random.choice(computer)
if choice == "0" and comchoice == "rock":
    print ('''  ______
   /(    )\
   \ \  / /
    \/[]\/
      /\
     |  |
     |  |
     |  |
     |  |
     |  |
     \  /   
      \/) ''')
    print("The computer chose", comchoice, ". It's a tie!")
elif choice == "0" and comchoice == "paper":
    print ('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) ''')
    print ("The computer chose", comchoice, ". You and rock lose. (:(")
elif choice == "0" and comchoice == "scissors":
    print ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')
    print ("The computer chose", comchoice, ". You WIN! :D")

if choice == "1" and comchoice == "paper":
    print ('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')
    print ("The computer chose", comchoice, ". You WIN! :D")
elif choice == "1" and comchoice == "rock":
    print ('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''')
    print ("The computer chose",comchoice, "You LOSE (:(")
elif choice == "1" and comchoice == "scissors":
    print ('''
   /(    )\
   \ \  / /
    \/[]\/
      /\
     |  |
     |  |
     |  |
     |  |
     |  |
     \  /   
      \/ ''')
    print ("Both the computer and you chose scissors. IT'S A TIE.")
if choice == "2" and comchoice == "rock":
    print ('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) ''')
    print ("The computer chose", comchoice, "You WIN.")
elif choice == "2" and comchoice == "paper":
    print ('''
   /(    )\
   \ \  / /
    \/[]\/
      /\
     |  |
     |  |
     |  |
     |  |
     |  |
     \  /   
      \/ ''')
    print ("It's a TIE.")
elif choice == "2" and comchoice == "scissors":
    print ('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')
    print ("The computer chose", comchoice, "You lose.")
    
    
    
    
