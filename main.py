#!/usr/bin/python3
from os import system
from math import floor
from colorama import Style, Fore
system("clr")
system("clear")
a = input("Input A:")
brF = input("Brute Force Mode (True/False)")
EnReOu="\nPythagorien Triple List\n"
if (brF == "False" or brF == "f"):
        rS = input("Input Range Start:")
        rE = input("Input Range End:")
        sB = input("Show Non-Pythagorien triples (True/False)")
        for i in range(int(rS),int(rE)):
                c = (int(a)**2 + i**2)**0.5
                if (sB == "True" or sB == "t"):
                        if (c == floor(c)):
                                print(Fore.GREEN+"is pypytri (YES) a:"+str(a),"b:"+str(i),"c:"+str(floor(c))+Style.RESET_ALL)
                                EnReOu += Fore.GREEN+"(YES) a:"+str(a) + " " + "b:"+str(i)+" "+"c:"+str(floor(c)) + "\n"+Style.RESET_ALL
                        else:
                                print("is pypytri (NO) a:"+str(a),"b:"+str(i),"c:"+str(c))
                elif (sB == "False" or sB == "f" and c==floor(c)):
                                print(Fore.GREEN+"(YES) a:"+str(a),"b:"+str(i),"c:"+str(floor(c))+Style.RESET_ALL)
else:
        i=1
        while True:
                i+=1
                c = (int(a)**2 + i**2)**0.5
                if(c == floor(c) & int(floor(c))!=int(a)):
                        print("a:"+str(a),"b:"+str(i),"c:"+str(floor(c)))
                        input("Press Enter to exit:")
                        system("clear")
                        system("clr")
                        exit()
print(EnReOu)
input("Press Enter to exit:")
system("clear")
system("cls")
exit()
