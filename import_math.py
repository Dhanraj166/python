# import math
# math.factorial(5)
# num=int(input())
# fact=1
# if num==0:
#     print(0)
# else:
    
#     for i in range(num,0,-1):
#         fact=fact*i
#     print(fact)
num=int(input())
def factorial(num):
    fact=1
    if num==0:
        print(0)
    else:
    
        for i in range(num,0,-1):
            fact=fact*i
        print(fact)
factorial(num)
