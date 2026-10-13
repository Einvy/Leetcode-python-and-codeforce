s = input()
capitalcount = 0
lowercount = 0
for letter in s:
    if letter == letter.lower():
        lowercount += 1
    elif letter == letter.upper():
        capitalcount += 1
if capitalcount > lowercount:
    print(s.upper())
else:
    print(s.lower())
