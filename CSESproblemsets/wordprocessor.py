n,k = map(int,input().split())
c = input()
line = []
count = 0
# N is the total words while k is the length that it should not pass.
# So n = 10 means 10 words and k = 7 would mean that each line should be no more than 7 letters
# Might need to use a list to check how many words there are but also need to somehow access letters unless I need to do two for loops?
for word in c:
    if count + len(word) > k:
        print(" ".join(line) + "\n")
        line = []
        count = 0
    line.append(word)
    count += len(word)
print(" ".join(line) + "\n")

