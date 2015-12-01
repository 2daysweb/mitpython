#Finding cube root through approximation methods

x = 64.0
epsilon = 0.01
step = epsilon**2
numGuesses = 0.0
ans = 0.0

while (abs(ans**3 - x)) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = ' + " " + str(numGuesses))
if abs(ans**3 - x) >= epsilon:
    print("Failed on square root of" + " " + str(x))
else:
    print(str(ans) + " " + "is close to cube root of" + " " + str(x))


    
    
