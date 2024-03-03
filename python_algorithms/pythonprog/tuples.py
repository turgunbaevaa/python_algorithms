import math
import random
#a tuple is a sequence of values, they can be any type and they are immutable
#we can not change 1 item in a string, like 'hello' to 'Hello'
"""
s1 = 'hello'
print(id(s1))
s1 = 'H' + s1[1:]
print(s1)
print(id(s1))

#TUPLES

mytuple = (10, 20, 30, 'hello', 'morning')
print(mytuple)
print(type(mytuple))
print(id(mytuple))
print(mytuple[3])

#tuple object does not support item assignment, so you can using LIST
mylist = list(mytuple)
mylist[2] = 300
mytuple = tuple(mylist)
print(mytuple)

#you can insert like this
mytuple = (10, 20, 30, 'hello', 'morning')
mytuple = mytuple[:2] + (300,) + mytuple[3:] #comma is used to inform python that here is a tuple, not int
print(mytuple)
print(type(mytuple))

y = (200)
print(y, type(y)) #200 <class 'int'>

y = (200,)
print(y, type(y)) #(200,) <class 'tuple'>

mytuple2 = tuple([20, 30, 40, 50])
mytuple3 = 'hello'
print(mytuple2) #(20, 30, 40, 50)
print(mytuple3)

#we use it in functions when we return more values

def rectangle(b, h):
    area = b*h
    peri = 2*(b+h)
    return area, peri

values = rectangle(20, 6)
print(values, type(values)) #(120, 52) <class 'tuple'>
print(values[0], values[1]) #120 52

a1, a2 = rectangle(20, 6)
print(a1) #120
print(a2) #52
print(a1, a2, type(a1), type(a2)) #120 52 <class 'int'> <class 'int'>

mytuple = (10, 20, 30, 'hello', 'morning')

for i in range(len(mytuple)):
    print(mytuple[i], end=' ')


#implment the function sphere(radius) that returns a tuple containing the area of a circle with radius, 
# the length of the circle and the volume of the sphere. Assign the returned values to 3 distinct variables
# Remember, that A = pi*radiusˆ2, L = 2*pi*radius, V = 4/3*pi*rˆ3

def sphere(radius):
    pi = math.pi
    area = pi*radius*radius
    length = 2*pi*radius
    volume = 4/3*pi*radius**3
    return area, length, volume

area, length, volume = sphere(3)
print(area, length, volume)

x = 10
y = 20
x, y = y, x
print(x, y)

mydict = {10: [2, 5], 24:[2, 3]}
for x in mydict.items():
    print(x)

#output (10, [2, 5])
#       (24, [2, 3])

for k, v in mydict.items():
    print(k, v)

#Output 10 [2, 5]
#       
# 24 [2, 3]



#Implement program that:
# - creates a dictionary having numeric keys and whose correponding  values are lists 
# containing two elements(the first key), three element(the second key) and four (the third key)
# - sum of the items in dict

mydict = {10: [2, 5], 24:[2, 3, 4], 30:[3, 6, 7, 8]}
for x, y in mydict.items():
    sum = 0
    for k in y:
        sum += k
    print(x, y, sum)


#Implement a function that creates a list containing 5 random integer numbers in range(1, 5)
# Use the locations of the list as keys of the dictionary. The corresponding value of each key is a list 
# containing as many random integer numbers as expressed by the value of the list
# 3. 

mylist = []
for i in range(5):  
    mylist.append(random.randint(1, 5))
print(mylist)

mydict = {}
for i in range(len(mylist)):
    mydict[i] = []
    for j in range(mylist[i]):
        mydict[i].append(random.randint(1, 20))
    print(i, j, mydict[i])

for x, y in mydict.items():
    sum = 0
    for k in y:
        sum += k
    print(x, y, sum)


t = divmod(11, 3)
print(t)  #(3, 2) division result and remainder 
quotient, remainder = divmod(11, 3)
print(quotient) #3
print(remainder) #2

a = [('a', 97), ('b', 98), ('c', 99), ('d', 100)]
for letter, num in a:
    print(letter, num)

#for x in a:
    #print(x)

for letter, num in a:
    print(letter)


#implement a program that prints a list containing all the tiples formed by orderly 
# joining together the letters of the alphabet and the corresponding ASCII 

result = []
start = 97
end = 122

for i in range(start, end+1): 
  result.append((chr(i), i))
print(result)

print("'''''''''''''''")
#reverse way
for i in range(end, start-1, -1): 
  result.append((chr(i), i))
print(result)



s1 = set()
s1.add(10)
s1.add('a')
print(type(s1), s1)
result = []

for i in range(20):
    result.append(random.randint(1, 10))

print(result)
print(set(result))

uniqueresult = []
for i in result:
    if i not in uniqueresult:
        uniqueresult.append(i)
print(uniqueresult) 



mystring = ('Ag companies have integrated drones, machine learning, AI, and automation into their everyday operations, all with the aim of helping farmers save time, money, and labor.')
mydict = {}
#calculate the frequency of the letters occuring in a string using set
for x in mystring:
    mydict[x] = 0
print(mydict)


first_set = {'red', 'white'}
second_set = {'red', 'white', 'green'}
third_set = {'red', 'white', 'blue'}

if first_set.issubset(second):
    print("Subset")
if second_set == third:
    print("The same colors")
if first_set != third:
    print("Not the same colors")
"""
myset = {'red', 'white', 'green', 'yellow', 'blue'}
mysubset = {'red', 'white', 'blue'}

def mypropersubet(myset, mysubset):
    if mysubset == set():
        return False
    if mysubset == myset:
        return False
    if mysubset.issubset(myset):
        return True
print(mypropersubet(myset, mysubset))













