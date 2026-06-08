count = 0
n = 2
total = 0

while count < 5:
    i = 1
    divisors = 0

    while i <= n:
        if n % i == 0:
            divisors += 1
        i += 1

    if divisors == 2:
        print(n)
        total += n
        count += 1

    n += 1

print("Sum of first 5 prime numbers:", total)
