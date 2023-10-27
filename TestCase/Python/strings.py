#Strings()
#enclosed withon the double quotes

#slicing()
a="hello world"
print(a[2:5])

a="hello world"
print(a[:3])

a="hello world"
print(a[2:])

a="hello world"
print(a[-5:-2])

a="hello world"
print(a.upper())

a="HEELO WORLD"
print(a.lower())

#strip()
a="hello world"
print(a.strip())

#split()
a="hellow world"
print(a.split())


a="hello world"
print(a.replace("h","ppppp"))

#Add()
a=4
b=6
c=a+b
print(a+b)

#cancate
a="4"
b="6"
print(a+b)

#format()
a=45
b="my age is {}"
print(b.format(a))


#Format()
a="sagar"
b="BE"
c="Krs"
d="My name is {} i studies {} from {}"
print(d.format(a,b,c))


a="sagar"
b="BE"
c="Krs"
d="My name is {} i \studies\ {} from {}"
print(d.format(a,b,c))

