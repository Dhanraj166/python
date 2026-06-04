def move_zero(arr):
    result = []
    
    for i in range(len(arr)):
        if arr[i] != 0:
            result.append(arr[i])
            
    
    while len(arr) != len(result):
        result.append(0)
        
    return result

print(move_zero([1, 2, 0, 3, 0, 4]))


# ---------------------------------------------------------------------------------------------------


def move_zero(arr):

    index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1

    while index < len(arr):
        arr[index] = 0
        index += 1
        
    return arr

print(move_zero([1, 2, 0, 3, 0, 4]))