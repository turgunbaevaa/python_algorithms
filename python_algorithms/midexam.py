alist = [ 4, 5, 10, 6, 1, 2]

for i in range(1, len(alist)):
    temp = alist[i]
    j = i - 1
    while j >= 0 and alist[j] > temp:
        alist[j+1] = alist[j]
        j-=1
    alist[j+1] = temp

print(alist)

for i in range(1, len(alist)):
    temp = alist[i]
    j = i - 1
    while j >= 0 and alist[j] < temp:
        alist[j + 1] = alist[j]
        j -= 1
    alist[j + 1] = temp

print(alist)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage
arr = [[5, 3, 8, 2, 1, 9, 4, 7, 6]]
sorted_arr = merge_sort(arr)
print(sorted_arr)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
if result != -1:
    print("Element", target, "found at index", result)
else:
    print("Element", target, "not found in the array.")



""" # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightR
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSmallSymmetric(a,b):
            if type(a)==TreeNode and type(b)==TreeNode:
                if a.val==b.val:
                    return isSmallSymmetric(a.left,b.right) and isSmallSymmetric(a.right,b.left)
            else:
                return a==b
        return isSmallSymmetric(root.left,root.right) """


""" listx = {
    'head': {
        'value': 2,
        'next': None,
        'prev': None
    },
    'tail': {
        'value': 5,
        'next': None,
        'prev': None
    }
}

def traverse(dll):
    curr = 'tail'
    while curr != None:
        inc = dll[curr]['value']
        node = dll[curr]['prev']
        print(inc+1)
        curr = node


print(traverse(listx)) """

""" def increment(listx):
    current_node = listx['tail']['prev']  # Start from the node before the tail
    
    while current_node != 'head':
        listx[current_node]['value'] += 1  # Increment the value of the current node
        current_node = listx[current_node]['prev']  # Move to the previous node
    
    return listx

listx = {
    'head': {'prev': None, 'next': 'n1'},
    'n1': {'prev': 'head', 'next': 'n2', 'value': 8},
    'n2': {'prev': 'n1', 'next': 'n3', 'value': 3},
    'n3': {'prev': 'n2', 'next': 'tail', 'value': 4},
    'tail': {'prev': 'n3', 'next': None}
}

print(increment(listx)) """


def count_leaves(tree, root):
    count = 0

    if root not in tree:
        print('Wrong root node')
        return count

    lc = tree[root]['L'] 
    rc = tree[root]['R']

    if lc is None and rc is None:
        count += 1
    else:
        if lc is not None:
            count += count_leaves(tree, lc)
        if rc is not None:
            count += count_leaves(tree, rc)

    return count

btree = {
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3},
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None},
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None},
    13: {'P': 10, 'L': None, 'R': None}
}

print(count_leaves(btree, 'root'))

dll = {'head': {'value': None, 'prev': None, 'next': 300}, 
       'tail': {'value': None, 'prev': 100, 'next': None}, 
       100: {'value': 'idk', 'prev': 200, 'next': 'tail'}, 
       200: {'value': 'idk', 'prev': 300, 'next': 100}, 
       300: {'value': 'idk', 'prev': 'head', 'next': 200}}

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

print(maxdll(dll))
