num=int(input())
num1=int(num/2)
var=True
for i in range(1,num1):   
    if num%i==0:
        var=False
        break 
if var:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")