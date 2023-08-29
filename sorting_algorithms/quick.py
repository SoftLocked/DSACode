def quick_sort(arr):

    def helper(arr, s, e):
        if (e-s+1 <= 1):
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1

        arr[e], arr[left] = arr[left], pivot

        helper(arr, s, left-1)
        helper(arr, left+1, e)

        return arr

    return helper(arr, 0, len(arr)-1)

print(quick_sort([4, 3, 2, 1]))

assert [1, 2, 3, 4] == quick_sort([4, 3, 2, 1])