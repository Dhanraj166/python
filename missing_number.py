# def missing(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] + 1 != arr[i + 1]:
#             return arr[i] + 1

# print(missing([1, 2, 3, 5]))


def missing(arr):
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] != 1:
            return arr[i] + 1

print(missing([1, 2, 3, 5]))
