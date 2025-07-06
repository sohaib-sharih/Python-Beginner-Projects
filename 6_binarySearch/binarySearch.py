"""
1. Implementatioin of binary search algorithm
2. We will prove that binary search is faster than naive search
3. naive searchL scan entire list and ask if its equal to the target
if yes, return the index
if no, then return -1
"""
import random
import time

def naive_search(l, target):
    #example l = [1, 2, 3]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

l = [1, 2, 3, 4, 5, 6, 10]
target = 6
ns = naive_search(l, target)
print(ns)

"""
1. binary search uses divide and conquer!
2. we will leverage the fact that our list is sorted

"""


def binary_search(l, target, low = None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    # example l = [1, 3, 5, 10, 12] Should return 3
    midpoint = (low + high)//2 # 2

    if l[midpoint] == target:
        return midpoint
    
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint -1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))
    length = 10000
    # build a sorted list of length 10,000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive Search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary Search time: ", (end - start)/length, "seconds")
