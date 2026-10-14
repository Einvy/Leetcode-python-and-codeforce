s = input()
word = "hello"
count = 0
for letters in s:
    if letters == word[count]:
        count += 1
    if count == len(word):
        break
if count == len(word):
    print("YES")
else:
    print("NO")



# In this one the order does not have to be next to each other so h can be at count 0 and then e could be at count 2. 
# Once count is length of hello it will break as hello as been found and does not need to continue loop





