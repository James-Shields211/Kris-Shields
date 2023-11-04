#James Shields ETGG1801 Lab 05
#PART 1: MASS CALCULATOR
print("Part 1: Mass Calculator")
#get user inputs
    ##Ask for input and convert to number 2/2
diameter=float(input("Enter the diameter (in meters) of a spherical object"))
density=float(input("Enter the density (amount of mass per 1x1x1 cube) of a spherical object"))
depth=float(input("Enter the thickness of the outer layer of a spherical object"))
#confirm user inputs
print("you provided the following values for diameter, density, and depth")
print(diameter)
print(density)
print(depth)
input ("Press Enter to continue")
#assign additional variables and do math
        ##Wait until you have the final volume then use density to get the mass (I think you’re getting the mass of the solid outer sphere, but then you’re subtracting the *volume* of the inner part, not the mass of the inner part)
        ##You might want to wait until the end and then round (it subtly changes your output if you round the intermediate parts)
import math
radius=diameter/2
pi=22/7
radius3=radius*radius*radius
total_volume=4/3*pi*radius3
radius_excluded=diameter-(depth*2)
rounded_volume_total=round(total_volume, 2)
total_mass=density*rounded_volume_total
mass_rounded=round(total_mass, 2)
radius_excluded3=radius_excluded*radius_excluded*radius_excluded
volume_excluded=4/3*pi*radius_excluded3
final_volume=total_volume-volume_excluded
rounded_volume_final=round(final_volume,2)
#output volume to user
print("The volume of the sphere based on the details you provided is", rounded_volume_final, "cubic meters (rounded to 2 decimal points)")
#output mass to user
print("The mass of the sphere based on the volume and the details you provided is", mass_rounded, "grams (rounded to 2 decimal points)")
input("Press Enter to continue to Part 2")


#------------------------------------------------------------


#PART 2: HP BAR
print('Part 2: HP Bar')
#get health value inputs from user
    ##Ask for input and convert to number (1/1)
hp_cur=round(int(input("Enter your current HP number")),2)
hp_max=round(int(input("Enter your maximum HP number")),2)
#internally check for outlier variables
if hp_cur > hp_max:
    print("Your current HP is greater than your maximum HP. You either made a mistake or you have Overhealth.")
    input("Press Enter to continue")
if hp_cur == 0:
    print("Your current HP is zero. Are you sure you're not dead?")
    input("Press Enter to continue")
#confirm the user's information externally
print("Your current HP is", hp_cur, "and your maximum HP is", hp_max)
#convert HP to a percent, and give that to user
print("percent of HP:", round((100*hp_cur)/hp_max,2))
#convert HP to a number relative to the max of 40
percent_hp_relative= int(round((40*hp_cur)/hp_max,0))
internal_bar_length=40
    ##I would save that 40 to a variable so if you were to change it, you’d only have to change the value one place (5/5)
#print out the health bar
    ##print the bar (including “scalability” with bar_size)
print("/", '-'*internal_bar_length, "\\")
print("|",'+'*percent_hp_relative, ' '*(internal_bar_length-percent_hp_relative-1),"|")
print("\\", '-'*internal_bar_length, "/")
#await input to quit
input("Press Enter to quit...")
#Variables Used: diameter, density, depth, pi, radius, radius3, total_volume, volume_rounded, total_mass, mass_rounded, hp_cur, hp_max, percent_hp_relative, internal_bar_length