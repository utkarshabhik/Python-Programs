def find_median(arr):
    n = len(arr)
    
    if n == 0:
        return None
    
    arr.sort()
    
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Example usage
arr = [7, 1, 3, 4, 5, 6, 2]
print(find_median(arr))
