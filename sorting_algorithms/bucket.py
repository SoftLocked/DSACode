def bucket_sort(arr):
    buckets = dict()

    for i in arr:
        if i not in buckets:
            buckets[i] = 1
        else:
            buckets[i] += 1

    j = 0
    for k, v in sorted(list(buckets.items())):
        for i in range(v):
            arr[j] = k
            j += 1

    return arr

print(bucket_sort([2,1,2,1,1,0,0]))

assert [0, 0, 1, 1, 1, 2, 2] == bucket_sort([2,1,2,1,1,0,0])