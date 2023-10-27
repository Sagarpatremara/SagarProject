# x=int(input("Enter number 1:"))
# print(end="\r")
# y=input("Enter Number 2:")
# print("1st number is",x)
# print(end="\r")
# print("2nd text is",y)
# z=x+5
# print(type(z))
# print(type(y))
# print(z)
######
# c,b,d=2,3,4
# g=h=j=2
# print(c,b,d)
# print(g,h,j)
# fruits=["apple","mango","strawberry"]
# x,y,z=fruits
# print(x,y,z)
# print(x+y+z)
# print(y)
########
# x=5
# y="john"
#print(x+y)#would give error
#correct one
# print(x,y)
#if you want without space you can use this
# print(str(x)+y)
#########
# x="awesome"
# def s():
#     x="cool"
#     print(x)
# s()
# print(x)
#########
# y="awesome"
# def s():
#     global y
#     y="helios"
#     print(y)
# print(y)
# s()
# print(y)
#########
# import random
# x=random.randint(300,400000)
# print(x)
#########
# a="""helios mah
# helios mah
# helios mahhelios mah
# helios mah
# helios mah"""
# print(a)

# b="helios"
# print(b[4])
# for i in b:
#     print(i)
# if "o" in b:
#     print("o exists in b")
# if "X" not in b:
#     print("X doesnt exist in b")

#######
# b="niagra falls is on the verge of extinction"
# print(b[2:5])#from 2 - 5
# print(b[:5])# from 0 -5
# print(b[5:])# after 5
# x=len(b)#length of a string
# c=b[::-1]#reverse a string
# print(str(c))
# d=b.strip(" ")#strips spaces in start and end
# print(d)
# e=list(b)#convert string to list
# print(e)
# f=b.replace("n","gg")#replaces n with gg
# print(f)
# g=b.split(" ")#converts text to words list or splits text into list of words.
# print(g)
# h="heads"
# i="up"
# k=h+i#concatenate strings without any space or charecter in between
# j=h+" "+i
# print(k)
# print(j)#concatenate strings
########
# A=12
# b="Five guys"
# c="delayed"
# d="hi ! there was a {} year old at {} who {} my order"
# print(d.format(A,b,c)) # formats with blanks
# e="I was at {1} and this {0} year old kid {2} my order"
# print(e.format(A,b,c)) # formats with bit places
# f="Hello ! We are the thomson-Kilngs \"Vikings\" from the future"
# print(f)#escape charecter
#LEARN PYTHON BOOLEANS
########
# x = 200
# print(isinstance(x, int))#Check if an object is an integer or not
#######

# x="wwssww"
# f=list(x)
# for i in range(0,len(f)):
#     cur=f[i]
#     prev=f[i-1]
#     char_to_count=f[i]
#     if cur!=prev:
#         count=f.count(char_to_count)
#         print(f[i],"has occured",count,"times")
########
# a="  h e  li os  "
# b=list(a)
# print(b)
# c="".join(b)# convert list to string
# e=c.replace(" ","")
# print(e)
###########
# a=[1,2,2,2,3,4,44,44,5,6,3,2,1]
# c=list(reversed(a))#reverse a int list and assign it to variable
# print(c)
# x=[1,2,3]
# x.reverse()#reverse a int list without assigning it to a variable
# print(x)
# b=["h","e","l","l",2,4]
# s=list(map(str,b))#convert list with multiple data types to string
# print("".join(s))
# v="helios"
# z=list(x)#to convert string to list
# print(z)
# d=len(b)# to count length/size of list
# print(d)
########
# l="gggeretettytytrtr"
# e=list(l)#string to list
# f=set(list(e))# remove duplicates form list
# g="".join(f) #list to string
# print(g)
########
# a=[1,2,8,7,6,5,4]
# b=list(reversed(a))
# c=sorted(b)#to sort in ascending order
# d=c[::-1]# to sort ascending ordered list to descending order
# print(d)
##########
# import  random
# x=random.randint(1,19)
# print(x)
########
# a=12345678
# b=str(a)[::-1]
# print(b)
########
# a=[1,2,3,4,5,6,7,88,8,"helios","raju","xenon"]
# a.remove(88)# to remove elements from list
# b=[]
# b=a
# print(b)
##########
# a="basheeweer"
# count=0
# for i in a:
#     if i=="e":
#         count+=1
# print(count)

# a=[11,2,3,4]
# b=["aalo","bello","chello","dello","ello","hello"]
# b.append("helios")# to append to end
# b.insert(0,"kellogies")# to append element at a position
# print(b)
# b.extend(a)#it is used to combine 2 lists
# b.remove("aalo")# to remove element in list
# del b[0]#to delete list item in specified index
# del b# to delete entire list
# c=["1,3,2,4,2,1"]
# c.clear()    #to empty list contents
# print(c)

# a="Helios1234"
# b=list(a)
# c="".join(b)
# print(c)

