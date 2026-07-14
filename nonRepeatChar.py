# s = "abbcccd"

# count = {}

# for ch in s:
#     count[ch] = count.get(ch, 0) + 1
# found = False
# for ch in reversed(s):
#     if count[ch] == 1:
#         print("Last non-repeating character:", ch)
#         found = True
#         break
# if not found:
#    print("No non-repeating character found")



s = "aabbcc"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

found = False

for ch in s:
    if count[ch] == 1:
        print("First non-repeating character:", ch)
        found = True
        break

if not found:
    print("No non-repeating character found")