x = int(input())
bac = 0

while x > 0:
    if x % 2 != 0:
        bac += 1
        x -= 1
    else:
        x //= 2
print(bac)
