num=int(input())
var="no is even" if num%2==0 else"no is odd"
print(var)


def is_adult(age):
    return "Adult" if age >= 18 else "Minor"

print(is_adult(22))
print(is_adult(15))
