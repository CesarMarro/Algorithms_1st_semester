def insertion_sortf(arr):

    i = 1
    while i < len(arr):
        j = i 
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
    
            j = j-1
        j = 0
        i = i + 1
    i = 100
    return arr