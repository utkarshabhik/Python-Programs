def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Step 1: Sort by starting time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    merged.append(intervals[0])
    
    for i in range(1, len(intervals)):
        last = merged[-1]
        current = intervals[i]
        
        # Check overlap
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged


# Example usage
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))
