x=i=t=0;b=int(input("breakpoint:"))
while t<b: 
    t+=1;x=t
    while x!=1:x+=(x/-2,(x*2)+1)[int(x%2)];i+=1
    i=0
print(t,i)