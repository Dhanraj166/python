ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

index = int(input("Enter amount: "))

if index == 0:
    print("zero")

while(index):
    if index < 20: 
        print(ones[index])
        break                                
    elif(index<100):
        result = index%10
        index = index//10
        if result == 0:
            print(tens[index-1])
        else:
            print(tens[index-1], ones[result])
        break
    elif(index<1000):
        result = index%10       
        first = index//100
        index = index%100
        if(index < 20 and index != 0):
            print(ones[first], "hundred", ones[index])
        elif(index%10 == 0 and index//10 == 0):
            print(ones[first], "hundred")  
        elif(index%10 == 0):
            index = index//10
            print(ones[first], "hundred", tens[index-1])
        else:
            index = index//10
            print(ones[first], "hundred", tens[index-1], ones[result])
        break
        
        
        
        
        
        
    