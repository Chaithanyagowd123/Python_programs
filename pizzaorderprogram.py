print("Thank you for choosing Python Pizza Deliveries!")
size = input("please enter size of your pizza Y/N") # What size pizza do you want? S, M, or L
add_pepperoni = input('you want pepperoni  Y/N') # Do you want pepperoni? Y or N
extra_cheese = input("do you want extra cheeseY/N") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
Bill=0
if(size=='S'):
  Bill+=15
elif(size=='M'):
  Bill+=20
else:
  Bill+=25
if(add_pepperoni=='Y'):
  if(size=='S'):
    Bill+=2
  else:
    Bill+=3
if(extra_cheese=='Y'):
  Bill+=1

print(f"Your final bill is: ${Bill}.")

