#Dictionary
# * Dicionary are used store key value pair
# * Tuples are ordered,changeble,and do not allow duplicates


#elf
#Simple dicionary
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
print(type(a))

#get()
a = { "brand": "Ford",
      "model": "Mustang",                   #get the perticular key value
      "year": 1964 }
b=a.get('brand')
print(b)


#keys
a = { "brand": "Ford",
      "model": "Mustang",                   #print only keys
      "year": 1964 }
b=a.keys()
print(b)

#update the values dict()
a = { "brand": "Ford",
      "model": "Mustang",                   #update the dict
      "year": 1964 }
b=a.keys()              #before the change
a["color"]="red"
print(b)                #after the vhange
print(a)


#get the values
a = { "brand": "Ford",
      "model": "Mustang",                   #print only values
      "year": 1964 }
b=a.values()
print(b)

#update the values
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
b=a.values()              #before the change
a["color"]="white"
print(b)                #after the vhange
print(a)


#print both keys and values in dict
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
b=a.items()
print(b)

#update the values
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
b=a.items()
print(b)
a["year"]=2020
print(b)

#####Update()
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
a.update({"brand":"kia"})
print(a)


#####pop()
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
a.pop("model")
print(a)


##clear()
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
a.clear()
print(a)

#copy()
a = { "brand": "Ford",
      "model": "Mustang",
      "year": 1964 }
print(a)
b=a.copy()
print(b)


#popitem
a = { "brand": "Ford",                          #remove the last
      "model": "Mustang",
      "year": 1964 }
a.popitem()
print(a)


