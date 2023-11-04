# James Shields, ETGG1801-01 lab 03 1/1
fname="James" #2/2
lname="Shields"
age=18
minutes=30
rate=5
opposition=15
adjacent=5
import math
adjacent2=adjacent*adjacent
opposition2=opposition*opposition
hypotenuse=math.sqrt(opposition2 + adjacent2)
#Step 6a works
print("My name is", fname, lname, "and I am", age, "years old.") #1/1
#Step 6b SyntaxError invalid syntax
print("My name is", fname, lname, "and I am", age, "years old.", sep="...") #1/1
# Step 6c works
print("The vehicle traveled",(rate*60),"kilometers in",(minutes*60),"seconds at a rate of ",(rate*2),"kilometers per hour") #2.4/3 (calc distance travelled, I have rate in km/min)
# Step 6d "works"
# I can get the code to give me a number, but its not the correct numer (it gave me ~26.925, but when I did the math manually I got 25)
print("The hypotenuse of a triangle is", hypotenuse, "feet if the opposite side is", opposition, "feet and the adjacent side is", adjacent, "feet")# Step 6e works 4/4
input("Press Enter to quit...") #1/1
#tota, 20.15/21 (total 22pts possible, grade out of 21)