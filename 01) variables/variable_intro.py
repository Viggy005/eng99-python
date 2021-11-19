#create 3 variables each should be different type

a = 10
b = 10.5
c= "sparta global"
print(a, type(a))
print(b, type(b))
print(c,type(c))
print(4+5)
print(6*6)
print(5/2)
print(13%3)

# concatination

s1 = "hello"
s2 = "world"
n= 42
print(s1+" "+s2+str(n))
name = "viggy"
age = 23
height = 173
print(f"my name is {name} age is {age*2} height is {height}")
pi = 3.1415926
print(f"pi is {pi:.2f}")
print(f"{1/3:.2%}")

name = input("enter your name\n")
age = int(input("enter your age\n"))
pi = input("enter the value of pi\n")

print(f"my name is {name} and am {age+5} years old and the value of pi is {pi}")

