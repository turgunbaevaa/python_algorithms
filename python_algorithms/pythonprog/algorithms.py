#insertion sort
import random
# Python program for implementation of Insertion Sort
"""


# Function to do insertion sort
def insertionSort(arr):
	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
				print(arr)
		arr[j + 1] = key
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

# This code is contributed by Mohit Kumra
def InsertionSort(a):	
    for j in range(1, len(a)):
        key = a[j]
        i = j
        while i > 0 and a[i-1] > key:
            a[i] = a[i-1]
            i = i-1
            a[i] = key
            print(a)
    return a

arr = [6, 5, 4, 3, 2, 1]
print(InsertionSort(arr))
#output:  [1, 2, 3, 4, 5, 6]


#linear algoritm
#n log_2 n

def InsertionSort(a):	
    for j in range(1, len(a)):
        key = a[j] #тут будет элемент из листа
        i = j
        while i > 0 and a[i-1] < key: #чтобы вывести как decreasing, нужно
            # чтобы предыдущий был меньше чем элемент листа, нужно пройтись по этому листу n-1 раз
            a[i] = a[i-1] #i это индекс
            i = i-1
            a[i] = key
            # вот тут нужно разобраться, ещё есть математическая формула
            print(a)
    return a

arr = [1, 6, 3, 4, 5, 2]
print(InsertionSort(arr))
#output: [6, 5, 4, 3, 2, 1]


#разделяй и властвуй divide and conquer (merge sort)
#binary tree
#recuirsive approach
#divide, compare, combine --> main part 
def merge(s1, s2, s):	#s1, s2 - sublists, s = result sublist
    i = j = 0
    while i+j < len(s):
        if j == len(s2) or (i<len(s1) and s1[i]<s2[j]):
            print("Inside if: ", i, j)
            s[i+j] = s1[i]
            i+=1
        else:
            print("Inside else: ", i, j)
            s[i+j] = s2[j]
            j+=1

def mergesort(s):
    n = len(s)
    if n< 2:
        return
    mid = n//2
    s1 = s[0:mid]
    s2 = s[mid:n]
    print("Before: ", s1, s2, s)
    mergesort(s1)
    mergesort(s2)
    merge(s1, s2, s)
    print(s1, s2, s)

arr = [85, 24, 63, 45, 17, 31, 96, 50]

print(mergesort(arr))

#complexity of the algorithm is n log
#the number of divisions is  n lg_2*n = изучи



# Growth of Functions -- 12.04.2023
# O-notation
# c g(n) f(n) --> f(n) = O(g(n)) --> n can be integer, for values of n larger than n 0 there is a funtion
#  whisch stays about the other -- c g(n). For all values of n > 0, then we may say f is below of O(g(n))
# f(n) represents of computational complexity of algorithm --> how many operations required to complete the task

# Recursion - Factorial number n!=n*(n-1)
# 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1) #recursion

n = int(input("Enter a number: "))
print(factorial(n)) # Computational complexity is big O(n)



# Binary search
# 

n = int(input("Enter the length of the list: "))

data = []
while len(data) < n:
    x = random.randint(1, 30)
    if x not in data:
        data.append(x)
print(sorted(data))

def binarysearch(data, target, low, high):
    if low > high:
        return False
    mid = (low + high)//2
    if data[mid] == target:
        return True
    elif target < data[mid]:
        return binarysearch(data, target, low, mid-1)
    else:
        return binarysearch(data, target, mid+1, high)
    
print(binarysearch(data, 2, 0, len(data)-1)) 

def ifact(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total

print(ifact(10000))

"""











