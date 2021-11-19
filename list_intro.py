shopping_list = ["eggs","bread","cheese","milk"]
print(shopping_list, type(shopping_list))

print(shopping_list[0])
print(shopping_list[2:])
shopping_list.append("chicken")
print(shopping_list)

nested = [
    [1,2,3],
    ["a","b"],
    [False, True]

]
print(nested)
print(nested[2][1])

#tuples - immutable

colour = ("red","yellow","green","red")
print(colour.count("red"))
print(colour.index("yellow"))

#sets - unordered, cant index it,

car_parts = {"wheels","doors", "exhaust","wheels"}
print(car_parts, type(car_parts))
car_parts.add("seats")
car_parts.remove("wheels")
print(car_parts, type(car_parts))
l = [1,2,3,1,2,3,4,5,6]
print(set(l))
print(set(l))
print(l)
