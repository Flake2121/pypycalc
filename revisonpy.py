from math import floor
from random import randint
a=randint(1,100)
b=c=0
while c!=floor(c) or c==0:
    b+=1
    c=(a**2+b**2)**0.5
    #print("a:",a,"b:",b,"c:",c)
print("a:",a,"b:",b)
if int(input("enter ans: "))==c:print("correct!");input()
else:print("wrong");input()

