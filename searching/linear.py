def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

print(linear_search([1, 2, 3, 4], 3))

assert 2 == linear_search([1, 2, 3, 4], 3)