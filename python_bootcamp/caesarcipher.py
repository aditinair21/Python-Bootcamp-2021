logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
o = []
def caesar(text, shift, option):
  for l in text:
    old_pos = 0
    if l not in alphabet:
      o.append(l)
      continue
    old_pos = alphabet.index(l)
    if option == 'encode':
      new_pos = old_pos + shift
      inew_pos = new_pos % 24
    if option == 'decode':
      new_pos = old_pos - shift
      inew_pos = new_pos % 26 
    final = alphabet[inew_pos]
    o.append(final)
  print("Your decoded message is: \n")
  print (''.join(o))
youwanna = 'yes'
while youwanna == 'yes':
  instruct = input("Type 'encode' to encode a message and 'decode' to decode a message:\n").lower()
  while instruct != 'encode' and instruct != 'decode':
    print("Please retype the program and enter 'encode' or 'decode' again.") 
    instruct = input("Type 'encode' to encode a message and 'decode' to decode a message:\n").lower()
  message = input("Type your message:\n").lower()
  num = int(input("Type the number you want to shift by:\n"))
  caesar(message, num, instruct)
  youwanna = input("Type 'yes' if you want to go again. Otherwise, type 'no'. ").lower()
  o.clear()
  if youwanna == "no":
    print("Thank you. The program will quit now.")
    sys.exit()