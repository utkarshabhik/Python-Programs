def minimize_height_difference(arr, k):
    n = len(arr)
    
    if n == 1:
        return 0
    
    arr.sort()
    
    ans = arr[-1] - arr[0]
    
    small = arr[0] + k
    big = arr[-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(n - 1):
        
        subtract = arr[i + 1] - k
        add = arr[i] + k
        
        if subtract < 0:
            continue
        
        new_min = min(small, subtract)
        new_max = max(big, add)
        
        ans = min(ans, new_max - new_min)
    
    return ans


# Example usage
arr = [1, 5, 8, 10]
k = 2

print(minimize_height_difference(arr, k))
