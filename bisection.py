x = 25.0
epsilon = 0.01
high = x
low = 0.0
numGuesses = 0.0
ans = (low+high)/2

while abs(ans**2 - x) >= epsilon:  
    print("for" + " " + str(low) + "low" + " and " + str(high) + "high")
    numGuesses += 1
    if ans**2 < x:
        low = ans
    
    
