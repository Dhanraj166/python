num = int(input("Enter a Number : "))

totel = 0

while(num > 0):
    totel = num%10 + totel
    num = num//10

print(f"The of sum digits is {totel}") 