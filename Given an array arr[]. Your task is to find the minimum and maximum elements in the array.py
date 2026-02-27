def find_min_max(arr):
    if not arr:
        return None
    
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return min_val, max_val


# Example usage
arr = [3, 5, 1, 8, 2]
print(find_min_max(arr))
