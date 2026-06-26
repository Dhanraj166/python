str = "JavaScript makes coding fun"
longest = ""
word = ""
for ch in str:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""
print(longest)

