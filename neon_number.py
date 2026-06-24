n = 9
squre = n * n
totel = 0
while squre>0:
    totel = (totel*10) + (squre%10)
    squre = squre // 10
    print(totel)
if totel == n:
    print("Neon Number")
else:
    print("Not Neon Number")
    

    