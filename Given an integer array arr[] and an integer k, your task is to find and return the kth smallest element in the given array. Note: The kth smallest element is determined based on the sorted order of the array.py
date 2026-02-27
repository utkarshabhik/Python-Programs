import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(middle))


def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        return None
    return quickselect(arr, k)


# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3

print(kth_smallest(arr, k))
