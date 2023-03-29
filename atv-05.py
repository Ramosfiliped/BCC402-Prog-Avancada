# A função stern_brocot recebe dois argumentos, nume e deno, 
# que correspondem ao numerador e denominador da fração desejada. 
# A função inicia as variáveis a e b com os valores passados como argumentos. 
# Em seguida, define as variáveis left, right e mid como instâncias da classe Pair.

# O algoritmo começa iterando até que o par de frações mid seja igual à fração desejada, 
# representada pelos valores nume e deno. A cada iteração, a função calcula os valores v1 e v2, 
# que correspondem aos numeradores das frações obtidas somando a e b com as frações adjacentes mid e left (ou mid e right). 
# Se v1 é menor que v2, a variável right é atualizada com o valor de mid, e a fração mediantes 
# correspondente é adicionada à sequência com o caracter 'L'. 
# Caso contrário, a variável left é atualizada com o valor de mid, 
# e a fração mediantes correspondente é adicionada à sequência com o caracter 'R'.

class Pair():
    def __init__(self, fst, snd):
        self.fst = fst
        self.snd = snd
    
    def get_first(self):
        return self.fst
    
    def get_second(self):
        return self.snd


def stern_brocot(nume, deno):
    a, b = nume, deno
    res = ""
    left = Pair(0,1)
    right = Pair(1,0)
    mid = Pair(1, 1)

    while mid.get_first() != a or mid.get_second() != b:
        v1 = a * mid.get_second()
        v2 = b * mid.get_first()

        if v1 < v2:
            right = mid
            mid = Pair(left.get_first() + mid.get_first(), left.get_second() + mid.get_second())
            res += 'L'
        else:
            left = mid
            mid = Pair(mid.get_first() + right.get_first(), mid.get_second() + right.get_second())
            res += 'R'

    print(res)

stern_brocot(878, 323)