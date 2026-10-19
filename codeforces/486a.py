n = int(input())
total = n // 2
if n % 2 != 0:
    total -= n
print(total)

# Idea is that each pair is 1. so n = 6 would be: (-1 + 2) + (-3 + 4) + (-5 + 6) so 1 + 1 + 1 = 3. so n // 6 is just 3 which is correct.
