from sqlalchemy import null


def FizzBuzz(n):
    result = []                 # empty list to store answers
    for idx in range(1, n+1):   # [1, n+1) (Not inclusive)
        if idx % 3 == 0 and idx % 5 == 0:
            result.append("FizzBuzz")
        elif idx % 3 == 0:
            result.append("Fizz")
        elif idx % 5 == 0:
            result.append("Buzz")
        else:
            result.append(idx)
    
    return result


print(FizzBuzz(15))
