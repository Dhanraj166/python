for i in range(1,20):
     if i%2==0:

          print("jump",i)
     elif i%5==0:
          continue
     elif i%7==0:
          break
     else:
          print("backward",i)

