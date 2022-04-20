from distutils.command import check
import math

def checkPalindrome(aString):
    # palindromes can be of any length
    aString = aString.lower()       # normalizing the string
    
    # remove all non-alphanumeric chars
    goodStr = ''.join(chr for chr in aString if chr.isalnum())      # join the other 2 halves if chr is alnum

    strLen = len(goodStr)           # getting the length (n)
    for idx in range(math.floor(strLen/2)):                         # could probably just typecast with int() because it will truncate the floating points
        if goodStr[idx] != goodStr[strLen-idx-1]:                   # need the -1 as idx is initially 0, and aString[strLen] is out of bounds
            return False
        else:
            continue
    return True

TestCases = ["racecar", "horse", "madam", "hannah", "peepeepoopoo", "a man, a plan, a canal: panama"]

for tc in TestCases:
    print(checkPalindrome(tc))

