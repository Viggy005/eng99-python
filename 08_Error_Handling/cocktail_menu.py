# a function that takes in a string
# if that string exists in cocktail file
# return "coming right up"
# otherwsie returns "not on the menu, sorry"
def cocktail_order(cocktail: str):
    with open("cocktail.txt", "r") as file:
        content = file.readlines()
        if cocktail+"\n" in content:
            return "Coming right up"
        else:
            return "not on the menu, Sorry"
print(cocktail_order("old fashioned"))
print(cocktail_order("coke"))

with open("cocktail.txt", "r") as file:
    content = file.readlines()
    print(content)

def add_to_menu(cocktail : str):
    with open("cocktail.txt", "r+") as file:
        content = file.readlines()
        if cocktail+"\n" in content:
            return ValueError
        else:
            file.write( cocktail + "\n" )

        #print(file.read())

print(add_to_menu("old fashioned"))
print(add_to_menu("old"))
print(add_to_menu("mojito"))
print(add_to_menu("old fashioned"))
print(add_to_menu("moscow mule"))
print(add_to_menu("iron bru"))


