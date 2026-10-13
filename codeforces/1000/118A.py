a = input()
a = a.lower()
vowels = "aeioyu"
newword = ""
for things in a:
    if things not in vowels:
      newword += "." + things
print(newword)


