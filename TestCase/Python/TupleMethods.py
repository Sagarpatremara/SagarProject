#Tuples :
# * Tuples are stored to multiple items in a single variable
# * Tuples are ordered,Unchangeble,and allow duplicates
# * once tuple is created we cannot change its value
# * Written with round brackets

a=("sagar")
print(type(a))


#Update
a=("Sagar","Vidya","mysore","krs")
b=list(a)
print(b)
b[1]="hasan"                    #Convert the tuple into list, change the list,convert the list back into a list
a=tuple(b)
print(a)

#append()
a=("Sagar","Vidya","mysore","krs")
b=list(a)
b.append("banglore")               #add the element into tuple
a=tuple(b)
print(a)

#remove()
a=("Sagar","Vidya","mysore","krs")
b=list(a)
b.remove("Vidya")        #remove the element to tuple
a=tuple(b)
print(a)

# #del
a=("Sagar","Vidya","mysore","krs")
del a

#Unpacking tuple
a=("Sagar","Vidya","mysore","krs")
(Sagar,Vidya,mysore,krs)=a
print(Sagar)
print(Vidya)
print(mysore)


a=("Sagar","Vidya","mysore","krs")
for r in range(len(a)):
    print(r)


a=("Sagar","Vidya","mysore","krs")
for r in a:
    print(r)

#multiply tuple()
a=("Sagar","Vidya","mysore","krs")
b=a*2
print(b)

this1=("Sagar","Vidya","mysore","krs")
this2=(1,2,3)
this3= this1 + this2
print(this3)

