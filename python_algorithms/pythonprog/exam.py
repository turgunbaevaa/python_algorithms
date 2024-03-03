import random
""""

#Implement the Python function <code>replace(stringx)</code> that returns the argument 
#string with allvowels replaced by an underscore. 
#For example, <code>replace('hello')</code> will return 'h_ll_'.

def replace(stringx):
    vowels = 'aeouiAEOUI'
    result = ''
    for char in stringx:
        if char in vowels:
            result += '_'
        else:
            result += char
    return result

print(replace("Aruuke"))


### Implement the Python function <code>vowelposition(stringx)</code>
#  that returns a list containing the position of the vowels of the given string.
#  For example: <code>vowelposition('hello')</code> will return <code>[1, 4]</code>.

def vowelposition(stringx):
    vowels = 'aeouiAEOUI'
    result = []
    for i in range(len(stringx)):
        if stringx[i] in vowels:
            result.append(i)
    return result

print(vowelposition('Hello'))


### Implement the Python function <code>myrange(listx)</code> that returns the
#  range (namely, the difference between the largest and the smallest) of the
#  elements of the argument list. Test the function using a list filled with distinct
#  random integer numbers.


mylist=[]
for i in range(20):
    mylist.append(random.randint(1, 200))
print(mylist)

def myrange(listx):
    min = listx[0]
    max = listx[0]
    result = 0
    for i in listx:
        if i > max:
            max = i
        elif i < min:
            min = i
    result = max - min
    print(max, min)
    return(result)
print(myrange(mylist))   

#### Implement the Python function <code>average(listx)</code> that
#  returns the average value of the elements of the argument list.
#  Test the function using a list filled with dstinct random integer numbers.

mylist2=[]
for i in range(10):
    mylist2.append(random.randint(1, 20))
print(mylist2)

def  average(listx):
    result = 0
    sum = 0
    for i in range(len(listx)):
        sum = listx[i] + sum
        result = sum/len(listx)
    return result

print(average(mylist2))

### Implement the Python function <code>altsum(listx)</code> that returns
#  the alternating sum of all elements in the argument list. For example,
#  given the list <code>listx = [1,4,9,10,5]</code> it computes <code>1-4+9-10+5</code>
#  and returns the results.

mylist3=[]
for i in range(10):
    mylist3.append(random.randint(1, 20))
print(mylist3)

def altsum(listx):
    result = 0
    for i in listx:
        if i % 2 != 0:
            result += +i 
        else:
            result += -i 
    return result

print(altsum(mylist3))


#. A number a is power of b if it is divisible by b and if a/b is a power of b.
#  Write a function named power(a,b) which requires two arguments (a and b) and returns
#  True if a is a power of b.

#Write the recursive function product(n) which requires an
#integer number n as argument and returns its product with all
#natural numbers that precede it. For example, product(4) must return 24 = 4 · 3 · 2 · 1


mylist = [1, 4, 5, 6, 7]

def myreduce(xlist):
    sum = 0
    for i in range(len(xlist)):
        sum = xlist[i] + sum
    return sum

print(myreduce(mylist))

mylist = [2, 4, 5, 6, 7]

def mymap(a):
    result = 0
    xlist = []
    for i in range(len(a)):
        result = a[i] ** 2
        xlist.append(result)
    return xlist

print(mymap(mylist))

def myfilter(a):
    xlist = []
    result = 0
    for i in range(len(a)):
        if a[i] % 2 !=0:
            result = a[i] **2
            xlist.append(result)
        else:
            xlist.append(a[i])
    return xlist

print(myfilter(mylist))
 
mylist = [1, 2, 3, 4, 5]
def multlist(a):
    result = 1
    for i in a:
        result = result * i
    return result

print(multlist(mylist))

mylist = []
for x in range(20):
    x = random.randint(1, 300)
    if x not in mylist:
        mylist.append(x)
print(mylist)


phonebook1 = ['Ann', 'Bob', 'Charlie']
phonebook2 = ['1234', '354762', '874528']
for i in range(len(phonebook1)):
    print(phonebook1[i], phonebook2[i])

mydict = {
             'John': { 'surname': 'Simon', 'age': 20},
             'Elizabeth': {'surname': 'Bennet', 'age': 20, 'height': 1.65},           
             'Charles': {'surname': 'Bingley', 'age': 25, 'height': 1.75}
          }

for i in mydict:
    #print(i, mydict[i])
    print(i, mydict[i]['surname'])

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

occdict = {}
x = 'helloworld'
occdict = {}
for i in range(len(x)):
    if x[i] not in occdict:
        occdict[x[i]] = 1
    else:
        occdict[x[i]] += 1
print(occdict)


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



x='good morning'
occdict={}
def lookup(x):
    for i in x:
        if i not in occdict:
            occdict[i]=1
        else:
            occdict[i]+=1
    return occdict
print(lookup(x))

x = int(input("Enter key: "))
dict2 = {1: ['f', 's'], 2: ['d', 'ds']}
print(dict2[x])

def replace(stringx):
    vowels = 'aeouiAEOUI'
    result = ''
    for char in stringx:
        if char in vowels:
            result += ''
        else:
            result += char
    return result

print(replace("Helloworld"))

user_dict = {}
user_str = input("Input character: ")
for i in range(len(user_str)):
    if user_str[i] not in user_dict:
        user_dict[user_str[i]] = 1
    else:
        user_dict[user_str[i]] += 1
print(user_dict)

x = input("Enter a srting: ")
x = list(x)
for i in range(len(x)):
    position = ord(x[i]) - ord('a')
    occ[position] += 1
print(occ)


#test result
dict1 = {10: ['here', 'I', 'am'], 20: ['Good', 'morning']}
x = input("Enter integer: ")
print(dict1.get(x, 'Unknown'))

mylist = []

while True:
    x = input("Enter a word: ")
    if x == 'stop':
        break
    mylist.append(x)
for word in mylist:
    print(len(word))

for i in range(len(mylist)):
    print(i, mylist[i], len(mylist[i]))

mystring = input("Input words separated: ")
mylist = mystring.split()
for x in mylist:
    print(x, len(mylist))

vowels = 'aeiuoAEIOU'
sentence = input('Enter a sentence: ')
result = ''

for x in sentence:
    if x not in vowels:
        result+= x
print(result)


a = [3, 7, 9, 12]
b = []

for x in a:
    b.append(x*x)
print(b)




dict1 = {10: ' goodbye', 20: ' so long'}
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
print(dict1.get(x, ' Wrong') + dict1.get(y, ' Wrong'))

mydict = {}
mystring = input('Enter a word: ')
for x in mystring:
    mydict[x] = ord(x)
print(mydict)

"""
list1 = [1, 2, 3]
listt2 = list1
list1.append(4)
print(list1, listt2)

dict1 = {'name': 'John', 'age': 30}
print(dict1.get('gender', 'Unknown'))
# dict[key] = value - create a new key value pair


dict2 = {'Ann': {'age': 20, 'height': 166}, 'Bob':{'age': 20, 'height': 156}}

x = input('Enter a string: ')
y = dict2.get(x, 'Unknown')
if y != 'Unknown':
    print(y.get('age', 'Wrong'))
