#Finding a cube root of an integer

x = int(input("Enter a number :"))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) +  " " + "is not a perfect cube")
else:
    print(str(x) + " " + "is a perfect cube")

    
