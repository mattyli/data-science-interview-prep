def checkAnagram(aString, bString):
    # normalize the strings
    aString, bString = aString.lower(), bString.lower()
    if len(aString) != len(bString):
        print("strings are not the same length")
        return False

    # use dictionary and counts again 
    # first check if the string lengths are the same, if they're not then they can't be anagrams

    dictA, dictB = dict(), dict()                           # initializng empty dicts

    for chrA, chrB in zip(aString, bString):
        dictA.update({chrA : aString.count(chrA)})          # counting the occurrences of all chars in aString
        dictB.update({chrB : bString.count(chrB)})          # ^ same but for bString

    # dictonaries are ordered, following method might now work
    if dictA != dictB:
        return False
    else:
        return True

# testing script
TestCases = [("apple","pale"), ("knee","keen"), ("listen","silent")]
for tc in TestCases:
    print(checkAnagram(tc[0], tc[1]))