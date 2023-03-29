# A função extendedEuclid é chamada para encontrar os valores x, y e d que 
# satisfazem a equação diofantina linear n1x + n2y = d. 
# Se v não for divisível por d, a saída é "failed". Caso contrário, a solução é 
# calculada usando x, y, n1, n2, c1, c2 e v, e a saída é a solução que minimiza 
# a função objetivo c1x + c2y, dentro do intervalo [lowerbound, upperbound], 
# onde lowerbound e upperbound são calculados com base nas restrições do problema. 
# Se não houver solução dentro desse intervalo, a saída é "failed".

# Link: https://github.com/KHvic/uva-online-judge/blob/master/10090-Marbles.cpp

import math

def extendedEuclid(a, b):
    global x, y, d
    if b == 0:
        x = 1
        y = 0
        d = a
        return
    extendedEuclid(b, a % b)
    y1 = x - (a // b) * y
    x = y
    y = y1

while True:
    v = int(input())
    if v == 0:
        break
    c1, n1, c2, n2 = map(int, input().split())
    extendedEuclid(n1, n2)
    if v % d != 0:
        print("failed")
    else:
        x *= v // d
        y *= v // d
        n2 //= d
        n1 //= d
        lowerbound = math.ceil(-(x / n2))
        upperbound = math.floor(y / n1)
        if lowerbound <= upperbound:
            res1 = c1 * (x + n2 * lowerbound) + c2 * (y - n1 * lowerbound)
            res2 = c1 * (x + n2 * upperbound) + c2 * (y - n1 * upperbound)
            if res1 < res2:
                print(x + n2 * lowerbound, y - n1 * lowerbound)
            else:
                print(x + n2 * upperbound, y - n1 * upperbound)
        else:
            print("failed")