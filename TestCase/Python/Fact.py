# a=5
# temp=1
# if(a==1):
#     print("fact is 1")
# else:
#     for i in range(1,a):
#         d=temp*(i+1)
#         temp=d
# print(temp)

# a={1,2,3,4,5,}
# a.add(7)
# print(a)
# b=a.copy()
# print(b)

# a={1,2,3,4,5,}
# a.discard(3)
# print(a)


# a=2
# b=3
# print(a,b)
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
#
#
# a=4
# for i in range(a):
#     print(i*"*")


# a="aaaabbbbccccgggggdddeeee"
# b=list(a)
# b=list(dict.fromkeys(b))
# print(b)


a=1661
b=str(a)[::-1]
if int(b)==a:
    print("its polindrome")
else:
    print("its not polindrome")