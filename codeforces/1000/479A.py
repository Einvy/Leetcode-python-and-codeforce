a = int(input())
b = int(input())
c = int(input())
possible = [
    a + b + c,
    a * b * c,
    a + b * c,
    a * b + c,
    (a + b) * c,
    a * (b + c)]
print(max(possible))
