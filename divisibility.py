# # Divisible by 5: 

# n = int(input("Enter a number : "))
# digit = n%10
# print(digit%5 == 0)



# # Divisibility by 4

# n = int(input("Enter a number : "))
# digit = n%100
# print(digit%4 == 0)


# # Divisibility by 6

# no = int(input("Enter a number : "))
# total = 0
# digit = no%10
# while no>0:
#     rem = no % 10 
#     total = total + rem
#     no = no // 10
# print(total)

# if total%3 == 0 and digit%2==0:
#     print('Divisible by 6')
# else:
#     print('Not Divisible by 6')



# # Divisibility by 9

# n = int(input("Enter a number : "))
# totel = 0
# while(n>0):
#     rem = n%10
#     totel += rem
#     n = n // 10
# print(totel%9==0)
# # if(totel%9==0):
# #     print('Divisible by 9')
# # else:
# #     print('Not Divisible by 9')


# # Divisibility by 10

# n = int(input("Enter a number : "))
# print(n%10 == 0)


# Divisibility by 11

n = int(input("Enter a number : "))
temp = n//10
odd = 0
even = 0
while(n>0):
    rem = n%10
    odd = odd + rem
    n = n // 100

while(temp>0):
    rem = temp%10
    even = even + rem
    temp = temp // 100
    
if((odd-even)%11 == 0):
    print('divisibility of 11')
else:
    print('Not divisibility of 11')



# Divisibility by 11

# n = int(input("Enter a number : "))

# odd = 0
# even = 0

# while(n>0):
#     rem = n%100
#     odd = odd + rem % 10
#     even = even + rem // 10
#     n = n // 100
# print((odd-even)%11 == 0)

