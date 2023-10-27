# List
# -------------
# * List are stored to multiple items in a single variable
# * Lists are ordered,changeble,and allow duplicates
# * List items are indexed te first items are indexed [0]
# * List items are can be edited and used any data type
# * square brackets[]

#len
a=["banana"]
print(len(a))       #find the len one string is 1 index

b="sagar"       # this is string comman functions not in the list
print(len(b))

a=["banana","apple","orange","grapes"]
a=a[1]                      # List items are indexed
print(a)

a=["banana","apple","orange","grapes"]
a=a[-1]                      # List items are indexed its negative index
print(a)

a=["banana","apple","orange","grapes"]
a=a[1:3]                      # Range of indexed where to start and where to end
print(a)

a=["banana","apple","orange","grapes"]
a=a[:3]                      # Range of indexed where to start and where to end
print(a)

a=["banana","apple","orange","grapes"]
a=a[1:]                      # Range of indexed where to start and where to end
print(a)
# #
a=["v","i","d","y","a","s","a","g","a","r"]
a[3]="G"                      #to change the value speciific items
print(a)

# # #Insert
a=["v","i","d","y","a","s","a","g","a","r"]
a.insert(1,"Devops")                #insert the element in to perticular index list
print(a)

# # #Append
a=["v","i","d","y","a","s","a","g","a","r"]
a.append("devops")              # Add the element into end of the list
print(a)

# # #Extend
a=["v","i","d","y","a","s","a","g","a","r"]
b=["KRS"]
a.extend(b)             # extend the element
print(a)

# # #remove
a=["v","i","d","y","a","s","a","g","a","r"]
a.remove("r")            # remove the element from list
print(a)

# # #pop()
a=["v","i","d","y","a","s","a","g","a","r"]
a.pop(0)           # remove the specified index
print(a)

# #del
a=["v","i","d","y","a","s","a","g","a","r"]
del a         # delete entir list

# #clear()
a=["v","i","d","y","a","s","a","g","a","r"]
a.clear()          #   remove the specified index
print(a)

# #loop method
a=["v","i","d","y","a","s","a","g","a","r"]
for i in a:
    print(a)

# #copy()
a=["v","i","d","y","a","s","a","g","a","r"]
print(a)
b=a.copy()            # copy from one list to another list
print(b)

# #sort()
a=["v","i","d","y","a","s","a","g","a","r"]
a.sort()           # sorting the list alphanumerically
print(a)

#reverce
a=["v","i","d","y","a","s","a","g","a","r"]
a.reverse()           # revrce the order of the list
print(a)

#joining two sets
a=["v","i","d","y","a","s","a","g","a","r"]
b=[1,2,3,4,5,6,7,8,9]
c=a+b
print(c)

