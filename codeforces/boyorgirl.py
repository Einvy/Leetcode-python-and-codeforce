a = list(input().lower())
count = 0
letters = []
for letter in a:
    if letter not in letters:
        letters.append(letter)
count = len(letters)
if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
