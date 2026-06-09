# Divisible by 5: 

n = int(input("Enter a number : "))
digit = n%10
if digit%5 == 0:
    print(True)
else:
    print(False)



# Divisibility by 4

n = int(input("Enter a number : "))
digit = n%100
if digit%4 == 0:
    print(True)
else:
    print(False)


# Divisibility by 6

no = 12345
total = 0
digit = no%10
while no>0:
    rem = no % 10 
    total = total + rem
    no = no // 10
print(total)

if total%3 == 0 and digit%2==0:
    print('Divisible by 6')
else:
    print('Not Divisible by 6')



# Divisibility by 9

n = int(input("Enter a number : "))
totel = 0
while(n>0):
    rem = n%10
    totel += rem
    n = n // 10
if(totel%9==0):
    print('Divisible by 9')
else:
    print('Not Divisible by 9')


# Divisibility by 10

n = int(input("Enter a number : "))
print(n%10 == 0)