def union_arrays(a, b):
    union_set = set()
    
    # Add elements of first array
    for num in a:
        union_set.add(num)
    
    # Add elements of second array
    for num in b:
        union_set.add(num)
    
    return list(union_set)


# Example usage
a = [1, 2, 3, 4, 5]
b = [1, 2, 3]

print(union_arrays(a, b))
