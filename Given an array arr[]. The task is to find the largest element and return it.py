def find_largest(arr):
    if not arr:
        return None
    
    max_val = arr[0]
    
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    
    return max_val


# Example usage
arr = [10, 24, 5, 78, 1]
print(find_largest(arr))
