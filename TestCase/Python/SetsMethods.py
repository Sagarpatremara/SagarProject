########SET METHODS########
# * Sets are stored to multiple items in a single variable.
# * Sets is a collection of which is unchangeble,unordered,unindexed.
# * Do not allow duplicate items
# * Sets cannot have two items with the same name
# * Duplicate value will be ignored
# * Curly brackets {}

# add()
a={1,2,3,4,5,6}
a.add(8)
print(a)

# copy()
b=a.copy()
print(b)

# difference() #
a={1,2,3,4}
b={2,3,6,5}
c=a.difference(b)    # prints elements excluding the common ones found in set b.
d=b.difference(a)    # prints elements excluding the common ones found in set a.
print(c)
print(d)

#discard()
a={1,2,3,4,"A","B"}
a.discard("A")        #Removes the element specified in the set.(It will not raise an error if element is not present)
print(a)


#remove()
b={1,2,3,4,"A","B"}
b.remove(4)        #Removes the element specified in the set.(It will raise an error if element is not present)
print(b)

#intersection
a={1,2,3,4,5,6}
b={2,3,4,9,11,12}
c=a.intersection(b)           #prints all unique elements in both the sets
print(c)

# union
a={1,2,3,4,5,6}
b={2,3,4,9,11,12}
c=a.union(b)           #prints all elements in both the sets without duplicating elements
print(c)

#update
a={1,2,3,4,5,6}
b={2,3,4,9,11,12}       #combines 2 sets together...no repeating elements allowed.
a.update(b)
print(a)

#pop()
b={2,3,4,9,11,12}       #removes first element in set.
b.pop()
print(b)

#symmetric_difference()
a={1,2,3,4,5}
b={2,3,1,8,9,10}
c=a.symmetric_difference(b)     #prints all elements excluding the common elements from both sets
print(c)

# isdisjoint()                  #checks if 2 sets are unique
a={11}
b={2,3,1,8,9,10,4,5}
c=a.isdisjoint(b)               #return false if elements in set a are present in set b
print(c)

# issubset()                    #checks if elements of one set is present in another set
a={1,2,3,4,5}
b={2,3,1,8,9,10,4}
c=a.issubset(b)               #return true if all elements of set a are present in set b
print(c)


