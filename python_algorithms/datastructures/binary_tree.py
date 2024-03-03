import random
tree = {
    'book':{'parent': None , 'left': 'chapter 1', 'right': 'chapter 2'}
}
print(tree['book'])
print(tree['book']['parent'])
print(tree['book']['left'])
print(tree['book']['right'])

tree['chapter 1'] = {'parent': 'book', 'left': 'section 1.1', 'right': 'section 1.2'}
tree['chapter 2'] = {'parent': 'book', 'left': 'section 2.1', 'right': 'section 2.2'}
tree['section 1.1'] = {'parent': 'chapter 1', 'left': None, 'right': None} #lowermost children
tree['section 1.2'] = {'parent': 'chapter 1', 'left': None, 'right': None}
tree['section 2.1'] = {'parent': 'chapter 2', 'left': None, 'right': None}
tree['section 2.2'] = {'parent': 'chapter 2', 'left': None, 'right': None}
tree['sub 1.2.1'] = {'parent': 'section 1.2', 'left': None, 'right': None}
tree['sub 1.2.2'] = {'parent': 'section 1.2', 'left': None, 'right': None}
tree['section 1.2'] = {'parent': 'chapter 1', 'left': 'sub 1.2.1', 'right': 'sub 1.2.2'}

for k,v in tree.items():
    print(k,v)

def create(btree, root):
    btree[root] = {'parent': None, 'left': None, 'right': None}

def add_node(btree, node, parent, side):
    # node: the node we want to create
    # parent: the node we want the new node to be appended
    # side: values ('left', 'righ')
    if parent not in btree:
        print('Wrong parent node')
        return False
    if btree[parent][side] != None:
        print('Wrong side')
        return False
    btree[node] = {'parent': parent, 'left': None, 'right': None}
    btree[parent][side] = node

def addnodes(tree, parent, leftnode, rightnode):
    if tree[parent]['left'] == None and tree[parent]['right'] == None:
        tree[leftnode] = {'parent': parent, 'left': None, 'right': None}
        tree[rightnode] = {'parent': parent, 'left': None, 'right': None}
        tree[parent]['left'] = leftnode
        tree[parent]['right'] = rightnode

tree2 = {}
create(tree2, 'I am root')
add_node(tree2, 'leftchild', 'I am root', 'left')
add_node(tree2, 'rightchild', 'I am root', 'right' )

tree3 = {}
add_node(tree2, 'rightchild', 20, 30)

for k, v in tree2.items():
    print(k,v)

""" def left(tree, node):
    if node not in tree:
        print('Wrong node')
        return None
    p = tree[node]['parent']
    if p == None:
        print(node, ' is the main root')
    else:
        lc = tree[p]['left']
        rc = tree[p]['right']
        if node == lc:
            print(node, ' is the left child of the ', p)
            return True
        elif node == rc:
            print(node, ' is the right child of the ', p)
            return False
        else:
            print('Something wrong')
            return False
        
print(left(tree, 'section 1.2')) """


def leftchild(tree, node):
    if node not in tree:
        print('Wrong node')
        return False
    #return tree[node]['left'] != None
    if tree[node]['left'] != None:
        return True
    else:
        return False
    

print(leftchild(tree, 'section 2.2'))


def are_siblings(tree, node1, node2):
    if node1 and node2 not in tree:
        print('Wrong node(s)')
        return False
    if tree[node1]['parent'] == tree[node2]['parent'] :
        return True
    else:
        return False

print(are_siblings(tree, 'section 1.1','section 2.2' ))

mytree = {}
create(mytree, 'root')
add_node(mytree, 'n1', 'root', 'left')
add_node(mytree, 'n2', 'root', 'right')
add_node(mytree, 'n11', 'n1', 'left')
add_node(mytree, 'n12', 'n1', 'right')
add_node(mytree, 'n21', 'n2', 'left')
add_node(mytree, 'n22', 'n2', 'right')

add_node(mytree, 'n221', 'n22', 'left')
add_node(mytree, 'n222', 'n22', 'right')
add_node(mytree, 'n111', 'n11', 'left')


for k, v in mytree.items():
    print(k,v)

def twochildnodes(tree, node):
    if node not in tree:
        print('Wrong node(s)')
        return False
    if tree[node]['left'] and tree[node]['right'] != None :
        return True
    else:
        return False

print(twochildnodes(mytree, 'n11'))

# breadth first traversal search
# inorder, postorder traversal

def bfs(tree, node):
    queue = []
    visited = []
    if node in tree:
        queue.append(node)
    else:
        print('Wrong node')
        return visited
    while queue:
        current = queue.pop(0)
        visited.append(current)
        print(current, queue)
        lc = tree[current]['left']
        rc = tree[current]['right']
        if lc:
            queue.append(lc)
        if rc:
            queue.append(rc)
    return visited

print(bfs(mytree, 'root'))

mylist = []
for i in range(10):
    y = random.randint(1, 50)
    if y not in mylist:
        mylist.append(y)
print(mylist)


btree = {}
create(btree, 35)
add_node(btree, 31, 35, 'left')
add_node(btree, 45, 31, 'right')
add_node(btree, 8, 31, 'left')
add_node(btree, 15, 45, 'right')
add_node(btree, 46, 45, 'left')
add_node(btree, 28, 8, 'right')
add_node(btree, 21, 8, 'left')
add_node(btree, 33, 15, 'right')
add_node(btree, 36, 15, 'left')

for k, v in btree.items():
    print(k,v)

def bfsmax(tree, node):
    queue = []
    visited = []
    if node in tree:
        queue.append(node)
    else:
        print('Wrong node')
        return visited
    xmax = node
    while queue:
        current = queue.pop(0)
        visited.append(current)
        if current > xmax:
            xmax = current
        print(current, xmax)
        lc = tree[current]['left']
        rc = tree[current]['right']
        if lc:
            queue.append(lc)
        if rc:
            queue.append(rc)
    return xmax

print(btree, 35)


















