text = "My Favourite Cricketer is Dhoni, Rohit and Kolhi"
key = "Rohit"
present = False
length = len(text)

for i in range(0, length- len(key) + 1):
    if(text[i:i+len(key)] == key):
        present = True
        break
if(present):
    print("present")
else:
    print("Not present")

