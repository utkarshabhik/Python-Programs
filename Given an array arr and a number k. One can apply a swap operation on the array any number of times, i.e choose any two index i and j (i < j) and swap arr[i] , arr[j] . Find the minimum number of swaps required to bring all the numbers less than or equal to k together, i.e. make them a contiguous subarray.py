def min_swaps_to_bring_k_together(arr, k):
    n = len(arr)
    
    # Step 1: Count elements <= k
    good = sum(1 for num in arr if num <= k)
    
    # Step 2: Count bad elements in first window
    bad = sum(1 for num in arr[:good] if num > k)
    
    min_swaps = bad
    
    # Step 3: Slide the window
    for i in range(good, n):
        
        # Remove left element from window
        if arr[i - good] > k:
            bad -= 1
            
        # Add new right element to window
        if arr[i] > k:
            bad += 1
            
        min_swaps = min(min_swaps, bad)
    
    return min_swaps


# Example usage
arr = [2, 1, 5, 6, 3]
k = 3

print(min_swaps_to_bring_k_together(arr, k))
