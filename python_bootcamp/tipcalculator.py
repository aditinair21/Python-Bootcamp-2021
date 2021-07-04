# Tip Calculator
total = int(input ("What is the total bill? $"))
tip = int(input ("How much percentage of a tip do you want to give? 10? 12? \n"))
number = int(input ("How many people are splitting the bill? \n"))
a = total * tip/100
complete = total + a
b=complete/number
print ("Each person has to pay", b, ".")
