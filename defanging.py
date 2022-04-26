def defang(IPaddy):
    # IP address composed of numbers and dots (string)
    return IPaddy.replace('.','[.]')            # just replace dot with the desired result

# result on the website is unnecessarily long, but this solution only works in python

TestCases = ["1.1.1.1", "127.3.00.6.2", "1.18.9.7"]

for tc in TestCases:
    print(defang(tc))