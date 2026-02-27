def is_subset(a, b):
    freq = {}
    
    # Count frequency of elements in a
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    # Check elements of b
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    
    return True


# Example usage
a = [11, 1, 13, 21, 3, 7]
b = [11, 3, 7, 1]

print(is_subset(a, b))
