# Dont
# Repeat
# Yourself

# def print_something(): #<----- defining the function
#     print("something has been printed")
#     print("something else is being printed")
#
# print_something() # <---- calling the function
# print_something() # <---- calling the function
# print_something() # <---- calling the function
# def print_something1(string_to_print):
#     print(f"{string_to_print} has been printed")
#     print(f"{string_to_print} has been printed again")
#
# print_something1("banana")
# print_something1("apple")
# print_something1("kiwi")
# print(string_to_print)

# write a function that returns the result of multiplying
#3 numbers and dividing totla by two

# def multiply_and_divide_by_2(num1,num2,num3):
#     total = (num1 * num2 * num3) // 2
#     return total
# x = multiply_and_divide_by_2(1,10,3)
# print(x)
# print(multiply_and_divide_by_2(2,2,2))

#
# multplies everthing in the tuple and divides the product by 2
#
# def shout_n_times(string_to_shout, number_of_times_to_shout=1):#default arguments will be overridden if we specift in calling
#     return string_to_shout.upper() * number_of_times_to_shout
# print(shout_n_times("hello,3",3))
# print(shout_n_times("boo"))
#note - anyhting to be specifed goes first in argument list
# def shout_n_times(string_to_shout="hello1", number_of_times_to_shout=2,loud = True):#default arguments will be overridden if we specift in calling
#     if loud:
#         string_to_shout = string_to_shout.upper()
#     return string_to_shout * number_of_times_to_shout
# print(shout_n_times("hello,3",3,False))
# print(shout_n_times("boo"))
# print(shout_n_times())

# type hints

# def shout_n_times(string_to_shout: str, number_of_times_to_shout: int =2,loud = True):#default arguments will be overridden if we specift in calling
#     if loud:
#         string_to_shout = string_to_shout.upper()
#     return string_to_shout * number_of_times_to_shout
# print(shout_n_times("hello,3",3,False))
# print(shout_n_times("boo"))
# print(shout_n_times(345,"it",loud = True))
#
# name with something clear
# lower case
# keep them small - break it into smaller function

#addition
#subtraction
#multiplication
#division
def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

print(addition(2,2))
print(subtraction(3,6))
print(multiplication(2,2))
print(division(10,100))


