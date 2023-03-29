lim = 673368
f = [1, 1, 2, 2]
sz = 4

for i in range(3, lim):
    for j in range(f[i]):
        if sz >= lim:
            break
        f.append(i)
        sz += 1

while True:
    n = int(input())
    if n == 0:
        break
    if n < lim:
        print(f[n])
        continue
    x = 3
    cur = 4
    bound = 6
    while bound + x * f[x] < n:
        bound += x * f[x]
        cur += f[x]
        x += 1
    print(cur + (n - bound) // x)
