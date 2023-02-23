def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


print(insertEnd([1, 9], 4, 6, 7))
