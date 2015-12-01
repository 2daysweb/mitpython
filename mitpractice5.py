x = int(input("Enter a number :"))
for ans in range(0, abs(x) + 1):
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print("Not a cube")
else:
    if x < 0:
            ans = -ans
    print("Cube root of" + str(x) + " " + str(ans))
        
              
