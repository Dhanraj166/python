def perfect(num):
    result = 0
    div = 1
    while(div<=num//2):
        if num%div == 0:
            result += div
        div += 1
    if num == result:
        return True
    return False
    
print(perfect(28))