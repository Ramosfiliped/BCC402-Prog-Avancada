# A ideia é determinar o valor limite para x, que é a largura do retângulo
# e é igual ao menor valor entre a largura e o comprimento dividido por 2
# Em seguida, o código determina o valor mínimo de x entre os picos retornados pela função peak_pair

# Link: https://github.com/Hikari9/UVa/blob/master/10215%20-%20The%20Largest%20Smallest%20Box....cpp

'''
Exemplos de teste:
(1)
1 1

(2)
2 2

(3)
3 3
'''

import math
# calcula as coordenadas de dois picos da função que representa a quantidade de água acumulada no telhado
def peak_pair(w, l):
    root = math.sqrt(w * w + l * l - w * l)
    return (((w + l) - root) / 6.0, ((w + l) + root) / 6.0)

while True:
    try:
        l, w = map(float, input().split())
    except EOFError:
        break

    peaks = peak_pair(w, l)
    limit = min(w / 2, l / 2)
    min_x = limit if limit < peaks[1] else peaks[1]

    print("{:.3f} {:.3f} {:.3f}".format(peaks[0], 0.000, min_x + 1e-7))