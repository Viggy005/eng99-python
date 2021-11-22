# age = 15
#
# if age > 15:
#     print("you can watch")
# elif age == 15:
#     print("just about old ")
# elif age <15:
#     print("not old enough")
# if age == 17:
#     print("good")
# name = "vigeshraj"
#
# if "raj" in name:
#     print(name)
#
#
#
# print("this will always run")

# use if-elif-else statement to print
#description of the certificate of the film
certificate = input("enter the certificate type\n")
if certificate == "U":
    print("All can watch the film")
elif certificate in ("PG","U/A"):
    print("children can watch with adult supervision")
elif certificate.upper() == "A":
    print("only 18+ can watch the film")
else:
    print("you have not entered a valid certificate")
