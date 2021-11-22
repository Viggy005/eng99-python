print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
# A1a:
def return_all_divisors(number):
    list_of_divisors = []
    #print(f"List of all divisors of {number} are:")
    for num in range(1,number):

        if number % num == 0:
            #print(f"{num} is a divisor of {number}")
            list_of_divisors.append(num)
    print(list_of_divisors)
    return list_of_divisors

return_all_divisors(10)

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function)
# A1b:
# -------------------------------------------------------------------------------------- #
def check_if_factor(num1,num2):
    if num1 in return_all_divisors(num2):
        return True
    elif num2 in return_all_divisors(num1):
        return True
    else:
        return False

print(check_if_factor(10,4))

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
# A2a:
# test = [1,2,3]
# print(test.index(3)+1)
def find_position_of_letter(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    print(f"The position of {letter} is:")
    print(alphabet.index(letter)+1)
    return alphabet.index(letter)+1

find_position_of_letter("b")

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
# A2b:
def generate_id_based_on_postion_of_each_letter(name):
    id = []
    for letter in name:
        id.append(find_position_of_letter(letter))
    return id

print(generate_id_based_on_postion_of_each_letter("viggy"))

test =[]
print(len(test))






