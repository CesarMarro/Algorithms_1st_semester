def linear_search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return i
    return -1