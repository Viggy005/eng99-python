import math
def find_sqrt(n):
    return math.sqrt(n)

def find_ceil(n):
    return math.ceil(n)

def divisors(number):
    list_of_divisors = []
    #print(f"List of all divisors of {number} are:")
    for num in range(1,number+1):

        if number % num == 0:
            #print(f"{num} is a divisor of {number}")
            list_of_divisors.append(num)
    print(list_of_divisors)
    return list_of_divisors