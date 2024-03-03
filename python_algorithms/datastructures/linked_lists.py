# https://www.geeksforgeeks.org/data-structures/linked-list/
'''
list1 = {}
list1['Hanna'] = {'value': None, 'prev': None, 'next': 'Tanya'}
list1['Tanya'] = {'value': None, 'prev': 'Hanna', 'next': None}
list1['Ann'] = {'value': 1234, 'prev': 'Hanna', 'next': 'Tanya'}

list1['Hanna']['next'] = 'Ann'
list1['Tanya']['prev'] = 'Ann'

print(list1)

list2 = {}
list2['Hanna'] = {'value': None, 'prev': None, 'next': 'Alice'}
list2['Alice'] = {'value': '12345', 'prev': 'Hanna', 'next': 'Bob'}
list2['Bob'] = {'value': '2345', 'prev': 'Alice', 'next': 'Tanya'}
list2['Tanya'] = {'value': None, 'prev': 'Bob', 'next': None}

print(list2)
'''
def create(double_list):
    double_list['head'] = {'value': None, 'prev': None, 'next': 'tail'}
    double_list['tail'] = {'value': None, 'prev': 'head', 'next': None}
    return double_list

def insert(double_list, node, value, left, right):
    double_list[node] = {'value': value, 'prev': left, 'next': right}
    double_list[left]['next'] = node
    double_list[right]['prev'] = node
    return double_list


double_list1 = {}
print(create(double_list1))
insert(double_list1, 'Dean', '35463', 'head', 'tail')
print(double_list1)
insert(double_list1, 'Alice', '65245', 'head', 'tail')
insert(double_list1, 'Dean', '35463', 'Alice', 'tail')
insert(double_list1, 'Fred', '5672', 'Dean', 'tail' )
for k, v in double_list1.items():
    print(k, v)

def create(dll):
    dll['head'] = {'value': None, 'prev': None, 'next': 'tail'}
    dll['tail'] = {'value': None, 'prev': 'head', 'next': None}
    return dll

def insert(dll, node, value, left, right):
    dll[node] = {'value': value, 'prev': left, 'next': right}
    dll[left]['next'] = node
    dll[right]['prev'] = node
    return dll

def traverse(dll):
    curr = 'head' 
    while curr != None:
        next = dll[curr]['next']
        print(curr)
        curr = next

def remove(dll, node):
    #before node1 <=> node <=> node2
    #after node1 <=> node2
    left = dll[node]['prev']
    right = dll[node]['next']
    dll[left]['next'] = right
    dll[right]['prev'] = left
    del dll[node]

def maxdll(dll):
    curr = dll['tail']['prev']
    maxnode = dll['tail']['prev']
    while curr != None:
        prev = dll[curr]['prev']
        if curr == 'head':
            break
        if curr > maxnode:
            maxnode = curr
        curr = prev
    return maxnode

mll1 = {}
create(mll1)
print(mll1)
insert(mll1, 'hello', 'world', 'head', 'tail')
insert(mll1, 'hi', 'everybody', 'hello', 'tail')
for k, v in mll1.items():
    print(k, v)

traverse(mll1)

myll2 = {}
create(myll2)
insert(myll2, 'data', 'structures', 'head', 'tail')
insert(myll2, 'random', 'numbers', 'data', 'tail')
insert(myll2, 'some', 'instructions', 'random', 'tail')
for k, v in myll2.items():
    print(k, v)

traverse(myll2)
remove(myll2, 'data')

for k, v in myll2.items():
    print(k, v)

traverse(myll2)

myll3 = {}
create(myll3)
insert(myll3, 100,  'idk', 'head', 'tail')
insert(myll3, 200, 'idk', 'head', 100)
insert(myll3, 300, 'idk', 'head', 200)
print(myll3)

def count_dll(dll):
    count_dll=0
    for node in dll:
        if node!='head' and node!='tail':
            count_dll+=1
    return count_dll

print(count_dll(myll3))

def insert_queue(dll, node, value):
    left = dll['tail']['prev']
    dll[node] = {'value': value, 'prev': left, 'next': 'tail'}
    dll[left]['next'] = node
    dll['tail']['prev'] = node
    return dll

dll_as_a_queue = {}
create(dll_as_a_queue)
insert_queue(dll_as_a_queue, 100, 'hello')
insert_queue(dll_as_a_queue, 200, 'goodbye')
insert_queue(dll_as_a_queue, 300, 'Finally')

print(traverse(dll_as_a_queue))


def remove_queue(dll):
    #before head <=> node1 <=> node2
    #after head <=> node2
    node1 = dll['head']['next']
    node2 = dll[node1]['next']
    dll['head']['next'] = node2
    dll[node2]['prev'] = 'head'
    del dll[node1]
    return node1

remove_queue(dll_as_a_queue)
traverse(dll_as_a_queue)









