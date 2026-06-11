# Prime Number
# n= int(input("Enter a number : "))
# if n == 1:
#     print(False)
# div = 2
# prime = True
# while(div <= n//2):
#     if(n%div == 0):
#         prime = False
#         break
#     div+=1
# print(prime)



# i = int(input("Enter starting Number : "))
# n = int(input("Enter a ending number : "))
# sum_of_prime = 0
# prime_count = 0
# if i<2:
#     i =2
# while(i<=n):
    
#     count = 0
#     j = 2
#     while(j <= i//2):
#         if(i%j == 0):
#             count += 1
#             break
#         j += 1
#     if(count == 0):
#         print(i)
#         sum_of_prime += i
#         prime_count +=1
#     i += 1
# print("sum of prime is :",sum_of_prime)
# print("Prime count is :",prime_count)



#  Write the smallest and the biggest two digit prime number.

n = 10
first = 0
last = 0
while(n<100):
    count = 0
    div = 2
    while(div<=n//2):
        if(n%div == 0):
            count += 1
            break
        div += 1
    if(count == 0):
        if(first == 0):
            first = n
        last = n
    n += 1

print("Smallest two digit prime number is ", first)
print("biggest two digit prime number is ", last)



