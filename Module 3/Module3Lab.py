def qsorter(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) //2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]
    
    return qsorter(left) + mid + qsorter(right)

print( qsorter( [2,1,1,0] ) )