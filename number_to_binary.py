no = int(input("Enter no.: "))

if no == 0:
    binary = "0"
else:
    binary = ""
    while no > 0:
        rem = no % 2
        binary = str(rem) + binary
        no //= 2

print(binary)