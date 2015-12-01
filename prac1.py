epsilon = .01
step = epsilon**2
ans = 0.0
x = 25.0
numGuesses = 0.0

while abs((ans**2 - x)) >= epsilon and ans**2 <= x:
    ans += step
    numGuesses += 1
if abs(ans**2 - x) >= epsilon:
    print(str(ans) + " " + "is not close enough to the sq. root of" + " " + str(x))
else:
    print(str(ans) + " " + "is approximately the sq root of" + " " + str(x))
print(numGuesses)

    


