def insertion_sort(arr):
    for i in range(len(arr)):
        j = i-1
        while j >= 0 and arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr

assert [1, 2, 3, 4] == insertion_sort([4, 3, 2, 1])