import random
import math

def myunion(set1, set2):
    result = set()
    for x in set1:
        result.add(x)
    for x in set2:
        result.add(x)
    return result

print(myunion({1, 2, 3, 9, 6}, {8, 7, 5, 4}))

set1 = {1, 2, 3, 9, 6}
set2 = {8, 7, 5, 4, 2}

print(set1.intersection(set2))

def myintersection(set1, set2):
    result = set()  
    for x in set1:
        if x in set2:
            result.add(x)   
    return result

print(myintersection({1, 2, 3, 9, 7, 6},{8, 7, 5, 4, 2} ))


def mydifference(set1, set2):
    result = set()  
    for x in set1:
        if x not in set2:
            result.add(x)
    return result

print(mydifference({1, 2, 3, 4, 5, 6},{1, 2, 3, 5} ))






