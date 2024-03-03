import math
""""

x = 2
y = 1

result = x / (x+y) + (x+y)/(y*y+2*x)

print(result)


pi = 3.14159
print(360/(2*pi))
print(360/2/pi)

number = 144
a = math.sqrt(number)
print(a)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Your name is {name}")
print(f"Your age is {age}")
print(type(age))

def loop(x):
    for i in x:
        print(i)

my_subjects = ["Calculus", "OOP", "Algoithms and Data Stuctures", "Physics"]
my_numbers = [1, 2, 4, 5, 6, 7, 8]
loop(my_subjects)
loop(my_numbers)

def function1(radius):
    area = math.pi*radius*radius
    print("The radius of the circle is: ", radius)
    return area

area_circle = function1(2)
print("The area of the circle is: ", area_circle)


def rect(w, h):
    result = w*h
    return result

area = rect(4,5)
print("Area of the rectangle is: ", area)


def square(a):
    square1 = a*a
    perimeter = 4*a
    return square1, perimeter

x = square(4)
print(x)


def volume(side):
    cube_volume = side**3
    print("The side of the cobe is ", side)
    return cube_volume

side = int(input("Enter Volume side: "))
y = volume(side)
print("Volume of the cube is ", y) 

print(math.pow(5, 3))

def paralellepiped(height, length, width):
    result = width*length*height
    return result

print(paralellepiped(2, 4, 5))


def convert(a):
    minute = a // 60
    print(minute, " minutes")
    second = a % 60
    print(second, " seconds")
    return minute, second

x = int(input("Enter seconds: "))
print(convert(x))


password = input("Input your password: ")

if len(password) >=8 and len(password)<=12:
    print("Password is valid")
else:
    print("Password is not valid")

password2 = "mykitggfdd"
result = len(password2) >= 8 and len(password2) <= 12
print(result)


x = int(input("Enter the number: "))

if x % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

z = int(input("Enter 1st number to check: "))
y = int(input("Enter 2nd number to check: "))

if z < y:
    print("z less than y")
elif z > y:
    print("z greater than y")
else:
    print("z equal to y")

a = 1
b = 3
c = 2
delta = b**2-4*a*c
if delta>0:
    root = math.sqrt(delta)
    x1 = (-b - root)/2/a
    x2 = (-b + root)/2/a
    print(x1, x2)
elif delta == 0:
    x = -b/2*a
    print("x=", x)
else:
    print("no solution")


char1 = input("Enter a vowel: ")
if char1 == 'a' or char1 == 'A':
    print(f"You entered {char1}")
elif char1 == 'e' or char1 == 'E':
    print(f"You entered {char1}")
elif char1 == 'o' or char1 == 'O':
    print(f"You entered {char1}")
elif char1 == 'i' or char1 == 'I':
    print(f"You entered {char1}")
elif char1 == 'u' or char1 == 'U':
    print(f"You entered {char1}")
else:
    print("You entered not a vowel")


char2 = input("Enter a vowel: ")

if (char2 == 'a' or char2 == 'e') or (char2 == 'i' or char2 == 'o') or char2 == 'u':
    print(f"You entered {char2}")
elif (char2 == 'A' or char2 == 'E') or (char2 == 'I' or char2 == 'O') or char2 == 'U':
    print(f"You entered {char2}")
else:
    print("You entered not a vowel")


vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
word = input('Enter a vowel: ')

if word in vowels:
    print(f"You entered {word}")
else:
    print("You entered not a vowel")


secret = 37
guess = 0

while guess != secret:
    guess = int(input("Enter a number: "))
    print("You entered ", guess)
print("YEEES")



def factorial(n):
    total = 1
    while n>0:
        total = total * n
        n = n - 1
        print("Current values: ", total, n)
    return total

num = int(input("Enter a number: "))
f = factorial(num)
print("Factorial of ", num, " is", f)



def altsum(n):
    total = 0
    while n > 0:
        if n % 3 == 0:
            total = total + n
        n = n - 1
        print("Current values: ", total, n)
    return total

print(altsum(20))


n = int(input("Enter a number: "))
while n > 0:
    print(n**2) 
    n = n-1



i = int(input("Enter num: "))
while i < 10:
    print(i, i**2)
    i += 1  #i = i + 1
print("After while loop")


secret = 45
while True:
    x = int(input("Guess the secret num: "))
    if x != secret:
        print("You failed! Try again!")
    else:
        print("You guess it!")
        break
print("The end!")



secret = 45
while True:
    x = int(input("Enter the secret number: "))
    if x < secret:
        print("Entered number is small than the secret number")
    elif x > secret:
        print("Entered nu,ber is greater than secret number")
    else: 
        print("You guess it!")
        break
print("The end")


def countdown(n):
    while n > 0:
        print(n)
        n -=1
    print("Via!")

print(countdown(10))


def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
            
    print(n)

print(sequence(5))  #I didn't understand this line of code


i = "Hello world!"
def onlyeven(sx):
    i = 0
    while i < len(sx):
        #if i % 2 == 0:
        print(i, sx[i])
        i += 2

print(onlyeven(i))


def greekpi(eps):
    i = 0
    mypi = 0
    while abs(mypi - math.pi) > eps:
        mypi += 4 * math.pow(-1, i)/(2 * i + 1)
        print(i, mypi, abs(mypi - math.pi))
        i += 1

print(greekpi(0.2))


string = "\nI wandered lonely as a cloud"
i = 0
print("While loop: ")

while  i < len(string):
    letter = string[i]
    print(letter)
    i += 1

print("\nFor loop: ")
for i in range(len(string)):    
    print(string[i])



for i in range(0, -20, -3):
    print(i)



sent = "Hello everyone"
for i in range(len(sent)):
    if i % 2 != 0:
        print(sent[i])

print(sent[::-1])
sent = sent[0].lower()+sent[1:]
print(sent)

sent = sent[:len(sent)-1] + 'x'
print(sent)

for i in range(10):
    sum = sum + i
print(sum)

sum = 0
while True:
    num = input("Input numbers: ")
    if num == 'stop':
        print("Done")
        break
    else:
        sum = sum + int(num)
print(sum)


max_num = float('-inf')
min_num = float('inf')

while True:
    num = input("Input a number (type 'stop' to quit): ")
    if num == 'stop':
        print("Done")
        break
    else:
        num = int(num)
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num


print("The maximum number entered was:", max_num)
print("The minimum number entered was:", min_num)


i = 2
sum = 0
for i in range(2, 101):
    if i % 2 == 0:
        sum = sum + i
    i += 1
print(sum)

while  i <= 100:
    sum += i
    i += 2
print(sum)

sum = 0
i = 1        
while  i <= 101:
    sum += i
    i += 2
    print(i, sum)
print(sum)


word = input("Enter a string: ")
print(word[1])


sum = 0
count = 0
while True:
    num = input("Input numbers: ")
    count += 1
    if num == 'stop':
        print("Done")
        break
    else:
        sum = sum + int(num)
        average = sum / int(count)
print(sum)
print(average)

for i in range(len(list)):
    print(i, list[i])

list = [1, 4, 5, 67, 8, 2, 10, 76]
i = 0
while i < len(list):
    print(i, list[i])
    i += 1    
    
print(type(empty_list))
empty_list.append(78)
print(empty_list)
empty_list.append(7)
print(empty_list)
empty_list.append(0)
print(empty_list)

empty_list = []

while True:
    num = input("Input numbers: ")
    if num == 'stop':
        print("Done")
        break
    else:
        empty_list.append(int(num))
print(empty_list)
print(type(empty_list))    



def my_list():
    empty_list = []
    while True:
        num = input("Input numbers: ")
        if num == 'stop':
            print("Done")
            break
        else:
            empty_list.append(int(num))
    return(empty_list)

print(my_list())


my_list = []

while True:
    num = input("Input numbers: ")
    if num == 'stop':
        print("Done")
        break
    else:
        my_list.append(int(num))
print(my_list)

sum = 0
i = 0

while i < len(my_list):
    sum += my_list[i]
    i += 1
    
print(sum)

def average(my_list):
    sum = 0
    i = 0
    while i < len(my_list):
        sum += my_list[i]
        i += 1
    return sum / len(my_list)

print(average(my_list))


list1 = [10, 20, 30]
list2 = [4, 45.67, 12, 20]

list3 = ['hello', 40, 123.45, True, [1, 2, 3, 4]]

print(list3[0][2])
print(list3[-1][-1])

for i in range(len(list3)):
    print(list3[i])

i = 0
while i < len(list3):
    print(list3[i])
    i += 1


    
list4 = [[2, 3], [4, 5], [4, 8]]
for i in range(len(list4)):
    sum = 0
    inner = list4[i]
    for j in range(len(inner)):
        sum += inner[j]
    print(inner, list4[i], sum)

for i in range(len(list4)):
    sum = 0
    for j in range(len(list4[i])):
        sum += list4[i][j]
    print(sum)

#inner loop can be applied for any number inside the list/element

list5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] 
for i in range(len(list5)):
    sum = 0
    for j in range(len(list5[i])):
        sum += list5[i][j]
    print(list5[i], sum)


string_list = ['hello', 'bye', 'ok', 'goodbye']

for i in range(len(string_list)):
    inner = string_list[i]
    for j in range(len(inner)):
        print(inner[j], inner[j].upper())

for i in range(len(string_list)):
    inner = len(string_list[i])
    print(string_list[i], inner)
    


def list_multiply(mylist, n):
    xlist = []
    for i in range(len(mylist)):
        xlist.append(mylist[i]*n)
    return xlist 
    
print(list_multiply([10, 20, 30], 4))

"""








