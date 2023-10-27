# a="sagar"
# b=1
# print(a)
# print(b)
##############
# a="sagar"
# a=1
# print(a)
############
# a=int(1)
# b=str(2)
# c=float("sagar")
# print(a)
# print(b)
# print(c)
############case sensitive##############3
# a=123
# A="Sagar"
# print(a)
# print(A)
# print(A)
######################multiple valuas##########3
# a,b,c=1,"sagar","vidyasagar"
# print(a,b,c)
# a,b,c=1,"sagar","vidyasagar"
# print(a)
# print(b)
# print(c)
######## unpack a collections######33
# animals=["cat","dog","snake"]
# a,b,c=animals
# print(a)
# print(b)
# print(c)
######################
# a,b,c=1,2,3
# print(a,b,c)
######################
# a=5
# b=5
# print(a+b)
###########3global variable###########
# x = "awesome"
# def myfunc():
#   print("Python is ",x)
# myfunc()
##########Global variable##########3
# x = "awesome"
# def myfunc():
#     x="sagar"
#     print("Python is ",x)
# myfunc()
# print("python is",x)
##########remove duplicate from strings
# a=["a","b","s","a"]
# a=list(dict.fromkeys(a))
# print(a)
##########################3Split string###########3
# a = "Hello, World!"
# print(a.split(","))
###############Strip method removre soace##########
# a = " Hello, World!"
# print(a.strip())
#########################lists###############
# a=["sagar","banana","chari","banan"]
# print(a)
# a=["sagar","banana","chari","banan"]
# print(len(a))
# a=["sagar","banana","chari","banan"]
# b=[1,2,3,75]
# c=[True,False]
# print(type(a),(b),(c))
#########3extend#########33
# a=["sagar","banana","chari","banan"]
# b=["Vidya"]
# a.extend(b)
# print(a)
#####remove###########33
# a=["sagar","banana","chari","banan"]
# a.remove("banana")
# print(a)
# ###########pop########3
# a=["sagar","banana","chari","banan"]
# a.pop(2)
# print(a)
# ##########del##############
# a=["sagar","banana","chari","banan"]
# del a[1]
# print(a)
# a=["sagar","banana","chari","banan"]
# a.clear()
# print(a)
#####looop list#####3
# a=["a","b","c","d"]
# for i in a:
#     print(i)
########range#####3
# a=["a","b","c","d"]
# for i in range (len(a)):
#     print(a[i])
########33sort######33
# a=["p","a","d","l"]
# a.sort()
# print(a)
# a=[180,16,12,78]
# a.sort()
# print(a)
#####copymethod##########
# a=[180,16,12,78]
# b=a.copy()
# print(b)
# a=[180,16,12,78]
# b=list(a)
# print(b)
##########join#########
# a=[180,16,12,78]
# b=["p","a","d","l"]
# c=a+b
# print(c)

# a=[180,16,12,78]
# b=["p","a","d","l"]
# for i in b:
#     a.append(i)
#     print(a)
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
# print(list1)
# a=(1,2,3,4)
# print(type(a))
# a=(1,2,3,4)
# print(len(a))
# a=("a", "b", "c")
# b=list(a)
# b.append("g")
# a=tuple(b)
# print(a)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)
# a=("a", "b", "c")
# del a
# print(a)

# a=("a", "b", "c")
# for i in range(len(a)):
#  print(a[i])
# #
# a=("a", "b", "c")
# for i in a:
#     print(a)

# a=("a", "b", "c")
# print(a)

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1
#
# a=("a", "b", "c")
# b=(5,6)
# c=a+b
# print(c)
#
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
# a=("a", "b", "c")
# b=a*2
# print(b)

#########sets#########
# a={"a", "b", "c","a"}
# print(a)
#
# a={"a", "b", "c","a"}
# print(len(a))
#
# a=set(("a", "b", "c","a"))
# print(a)

# a={"a", "b", "c","a"}
# for i in a:
#     print(a)
######33add items#########3
# a={"a", "b", "c","a"}
# a.add("fdfddf")
# print(a)

# a={"a", "b", "c","a"}
# b={"xxxx"}
# a.update(b)
# print(a)
#
# a={"a", "b", "c","a"}
# a.remove("a")
# print(a)

# a={"a", "b", "c","a"}
# a.discard("a")
# print(a)

# a={"a", "b", "c","a"}
# b=a.pop()
# print(b)
# print(a)

# thisset = {"apple", "banana", "cherry"}
#
# thisset.clear()
#
# print(thisset)
#
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)

# a={"a", "b", "c","a"}
# b={"a", "b", "c"}
# a.intersection_update(b)
# print(a)

# d1={"brand": "Ford",}
# print(d1)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["model"] = "kea"
# print(thisdict)

#
# a=2
# b=3
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are eqaul")

# a=10
# b=5
# if b>a:
#     print("b is greater then a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater then b")

# a=10
# b=5
# if b>a:
#     print("b is greater then")
# else:
#     print("a is greater then b")

# a=10
# b=5
# if not b>a:
#     print("b is greater then")
# else:
#     print("a is greater then b")

# a = 33
# b = 200
# if b>a:

# i = 1
# while i < 6:
#     print(i)
# i += 1

# a=["a","b"]
# for x in a:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


# for i in range(6):
#     print(i)


######3functions######3
# def my_function():
#     print("hello")
# my_function()

# def my_function(fname):
#     print(fname,"sagar")
# my_function("bro")

# def my_function(child1,child2):
#     print("the youngest child is ",child2)
# my_function(child1="Email",child2="Mail")

# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# x=lambda a:a+10
# print(x(5))

# a=lambda a,b:10+41
# print(a(10,41))

# class MyClass:
#   x = 5
# print(MyClass)

# class MyClass:
#   x = 5
#
# p1 = MyClass()
# print(p1.x)
#
# class Person:
#     def __int__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = person(name:"sagar",age:13)
#
# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# import myModule
# myModule.greeting("hello")
# import myModule
# from importlib import reload
# reload(myModule)
# import myModule
# myModule.a("Jonathan")


# import datetime
# x = datetime.datetime.now()
# print(x)

# import datetime
#
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%A"))

# x = min(5, 10, 25)
# y = max(5, 10, 25)
#
# print(x)
# print(y)
#
#
# x = abs(-7.25)
#
# print(x)
#
# import math
# a=math.sqrt(64)
# print(a)

# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

f=open("C:\Users\HP\Desktop\new 3.txt","r")
print(f.read())


