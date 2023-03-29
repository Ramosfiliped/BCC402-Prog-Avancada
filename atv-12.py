# Este programa cria vetores de números para representar as somas de quadrados, 
# cubos e quartas potências de inteiros positivos, 
# bem como as diferenças entre as somas de quadrados, 
# cubos e quartas potências e as somas de todas as potências menores.

'''
Exemplos de teste:
(1)
1

(2)
2

(3)
3
'''

s2vec = [0]
r2vec = [0]
s3vec = [0]
r3vec = [0]
s4vec = [0]
r4vec = [0]

for i in range(1, 101):
    # Adiciona um cubo i*i em um quadrado 3*3,
    # existem (i-1)^2 quadrados bidimencionais e (i-2)^2 cubos tridimensionais

    s2 = s2vec[-1] + i*i
    s3 = s3vec[-1] + i*i*i
    s4 = s4vec[-1] + (i*i*i*i)
    # cubo/quadrado total na k-ésima dimensão é potência da série aritmética
    # 1*(1+2+3) + 2*(1+2+3) + 3*(1+2+3)
    r2 = pow((i*(i+1))//2, 2) - s2
    r3 = pow((i*(i+1))//2, 3) - s3
    r4 = pow((i*(i+1))//2, 4) - s4
    s2vec.append(s2)
    s3vec.append(s3)
    s4vec.append(s4)
    r2vec.append(r2)
    r3vec.append(r3)
    r4vec.append(r4)

while True:
    try:
        n = int(input())
        print(s2vec[n], r2vec[n], s3vec[n], r3vec[n], s4vec[n], r4vec[n])
    except:
        break