s = input()
count = 0
for vals in s:
    if vals == "4" or vals == "7":
        count += 1
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
