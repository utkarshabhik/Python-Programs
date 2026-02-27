def three_way_partition(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            
        elif arr[mid] > b:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
        else:  # a <= arr[mid] <= b
            mid += 1
    
    return arr


# Example usage
arr = [1, 4, 3, 2, 5, 8, 6, 7]
a = 3
b = 6

print(three_way_partition(arr, a, b))
