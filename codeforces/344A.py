n = int(input())
count = []
for _ in range(n):
    count.append(input())
val = 1
for i in range(1, n):
    if count[i] != count[i - 1]:
        val += 1
print(val)
