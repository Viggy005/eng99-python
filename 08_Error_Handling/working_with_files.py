try:
    # file = open("order.txt")
    # print(file, type(file))
    # orders = []
    # # print(file.readline())
    # # print(file.readline())
    # # print(file.readline())
    # # print(file.readline())
    # # print(file.readline())
    # # print(file.readline())
    # # print(file.readlines())
    # # orders = file.readlines()
    # # print(orders, type(orders))
    # for order in file.readlines():
    #     clean_order = order.strip()
    #     orders.append(clean_order)
    # file.close()
    with open("order.txt") as file:
        orders = file.read().split("\n")


except FileNotFoundError as errmsg: #always should include type of error
    print("the file cannot be found")
    print(errmsg)
    raise # raise that error
finally:
    print("always do this, whatever happens")

# with open("tickets.txt","w") as file: # write mode will over write the file
#     for order in orders:
#         file.write(f"One {order} coming right up\n")

# with open("tickets.txt","a") as file: # append mode will add to the file
#     for order in orders:
#         file.write(f"One {order} coming right up\n")

# r- read
# w - - write
# a- append
# x - kind of write mode will fail if file alrqdy exists
# + - ??
# r+ - read as well append to file
# w+ - 
with open("tickets.txt","r+") as file:
    orders = file.read().split("\n")
    for order in orders:
        file.write(f"One {order} coming right up\n")



