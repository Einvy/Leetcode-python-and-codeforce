n,m = map(int,input().split())
required = list(map(int, input().split()))
time = 0
task = 1
for i in required:
    if i >= task:
        time += i - task
    else:
        time += n - task + i
    task = i
print(time)
