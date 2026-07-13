def find_lucky_brute_force(arr):
    lucky_integer = -1
    
    for i in range(len(arr)):
        count = 0
        
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if arr[i] == count:
            if arr[i] > lucky_integer:
                lucky_integer = arr[i]
                
    return lucky_integer

print(find_lucky_brute_force([2, 2, 3, 4]))        
print(find_lucky_brute_force([2, 3, 4, 3, 5, 3]))  
