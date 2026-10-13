read = open("shell.in")
n = int(read.readline())

shellatpos = [i for i in range(3)]
counter = [0 for _ in range(3)]
for _ in range(n):
    a, b, g = [int(i) - 1 for i in read.readline().split()]
    shellatpos[a], shellatpos[b] = shellatpos[b], shellatpos[a]
    counter[shellatpos[g]] += 1
print(max(counter), file=open("shell.out", "w"))
