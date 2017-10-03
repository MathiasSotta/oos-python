#!/usr/bin/python
# -*- encoding: utf-8 -*-

# import time
# t = time.localtime()
# #t = time.strftime("%a, %d.%m.%Y %H:%M:%S")
# print(t)


# i = 15
# print(i)
# print("\n")
#
# j = "Wiesel"
# print(j[0:5])
#
# for k in "hallo":
#     print(k)
#
# s = 'Accelerate'
# t = 'Adventure'
#
# print(s[0:3]+t[3:])

text = 'all zip files are zipped'
text2 = 'all zip files are compressed'

q = "zip"

j = str.find(text2, q)
if j:
    k = str.find(text2, q, j + 1)
    print(k)
else:
    print(j)

#############


y = 3.14159
x = 29.499999999999999


def mod(z):
    return z % 1


if mod(x) < 0.5000000000001:
    x = int(x)
else:
    x = int(x) + 1

print(x)

###############

countries = ({'country': "United States", 'capital': "Washington"},
             {'country': "Germany", 'capital': "Berlin"},
             {'country': "France", 'capital': "Paris"},
             {'country': "Spain", 'capital': "Madrid", 'language': 'spanish'},
             )

# Print out the all countries and their capital
for i in countries:
    print(i['country'] + ", " + i['capital'])
