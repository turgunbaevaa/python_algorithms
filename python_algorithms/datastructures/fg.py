dll = {'head': {'value': None, 'prev': None, 'next': 300}, 
       'tail': {'value': None, 'prev': 100, 'next': None}, 
       100: {'value': 'idk', 'prev': 200, 'next': 'tail'}, 
       200: {'value': 'idk', 'prev': 300, 'next': 100}, 
       300: {'value': 'idk', 'prev': 'head', 'next': 200}}
def traverse(dll):
    curr = 'head' 
    while curr != None:
        next = dll[curr]['next']
        print(curr)
        curr = next
    curr = dll['tail']['prev']
    maxnode = dll['tail']['prev']
    while curr != None:
        prev = dll[curr]['prev']
        if curr == 'head':
            break
        if curr > maxnode:
            maxnode = curr
        curr = prev
    minnode = dll['tail']['prev']
    while curr != None:
        prev = dll[curr]['prev']
        if curr == 'head':
            break
        if curr < minnode:
            minnode = curr
        curr = prev

    return maxnode, minnode

print(traverse(dll))

def get_edge(el, n1, n2):
    if (n1, n2) in el or (n2, n1) in el:
        return True
    else:
        return False

edgelist = [(1, 2), (1, 3), (2, 3), (3, 4)]

print(get_edge(edgelist, 1, 4))
