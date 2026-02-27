import bisect

def matrix_median(mat):
    n = len(mat)
    m = len(mat[0])
    
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    
    desired = (n * m) // 2
    
    while low < high:
        mid = (low + high) // 2
        
        count = 0
        for row in mat:
            count += bisect.bisect_right(row, mid)
        
        if count <= desired:
            low = mid + 1
        else:
            high = mid
    
    return low


# Example usage
mat = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

print(matrix_median(mat))
