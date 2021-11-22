# #iterable
# numbers = [1,2,3,4,5,6,7]
# print(len(numbers))
#
# for number in numbers:
#     square = number ** 2
#     print(square)
#
# print("finished looping")
#
# for i in range(1,5):
#     print(i)

# d = {"name":"viggy", "job":"trainee", "likes":"devops"}
# print(d.items())
# for k,v in d.items():
#     print(k)
#     print(v)
# for item in d.values():
#     print(item)
# for item in d.keys():
#     print(item)

# nested = [[1,2,3],[4,5,6],[7,8,9]]
# for a in nested:
#     print(a)
#     for b in a:
#         print(b)

menu = [
    {"food":"pizza","price":13.00},
    {"food":"burger",'price':9.50},
    {"food":"chips","price":2.60},
    {"food":"water"}
]
total_cost= 0
for item in menu:
    if item.get("price"):
        total_cost += item["price"]

print(total_cost)