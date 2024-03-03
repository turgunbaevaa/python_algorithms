# STACK
# A stack is a collection of elements that can be inserted or removed according
# to the principle last-in, first-out(LIFO)

# Elements can be inserted in any moment, but it is possiblr to access or
# remove only the last inserted element

# A stack is a Abstract data type (ADT)
#push(e) - inserts element on top of the stack
# pop() - removes the element on top of the stack and returns it.
# If the stack is empty an error is returned
# top() - returns a reference to the top element of the stack
# is_empty - Returns TRUE 

mystack = [1, 2, 3]
def is_empty(stack):
    # O(1) - big o(1) - не важно сколько элементов внутри
    if len(stack) != 0:
        return False
    else:
        return True
    #return len(stack) == 0
print(is_empty(mystack))


def length(stack):
    # O(1) - big o(1) - не важно сколько элементов внутри
    return len(stack)

print(length(mystack))

# Big O(1) - 1 is constant, independent how large your stack
def top(stack):
    if is_empty(stack):
        return -1
    else:
        return stack[0]
    
print(top(mystack))

mylist = []
mylist.insert(0, 4)
mylist.insert(0, 5)
mylist.insert(0, 7)
print(mylist) #[7, 5, 4]
print(mylist.pop(0)) # 7
print(mylist.pop(0)) # 5
print(mylist.pop(0)) # 4

def push(stack, element):
    stack.insert(0, element)
    return stack

print(mystack)
print(mystack, 10)
print(mystack, 20)
print(mystack, 30)
print(mystack, 40)

def extract(stack):
    x = stack.pop(0)
    return x

print(extract(mystack))

mystack = []
push(mystack, 4)
push(mystack, 7)
print(extract(mystack))
push(mystack, 10)
push(mystack, 8)
print(extract(mystack))

print(mystack)

# Computational cost 
# is_empty = 



