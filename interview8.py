number = 8

def numbers(things):
    total = 0
    numStr = ""
    fact = 1
    for x in range(1,things+1):
        numStr += str(x)
        total += x
        fact = fact * x
    print(numStr)
    print("The sum of all the numbers is: " + str(total))
    print("The factorial of all the numbers is: " + str(fact))



numbers(4)