#####convert string to list
# w=[1,2,3,4,5,6,7,8]
# x=list(w)
# y=list(map(str,x))
# z="".join(y)
# print(z)
#############
# a=[1,2,3,4,5,6]
# a.sort(reverse=True)
# b=list(reversed(a))
# print(b)
# c=list.copy(a)
# print(c)
# d=[7,8,9,10]
# e=[]
# a.extend(d)
# e=a.copy()
# print(e)
# f=["h","e","l","i"]
# print(f.index("l"))

# numbersx = [1, 2, 3, 4, 5, 6, 7]
# for i in range(len(numbersx)):
#     e=numbersx[i]*numbersx[i]
#     numbersx[i]=e
# print(numbersx)


#####tuples########
# a=("a","b","c","d","e","f")
# b=("g",)
# c=a+b
# print(a[1:])
# print(a)
# print(type(a))
# d=list(a)
# print(d)
# d[0]="helios"
# e=tuple(d)
# print(e)
########

####SETS########
# a={"a","b","c","d","e"}
# print(a)
# print(type(a))
# print(a)
# a.add("helios")
# print(a)
# b={"tumper"}
# a.update(b)
# print(a)
# a.remove("tumper")
# print(a)
# a.pop()#removes a random element
# print(a)
# a.clear()#clears all emelemnts in set
# print(a)
# del a #deletes entire set
# print(a)
####set operations########
# b={1,2,3,4}
# c={5,6,7,8,1,2}
# d=b.union(c) #combine 2 sets together.
# print(d)
# e=b.intersection(c)# prints the common elements in both sets.
# print(e)
# f=b.symmetric_difference(c)# prints the unique elements in both sets removing the common ones.
# print(f)
########Nested Dictionaries####
# a={}
# a['GFG']= {}
# print(a)
# a['GFG']["rank"]= {}
# print(a)
# a['GFG']["rank"]= 10
# print(a)
# a["MFG"]={}
# a["MFG"]["rank"]={}
# a["MFG"]["rank"]=12
# a["MFG"]["bank"]=13
# a["MFG"]["tank"]=14
# print(a)
#################


####Dictionaries####
# a = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(a)
# print(a["model"])#accesing elements ins dictionary
# print(a.get("brand"))#accesing elements ins dictionary
# print(a.keys())#prints keys in dictionary
# print(a.values())#prints values in dictionary
# #f=2
# #d="color"
# #a[d]=f# to pass arguments from variables into dict positions
# a["color"]="red"#to add items to dictionary.
# a["brand"]="Chevorlet"
# print(a)
# x=a.items()#return dict in tuple form.
# print(x)
# if "brand" in a:
#     print(True)# prints true if keys specified in dictionary exists
# a.update({"engine":"vector"})
# print(a)
# for x in a:
#   print(x)#prints all values in dictionary usng loops
# for x in a.keys():
#   print(x)#prints all keys in dictionary usng loops
# for x in a.values():
#     print(x)#prints all values in dictionary usng loops
# c=a.copy()#copies dict a to c
# print(c)
# del a["engine"]#deletes engine key in dictionary
# print(a)
# a.clear()# clears entire dictionary
# print(a)
# del a#deletes entire dictionary
# print(a)
# a=[12,1,10,13]
# a.sort()
# print(a)
# filename = "Epfo_Card.pdf"
# with open(filename) as f_obj:
#     content = f_obj.read()
#
# print(content)

# f=open("demofile.txt")
# print(f.read())

# a={"a":1,"b":2,"c":3}
# print(a.keys())
# a={"a":1,"b":2,"c":3}
# for i in a.values():
#     print(i)

# a={"a":1,"b":2,"c":3}
# a.popitem()
# print(a)

# a={"a":1,"b":2,"c":3}
# # a.update({"b":6})####update the values
# # print(a)
# # a["z"]=10
# print(a)
# a.clear()
# print(a)
# a.setdefault("z","e")
# print(a)

# a={"a":1,"b":2,"c":3}
# a1=a.get(3)
# print(a1)

# a={"a","b","c"}
# a.remove("a")######remove the sets
# print(a)

# a={"a","b","c"}
# a.clear()######remove the sets
# print(a)
# a={"a","b","c"}
# a.pop()######remove the sets
# print(a)
#
# a={"a","b","c"}
# a.add("z")######remove the sets
# print(a)

# a=["a","b","c"]
# a.sort()######remove the sets
# print(a)

# a=[1,2,3]
# # a.append(7)
# # print(a)
# a.extend([8,9])
# print(a)

# a=[1,2,3]
# a[2]=4
# print(a)


# print("hello ",end="")
# print("how are you")#$#############print without new line


# a="vidyasagar gping to native"
# b=a.strip()
# print(b)

# a="sagar"
# b=a.upper()
# print(b)


a=["a","b","b"]
a=list(dict.fromkeys(a))
print(a)