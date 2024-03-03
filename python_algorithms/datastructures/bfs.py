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

def opposite(el, node):
    incident = incident_edges(el, node)
    opp_nodes = []
    for x, y in incident:
        if x != node:
            opp_nodes.append(x)
        if y != node:
            opp_nodes.append(y)
    return opp_nodes

def bfs(el, start):
    explored = []
    q = [start]
    while q:
        current = q.pop(0)
        if current not in explored:
            explored.append(current)
            temp = opposite(el, current)
            for x in temp:
                q.append(x)
                print("Current node:", current, " Found node:", x, q)
    return explored



edgeList = [(1, 2), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)]
abcEdgeList = [('A', 'B'), ('A', 'E'), ('A', 'F'), ('B', 'C'), 
               ('B', 'F'), ('C', 'D'), ('C', 'G'), ('D', 'G'), 
               ('D', 'H'), ('E', 'I'), ('E', 'F'), ('F', 'I'), 
               ('G', 'J'), ('G', 'K'), ('G', 'L'), ('H', 'L'), 
               ('I', 'J'),('I', 'M'), ('I', 'N'), ('J', 'K'), 
               ('K', 'N'), ('K', 'O'), ('L', 'P'), ('M', 'N')]


print(bfs(abcEdgeList, 'A'))
print(bfs(edgeList, 5))
for node in sorted(vertices(abcEdgeList)):
    print(node, opposite(abcEdgeList, node))

print(edgeList.pop())

print(opposite(edgeList, 2))