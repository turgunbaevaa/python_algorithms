import random
import math
"""
print(random.random())  #in the range 0 - 1
print(random.randint(1, 1000))  #in the range we want

for i in range(20):  
    print(random.randint(1, 6))

print("While loop: ")
i = 0
list1 = []
while i < 20:
    random_num = random.randint(1, 6)
    i += 1
    list1 = random_num
    print(random_num)



#function to count random list given number 
mylist = []
for i in range(20):  
    mylist.append(random.randint(1, 6))
print(mylist)


mylist = []
for i in range(600000):  
    mylist.append(random.randint(1, 6))
print(mylist)

def count_num(xlist, number):
    count = 0
    for i in range(len(xlist)):
        if xlist[i] == number:
            count += 1
    return count

print(count_num(mylist, 1))

def newcount(xlist):
    count = 0
    for i in range(len(xlist)):
        if xlist[i] <= 3:
            count += 1
    return count

print(newcount(mylist))



mylist = []
for i in range(20):  
    mylist.append(random.randint(1, 6))
print(mylist)

i = len(mylist) - 1
while i >= 0:
    print(mylist[i], end=' ')
    i -= 1


for i in range(len(mylist)-1, -1, -1):
    print(i, mylist[i])
   

mylist = []
for i in range(20):  
    mylist.append(random.randint(1, 30))
print(mylist)

print(" Even elements of the list ")

for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        print(mylist[i], end=" ")

print(" \nOdd elements of the list ")

for i in range(len(mylist)):
    if mylist[i] % 2 != 0:
        print(mylist[i], end=" ")

print(" \nEven indecies of the list ")

for i in range(0, len(mylist), 2):
    print(mylist[i], end=" ")

print(" \nOdd indecies of the list ")

for i in range(1, len(mylist), 2):
    print(mylist[i], end=" ")


mylist = []
while len(mylist) < 20:
    x = random.randint(1, 300)
    if x not in mylist:
        mylist.append(x)
print(mylist)



mylist = []
while len(mylist) < 20:
    x = random.randint(1, 40)
    if x not in mylist and x % 2 == 0:
        mylist.append(x)
    #print(x, mylist)
print(mylist)
print(sorted(mylist))


mylist = []
for i in range(20):
      mylist.append(0)
print()

for i in range(20):
      if i % 2 != 0:
            mylist[i] = 1
print(mylist)

def increasing_list(start, n):
    result = []
    for i in range(n):
        result.append(start + i)
    return result

print(increasing_list(100, 10))

def decreasing_list(start, n):
    result = []
    for i in range(n):
        result.append(start - i)
    return result

print(decreasing_list(100, 10))

s1 = 'Good morning' #sequence of characters is a string
print(s1[0], s1[3])


phonebook1 = ['Ann', 'Bob', 'Charlie']
phonebook2 = ['1234', '354762', '874528']
for i in range(len(phonebook1)):
    print(phonebook1[i], phonebook2[i])



my_phonebook = {'Bob': '3527653421', 'Ann': '3216573456', 'Charlie': '3516755467'}
my_dict = {1: [10, 20, 30], 2: [40, 50, 60], 3: [70, 80, 90]}
print(my_dict[2])
print(len(my_dict)) #len of the dict is 3
print(my_dict[1][2]) #here I acces to the value of the list
my_dict[1][2] = 40
print(my_dict)  #here I change data/value
for element in my_dict:
   print(element, my_dict[element])
   #output: 1 [10, 20, 40]
          # 2 [40, 50, 60]
          # 3 [70, 80, 90]

#print(my_phonebook['Charlie'])
#print(my_phonebook.keys())
#print(my_phonebook.values())
#my_phonebook['Alice'] = ['3516573564']
#print(my_phonebook)

#here we print keys
for x in my_phonebook:
    print(my_phonebook[x])

#here we print values
for x in my_phonebook:
    print(x)

#here also values
for x in my_phonebook.keys():
  print(x)



dict1 = {'John': 20, 'Alice': 24, 'Kate': 25}
for i in dict1:
    print(i, dict1[i])

mydict = {
          'John': ['Simon', 20, 1.65], 
          'Elizabeth': ['Bennet', 18, 1.63], 
          'Charles': ['Bingley', 25, 1.75]
          }

for i in mydict:
    print(i, mydict[i])

print(mydict['John'][0])


mydict = {
             'John': { 'surname': 'Simon', 'age': 20},
             'Elizabeth': {'surname': 'Bennet', 'age': 20, 'height': 1.65},           
             'Charles': {'surname': 'Bingley', 'age': 25, 'height': 1.75}
          }

for i in mydict:
    #print(i, mydict[i])
    print(i, mydict[i]['surname'])


################################
#### #count how many times each letter contained in a given string
#not good solution

occ = [0] * 26
x = 'hello'

ab = list("abcdefghijklmnopqrstuvwxyz ")
abstring = "abcdefghijklmnopqrstuvwxyz "
print(ab, len(ab))

for i in range(len(x)):
    print(ord(x[i]), ord(x[i]) - ord('a'))

for i in range(len(abstring)):
    print(abstring[i], ord(abstring[i]), ord(abstring[i]) - ord('a'))


for i in range(len(x)):
    position = ord(x[i]) - ord('a')
    occ[position] += 1
print(occ)

largeocc = [0] * 256
x = 'Hello world!'
for i in range(len(x)):
    position = ord(x[i]) - ord('a')
    largeocc[position] += 1
print(largeocc)

#################################



#count how many times each letter contained in a given string
x = '"Hello world!", said Katie to Alice 2 times.'
occdict = {}
for i in range(len(x)):
    if x[i] not in occdict:
        occdict[x[i]] = 1
    else:
        occdict[x[i]] += 1
print(occdict)


user_dict = {}
user_str = input("Input character: ")
for i in range(len(user_str)):
    if user_str[i] not in user_dict:
        user_dict[user_str[i]] = 1
    else:
        user_dict[user_str[i]] += 1
print(user_dict)


occdict = {}
x = 'helloworld'
occdict = {}
for i in range(len(x)):
    if x[i] not in occdict:
        occdict[x[i]] = 1
    else:
        occdict[x[i]] += 1
print(occdict)
print(occdict.get('x', 0))
print(occdict.get('o', 0))


secretstring = 'Good morning Algorithms'
occdict = {}
for i in range(len(secretstring)):
    if secretstring[i] not in occdict:
        occdict[secretstring[i]] = 1
    else:
        occdict[secretstring[i]] += 1
print(occdict)

while True:
    userchar = input("Guess a character contained in the secret string: ")
    if occdict.get(userchar, 0) >= 1:
        print("Found")
        break
    else:
        print("Try again")



#reverse lookup

occdict = {}
x = 'helloworld'
occdict = {}
for i in range(len(x)):
    if x[i] not in occdict:
        occdict[x[i]] = 1
    else:
        occdict[x[i]] += 1
print(occdict)

v = int(input("Enter value to find keys: "))
for key in occdict:
    if occdict[key] == v:
        print(key, occdict[key])


#implemented a program with unique values - разбери

x = 'good afternoon everybody'
occdict = {}
for i in range(len(x)):
    if x[i] not in occdict:
        occdict[x[i]] = 1
    else:
        occdict[x[i]] += 1
print(occdict)

for k in occdict:
    print(k, occdict[k])

print(occdict.get('o', 0))

value = 4
result = []
for key in occdict:
    if occdict[key] == value:
        result.append(key)
print(result)

result2 = {}
uniquevalues = []
values = list(occdict.values())
print(values)
for val in values:
    if val not in uniquevalues:
        uniquevalues.append(val)
print(uniquevalues)

for val in uniquevalues:
    for key in occdict:
        if occdict[key] == val:
            if val in result2:
                result2[val].append(key)
            else:
                result2[val] = [key]
        print(val, '\t', key, '\t', result2.get(val, []))
print(result2)


#implement python function that creates a list of 20 random integer values in the range 1-10. 
# Create second list that contains only the unique values of the first list

new_list = []
mylist = []
for i in range(20):  
    mylist.append(random.randint(1, 10))
print(mylist)

for i in mylist:
    if i not in new_list:
        new_list.append(i)
    #print(i, new_list)
print(new_list)

#implement  a python program that creates a dictionary whose keys are the university id numbers of some fictitious students. 
# The corresponding value is a dictionary having as keys the strings 'name'and 'surname' and corresponding values are 
# the names and surnames of fictious students

student_info ={
    '45362':{"name": 'Bob', 'surname': 'Rocker'},
    '56942':{"name": 'Ann', 'surname': 'William'},
    '64538':{"name": 'Katie', 'surname': 'Bennet'},
    '63542':{"name": 'Bernard', 'surname': 'Smith'}
    }
print(student_info)

for key in student_info:
    name = student_info[key]['name']
    surname = student_info[key]['surname']
    print(key, name, surname)

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # make None as the default value for next.


def count_nodes(head):
    # assuming that head != None
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count


nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print("This linked list's length is: (should print 5)")
print(count_nodes(nodeA))









