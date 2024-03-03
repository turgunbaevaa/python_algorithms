# first-in first-out FIFO
# A collection of elements that canbe inserted or removed according to the principle
# Elements can be inserted in any moment, but it is possible to access or remove only
#  the first element inserted
def is_empty(queue):
    if len(queue) != 0:
        return False
    else:
        return True
    #return len(queue) == 0

def length(queue):
    return len(queue)

def top(queue):
    if is_empty(queue):
        return -1
    else:
        return queue[0]
    
def insert(queue, element):
    queue.append(element)
    return queue
myqueue = [] 
insert(myqueue, 10)
insert(myqueue, 20)
insert(myqueue, 30)
insert(myqueue, 40)
print(myqueue)

def extract(queue):
    x = queue.pop(0)
    return x

print(extract(myqueue))
print(myqueue)

myqueue2 = []
mystack = []

def push(stack, element):
    stack.insert(0, element)
    return stack

insert(myqueue2, 5)
insert(myqueue2, 7)
insert(myqueue2, 9)
insert(myqueue2, 10)
print(myqueue2)
# it works only for small number of elements
x1 = extract(myqueue2)
push(mystack, x1)
x2 = extract(myqueue2)
push(mystack, x2)
x3 = extract(myqueue2)
push(mystack, x3)
x4 = extract(myqueue2)
push(mystack, x4)
print(myqueue2)
print(mystack)


def queue2stack(queue, stack):
    for i in range(length(queue)):
        x = extract(queue)
        push(stack, x)
    return stack
myqueue3 = [1, 2, 4, 7, 9]
mystack3 = []
print(myqueue3)
print(queue2stack(myqueue3, mystack3))

#Use while loop and is_empty function

my_queue = []
def insert(queue, x):
    queue.append(x)
    return queue

insert(my_queue, 10)
insert(my_queue, 5)
insert(my_queue, 4)
insert(my_queue, 6)
insert(my_queue, 7)
print(my_queue)

temp = []
while not is_empty(my_queue):
    temp.append(extract(my_queue))
print(temp)

insert(my_queue, temp[2])
insert(my_queue, temp[1])
insert(my_queue, temp[0])
insert(my_queue, temp[3])
insert(my_queue, temp[4])
print(my_queue)


