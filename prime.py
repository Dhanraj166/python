# Prime Number
n= int(input("Enter a number : "))
if n == 1:
    print(False)
div = 2
prime = True
while(div <= n//2):
    if(n%div == 0):
        prime = False
        break
    div+=1
print(prime)




