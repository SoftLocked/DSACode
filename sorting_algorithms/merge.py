def merge(arr, start, middle, end):
    L = arr[start:middle+1]
    R = arr[middle + 1:end+1]

    l, r, arr_pos = 0, 0, start

    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            arr[arr_pos] = L[l]
            l += 1
        else:
            arr[arr_pos] = R[r]
            r += 1
        arr_pos += 1

    while l < len(L):
        arr[arr_pos] = L[l]
        l += 1
        arr_pos += 1
    while r < len(R):
        arr[arr_pos] = R[r]
        r += 1
        arr_pos += 1

def merge_sort(arr):

    def helper(arr, start, end):

        if (end-start+1 <= 1):
            return arr

        middle = start + (end-start)//2
        helper(arr, start, middle)
        helper(arr, middle+1, end)

        merge(arr, start, middle, end)

        return arr

    return helper(arr, 0, len(arr)-1)

print(merge_sort([4, 3, 2, 1]))

assert [1, 2, 3, 4] == merge_sort([4, 3, 2, 1])
