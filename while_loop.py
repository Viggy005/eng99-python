# x = 0
# while True:
#     print(f"x is currently {x}")
#     x+=1
#     if x == 10:
#         break
#     print(f"x is now {x}")
#     print("------------")
#
# print("broken out of loop")
prompt_for_age  = True

# while prompt_for_age:
#     age = input("what is your age in years")
#     if age.isdigit():
#         #age = int(age)
#         prompt_for_age = False
#     else:
#         print("pls provide age in digits")

while prompt_for_age:
     age = input("what is your age in years")
     if int(age) < 120 and age.isdigit() == True:
         #age = int(age)
         prompt_for_age = False
     else:
         print("pls provide age below 120")
