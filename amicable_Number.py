no1 = 220 
no2 = 284

sum_no1 = 0
sum_no2 = 0
div = 1
while(div <= no1//2):
    if no1%div == 0:
        sum_no1 += div
    div += 1
div = 1
while(div <= no2//2):
    if no2%div == 0:
        sum_no2 += div
    div += 1

if (no1 == sum_no2 and no2 == sum_no1):
    print("The numbers are Amicable Numbers")
else:
    print("The numbers are not Amicable Numbers")
