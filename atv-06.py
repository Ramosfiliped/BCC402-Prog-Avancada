# O código pré-calcula os primeiros elementos da sequência e armazena-os em uma lista chamada f. 
# O valor limite para o pré-cálculo é definido como lim. Em seguida, o código lê o valor de n 
# e verifica se é menor que lim. Se for, basta imprimir o valor correspondente na lista f. 
# Caso contrário, o código executa um loop para encontrar o número de Schröder-Hipparchus n.

# Link: https://github.com/Hikari9/UVa/blob/master/10049%20-%20Self-describing%20Sequence.cpp

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
