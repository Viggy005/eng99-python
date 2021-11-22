# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):# developer friedly:(to de-bug)print(object name) good reper should be able to make an object
#         return f"Location( lattitude= {self.latitude}, longitude= {self.longitude})"
#
#     def __str__(self):# readabel human friendly
#         return "location string output"
# bham_academy = Location(22.875, 67.99)
# print(bham_academy)
# print(repr(bham_academy))
#
#
# # dunnder repper, dunnder string
# print(f"The Sparta Global is located at {bham_academy}")
#dundeer format
n = 0.00487
print(f"percentage:{n:%}")
print(f"fixed point : {n:f}")
print(f"")


class Dog:
    def __init__(self,age):
        self.age = age

    def __str__(self):
        return f""