m=int(input("m: "))
s=int(input("s: "))
h=int(input("h: "))
t=(100*(m+s+h))/300
if t >= 40:
    print("good")
elif t >= 40 and m>33 and s>33 and h>33:
    print("pass")
else :
    print("fail")