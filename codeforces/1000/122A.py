n = int(input())
count = 0

numbers = [4,7,44,474,477,47,74,77,447,444,747,744,774,777]

for vals in numbers:
    if n % vals == 0:
        count += 1
if n % 4 == 0 or n % 7 == 0:
    print("YES")
elif count > 0:
    print("YES")
else:
    print("NO")
