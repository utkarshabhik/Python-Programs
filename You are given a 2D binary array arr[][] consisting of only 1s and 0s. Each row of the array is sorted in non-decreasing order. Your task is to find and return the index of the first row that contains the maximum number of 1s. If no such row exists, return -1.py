def row_with_max_ones(arr):
    if not arr or not arr[0]:
        return -1
    
    n = len(arr)
    m = len(arr[0])
    
    row = 0
    col = m - 1
    max_row_index = -1
    
    while row < n and col >= 0:
        if arr[row][col] == 1:
            max_row_index = row
            col -= 1
        else:
            row += 1
    
    return max_row_index


# Example usage
arr = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

print(row_with_max_ones(arr))
