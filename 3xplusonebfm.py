x=i=t=0
while 1: 
    t+=1;x=t
    while x!=1:x+=(x/-2,(x*2)+1)[int(x%2)];i+=1
    print(t,i);i=0