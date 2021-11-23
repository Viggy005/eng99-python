print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
# A1a:
def return_all_divisors(number):
    list_of_divisors = []
    #print(f"List of all divisors of {number} are:")
    for num in range(1,number+1):

        if number % num == 0:
            #print(f"{num} is a divisor of {number}")
            list_of_divisors.append(num)
    #print(list_of_divisors)
    return list_of_divisors

print(return_all_divisors(10))
print(return_all_divisors(1))
print(return_all_divisors(0))
print(return_all_divisors(100))

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
    elif num1 == num2:
        return True
    else:
        return False

print(check_if_factor(10,4))
print(check_if_factor(1,1))
print(check_if_factor(0,0))


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
    #print(f"The position of {letter} is:")
    #print(alphabet.index(letter)+1)
    return alphabet.index(letter)+1

print(find_position_of_letter("b"))
print(find_position_of_letter("z"))
print(find_position_of_letter("a"))
print(find_position_of_letter("v"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
# A2b:
def generate_id_based_on_postion_of_each_letter(name):
    id = []
    id_str = ""

    for letter in name:
        id.append(find_position_of_letter(letter))
        id_str += str(find_position_of_letter(letter))
    id_str = int(id_str)
    return id_str

print(generate_id_based_on_postion_of_each_letter("aaa"))
print(generate_id_based_on_postion_of_each_letter("avz"))
print(generate_id_based_on_postion_of_each_letter("viggy"))

#test =[]
#print(len(test))
print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)
# A2c:
# -------------------------------------------------------------------------------------- #
#stg = "1234"
#print(len(stg))
def generate_password(name):
    id = generate_id_based_on_postion_of_each_letter(name)
    #print(id)
    number_to_subratct = 0
    for no in range(len(str(id))):
        number_to_subratct += int(str(id)[no])
    password = id - number_to_subratct
    return password

print(generate_password("aaa"))
print(generate_password("a"))
print(generate_password("zz"))

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# A3a:
def check_if_prime(number):
    if_prime = True
    for no in range(2,number):
        if number % no == 0:
            if_prime = False
    return if_prime
print(check_if_prime(7))
print(check_if_prime(4))
print(check_if_prime(1))
print(check_if_prime(0))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit
# A3b:
# -------------------------------------------------------------------------------------- #
def no_error_check_if_prime(number):
    if str(number).isdigit() == False:
        print("you have not entered a number so cant check if its prime or not")
        return None
    else:
        if_prime = True
        number = int(number)
        for no in range(2, number):
            if number % no == 0:
                if_prime = False
        return if_prime

print(no_error_check_if_prime("j"))
print(no_error_check_if_prime("7"))
print(no_error_check_if_prime("10"))
print(no_error_check_if_prime(7))
print(no_error_check_if_prime(10))








