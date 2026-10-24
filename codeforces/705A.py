n = int(input())
feelings = []
for things in range(1, n+1):
    if things % 2 != 0:
        feelings.append("I hate")
    else:
        feelings.append("I love")
print(" that ".join(feelings) + " it")
# Even = I love
# Odd = I hate
# Base is that it.
# .join creates a list removing the list brackets from feelings making it a list.
