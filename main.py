#!/usr/bin/python3
import os 
from math import floor
import platform
from processing_py import *

# Define a color for output
GreenC="\033[0;32;40m"
ResetC="\033[0;37;40m"

# Clear the console screen (attempting both Windows and Unix commands)
from platform import system

if platform.system() == "Windows":
    # Code to run on Windows
    os.system("cls")
else:
    # Code to run on anything else
    os.system("clear")



#Make window for visualiseation
app = App(600,400)
app.background(0,0,0)
app.strokeWeight(1)
app.stroke(255)
app.fill(255)

#Draws triangles with markers based of nubers a,b
def draw_triangle(shapeOffset, a, i,shapeScale):
    app.triangle(shapeOffset[0]*shapeScale, shapeOffset[1]*shapeScale, (int(a) + shapeOffset[0])*shapeScale, shapeOffset[1]*shapeScale, (int(a) + shapeOffset[0])*shapeScale, (i + shapeOffset[1])*shapeScale)

    


    if shapeOffset[0] < app.width:
        shapeOffset[0] += int(a) + 25
    else:
        shapeOffset[1] += i + 25
        shapeOffset[0] = 10
    app.redraw()




# Prompt user for input
a = input("Input A:")
brF = input("Brute Force Mode (True/False)")
EnReOu="\nPythagorien Triple List\n"
shapeOffset=[10,10]
shapeScale=5
# Check if brute force mode is not activated
if (brF == "False" or brF == "f"):
        # Get the range of numbers to check for Pythagorean triples
        rS = input("Input Range Start:")
        rE = input("Input Range End:")
        sB = input("Show Non-Pythagorien triples (True/False)")
        
        # Iterate through the range
        for i in range(int(rS),int(rE)):
                # Calculate the hypotenuse
                c = (int(a)**2 + i**2)**0.5
                
                # Check if user wants to see non-Pythagorean triples
                if (sB == "True" or sB == "t"):
                        # Check if the calculated hypotenuse is an integer
                        if (c == floor(c)):
                                # Print and record the Pythagorean triple
                                print(GreenC+"is pypytri (YES) a:"+str(a),"b:"+str(i),"c:"+str(floor(c))+ResetC)
                                EnReOu += GreenC+"(YES) a:"+str(a) + " " + "b:"+str(i)+" "+"c:"+str(floor(c)) + "\n"+ResetC
                                draw_triangle(shapeOffset,a,i,shapeScale)
                        else:
                                # Print the non-Pythagorean result
                                print("is pypytri (NO) a:"+str(a),"b:"+str(i),"c:"+str(c))
                elif (sB == "False" or sB == "f" and c==floor(c)):
                                # Print only Pythagorean triples
                                print(GreenC+"(YES) a:"+str(a),"b:"+str(i),"c:"+str(floor(c))+ResetC)
                                draw_triangle(shapeOffset,a,i,shapeScale)

else:
        # If brute force mode is activated
        i=1
        while True:
                i+=1
                # Calculate the hypotenuse
                c = (int(a)**2 + i**2)**0.5
                # Check if the hypotenuse is an integer and not equal to 'a'
                if(c == floor(c) & int(floor(c))!=int(a)):
                        # Print the Pythagorean triple
                        print("a:"+str(a),"b:"+str(i),"c:"+str(floor(c)))
                        draw_triangle(shapeOffset,a,i,shapeScale)
                        # Prompt to exit
                        input("Press Enter to exit:")
                        # Clear the screen and exit
                        system("clear")
                        system("clr")
                        exit()

# Print the recorded Pythagorean triples
print(EnReOu)
# Prompt to exit
input("Press Enter to exit:")
# Clear the screen and exit
from platform import system

if platform.system() == "Windows":
    # Code to run on Windows
    os.system("cls")
else:
    # Code to run on anything else
    os.system("clear")

exit()
