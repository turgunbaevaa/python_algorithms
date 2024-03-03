# Edge List - lis of edges
# maximum number of edges --> the number of nodes *(multiply) number of nodes - 1 divided by 2
# Data Structures for graphs
# Edge list
# Adjacency list
# Adjacency matrix

edgelist = [('u', 'v'), ('u', 'w'), ('v', 'w'), ('w', 'z')]
print(edgelist[0])

def edge_count(el):
    return len(el)

def edges(el):
    return el
#

def vertices(el):
    verts = set()
    for edge in el:
        verts.add(edge[0])
        verts.add(edge[1])
    return list(verts)

def vertex_count(el):
    return len(vertices(el))

def get_edge(el, n1, n2):
    if (n1, n2) in el or (n2, n1) in el:
        return True
    else:
        return False

def degree(el, node):
    count = 0
    for edge in el:
        if node in edge:
            count += 1
    return count
# O(n*2(it may change, cause it's number of edges))

def incident_edges(el, node):
    inc_edges = []
    for edge in el:
        if node in edge:
            inc_edges.append(edge)
    return inc_edges

def remove_vertex(el, node):
    toberemoved = incident_edges(el, node)
    for edge in toberemoved:
        el.remove(edge)
    return el

def remove_edge(el, n1, n2):
    if not get_edge(el, n1, n2):
        print("Edge not found")
        return el
    if(n1, n2) in el:
        el.remove((n1, n2))
    if(n2, n1) in el:
        el.remove((n2, n1))
    return el

def triangle(el, n1, n2, n3):
    x1 = get_edge(el, n1, n2)
    x2 = get_edge(el, n1, n3)
    x3 = get_edge(el, n2, n3)
    return x1 and x2 and x3

def path2(el, n1, n2, n3):
    x1 = get_edge(el, n1, n2)
    x2 = get_edge(el, n2, n3)
    return x1 and x2

def gpath2(el, n1, n2, n3):
    x1 = get_edge(el, n1, n2)
    x2 = get_edge(el, n2, n3)
    x3 = get_edge(el, n1, n3)
    xsum = x1+x2+x3
    if xsum>=2:
        return True
    else:
        return False

print(edge_count(edgelist))
print(edges(edgelist))
print(vertex_count(edgelist))
print("Vertices")
print(vertices(edgelist))


edgelist.append(('u','z'))
edgelist.append(('v', 'z'))
print(edgelist)
print('Get edge: ')
print(get_edge(edgelist, 'v', 'u'))
print(triangle(edgelist, 'u', 'y', 'z'))
print(path2(edgelist, 'u', 'w', 'u'))    
print(gpath2(edgelist, 'u', 'v', 'w'))
print(gpath2(edgelist, 'z', 'v', 'w'))

""" print(degree(edgelist, 'u'))
print(incident_edges(edgelist, 'z'))
print(incident_edges(edgelist, 'y'))
print(remove_vertex(edgelist, 'w'))
print(remove_edge(edgelist, 'u', 'v'))
 """








