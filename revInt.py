def revInt(n):
    lim = 2**31

    if n > lim - 1 or n < -1*lim:
        return 0
        # out of bounds
    else:
        # in bounds

        revNum = int(str(abs(n)).rstrip("0"))        # strip the trailing 0's
        revNum = int(str(revNum)[::-1])         # reverse index using slicing
       
        if n < 0:                       # if the original number was negative
            return -1*revNum
        else:
            return revNum


print(revInt(-14001))
