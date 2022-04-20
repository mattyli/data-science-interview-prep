def findUniqueChar(someString):
    # normalize all the characters in the string
    someString = someString.lower()

    # use dictionary with char as key, count of char as value
    # char : count

    strDict = dict()        # make an empty dict
    for chr in someString:
        strDict.update({chr : someString.count(chr)})     # getting the count
    
    # now need to get the first occurence of count = 1
    for key in strDict:
        if strDict[key] == 1:
            return someString.find(key)                   # looping through the dict
        else:
            continue
    return -1

for s in ["Appsilon", "Appsilon Poland", "abcabc"]:
    print(findUniqueChar(s))
