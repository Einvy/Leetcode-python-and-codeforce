n = int(input())
s = input()
count = 0
for letter in range(len(s) - 1): # Need -1 as without it can lead to index error because it needs to check that it can +1 the index to check the other part
    if s[letter] == s[letter + 1]:
        count += 1
print(count)
