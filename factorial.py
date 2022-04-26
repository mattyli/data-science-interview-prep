def calcFactorial(num):     # will return an int
    if num < 0:
        return -1

    if num == 0:                            # base case (0! = 1)
        return 1
    else:
        return num * calcFactorial(num-1)   # n*(n-1)! <-- recursive part

TC = [5,7,10,12,0,-3]

for tc in TC:
    print(calcFactorial(tc))
