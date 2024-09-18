#!/bin/python
import os 
import math
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
app = App(int(input("Window X: ")),int(input("Window Y: ")))
app.background(50)
app.strokeWeight(1)
app.noStroke()
app.fill(255)
app.textAlign(CENTER)




#Draws triangles with markers based of nubers a,b
def draw_triangle(shapeOffset, a, i,shapeScale):
    app.redraw()
    app.triangle(shapeOffset[0]*shapeScale, shapeOffset[1]*shapeScale, (int(a) + shapeOffset[0])*shapeScale, shapeOffset[1]*shapeScale, (int(a) + shapeOffset[0])*shapeScale, (i + shapeOffset[1])*shapeScale)
    app.textAlign(LEFT)
    app.fill(0)
    app.text("a: "+a,(shapeOffset[0]*shapeScale)-15,(shapeOffset[1]-1)*shapeScale)
    app.text("b: "+str(i),((shapeOffset[0]+int(a)+1)*shapeScale)+4,(shapeOffset[1]*shapeScale)+((i/2)*shapeScale))
    app.textAlign(RIGHT)
    app.text("c: "+str(int((int(a)**2+i**2)**0.5)),shapeOffset[0]*shapeScale+(int(a)/2)*shapeScale,(shapeOffset[1]+i)*shapeScale-(i/3)*shapeScale)
    app.fill(255)

    app.redraw()
    shapeOffset[0] += (int(a)*1.5)
    if (shapeOffset[0]*shapeScale+(len(a))*30) > app.width:
           shapeOffset[1] += i + 3
           shapeOffset[0] = 5*shapeScale
app.textSize(13)




# Prompt user for input
app.textSize(30)
a = input("Input A:")
app.text("a: "+str(a),app.width - (len(str(a))*30),app.height-50)
app.redraw()
brF = input("Brute Force Mode (True/False)")
EnReOu="\nPythagorien Triple List\n"
shapeScale=float(input("Scale: "))
shapeOffset=[3,10/shapeScale]
app.textSize(13)


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
                        if (c == math.floor(c)):
                                # Print and record the Pythagorean triple
                                print(GreenC+"is pypytri (YES) a:"+str(a),"b:"+str(i),"c:"+str(math.floor(c))+ResetC)
                                EnReOu += GreenC+"(YES) a:"+str(a) + " " + "b:"+str(i)+" "+"c:"+str(math.floor(c)) + "\n"+ResetC
                                draw_triangle(shapeOffset,a,i,shapeScale)
                        else:
                                # Print the non-Pythagorean result
                                print("is pypytri (NO) a:"+str(a),"b:"+str(i),"c:"+str(c))
                elif (sB == "False" or sB == "f" and c==math.floor(c)):
                                # Print only Pythagorean triples
                                print(GreenC+"(YES) a:"+str(a),"b:"+str(i),"c:"+str(math.floor(c))+ResetC)
                                draw_triangle(shapeOffset,a,i,shapeScale)

else:
        # If brute force mode is activated
        i=1
        while True:
                i+=1
                # Calculate the hypotenuse
                c = (int(a)**2 + i**2)**0.5
                # Check if the hypotenuse is an integer and not equal to 'a'
                if(c == math.floor(c) & int(math.floor(c))!=int(a)):
                        # Print the Pythagorean triple
                        print("a:"+str(a),"b:"+str(i),"c:"+str(math.floor(c)))
                        draw_triangle(shapeOffset,a,i,shapeScale)
                        # Prompt to exit
                        input("Press Enter to exit:")
                        # Clear the screen and exit
                        

                        if platform.system() == "Windows":
                            # Code to run on Windows
                            os.system("cls")
                        else:
                            # Code to run on anything else
                            os.system("clear")

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
