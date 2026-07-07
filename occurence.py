input = 'a1b2c3'
#output: abbcccddd

output = ''
for x in input:
    if x.isalpha():
        output = output + x
        previous = x
    else:
        no = int(x)
        z = chr(ord(previous)+1)
        output = output + z*no
print(output)