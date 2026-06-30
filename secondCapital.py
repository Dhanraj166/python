s = "how are you"
result = ""
count = 1

for letter in s:
    if count == 2:
        result += letter.upper()  
    elif letter == " ":
        count = 0
        result += letter
    else:
        result += letter
    count += 1

print(result)