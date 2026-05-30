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


i = int(input("Enter starting Number : "))
n = int(input("Enter a ending number : "))
sum_of_prime = 0
prime_count = 0
if i<2:
    i += 1
while(i<=n):
    if i<2:
        i += 1
    count = 0
    j = 2
    while(j <= i//2):
        if(i%j == 0):
            count += 1
            break
        j += 1
    if(count == 0):
        print(i)
        sum_of_prime += i
        prime_count +=1
    i += 1
print("sum of prime is :",sum_of_prime)
print("Prime count is :",prime_count)




