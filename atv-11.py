# O código não está funcionando 100%

# A ideia de solução é utilizar um algoritmo guloso que, a cadad novo carro a ser carregado, tenta carregá-lo
# no lado em que houver mais espaço disponível, ou, se isso não for possível, carreega-o no lado em que houver mais
# espaço disponível, ou, se isso não for possível, carrega-o no lado oposto.
# A ideia é que, se em algum momento não for possível carregar os carros restantes, a solução será inviável.

'''
Exemplos de teste:
(1)
1
50
2500
3000
1000
1000
1500
700
800
0
'''

MAX_FERRY_LENGTH = 101 * 100
# Cada carro tem no mínimo 1 metro
MAX_CAR_CAN_LOAD = 202
cars = []
# [car][lhsLength] - o comprimento da direita será ~ carSum [car] - lhsLength
loaded_previous_to_lhs = [[False for _ in range(MAX_FERRY_LENGTH)] for _ in range(MAX_CAR_CAN_LOAD)]
# Truque de economia de espaço de soma - alternar entre duas matrizes.
can_reach_length = [[False for _ in range(MAX_FERRY_LENGTH)] for _ in range(2)]

t = int(input())
sep = ""
for _ in range(t):
    print(sep, end="")
    sep = "\n"
    cars.clear()
    can_reach_index = 0
    ferry_length = int(input()) * 100
    length_sum = 0
    num_car = 0
    previous_from = None
    possible = True
    can_reach_length[can_reach_index][0] = True
    for i in range(1, ferry_length + 1):
        can_reach_length[can_reach_index][i] = False
    while True:
        car = int(input())
        if car == 0:
            break
        if possible:
            cars.append(car)
            next_can_reach = 1 - can_reach_index
            for i in range(ferry_length + 1):
                can_reach_length[next_can_reach][i] = False
            length_sum += car
            reached_one = False
            for i in range(ferry_length + 1):
                if can_reach_length[can_reach_index][i]:
                    if i + car <= ferry_length:
                        reached_one = True
                        previous_from = i + car
                        loaded_previous_to_lhs[num_car + 1][i + car] = True
                        can_reach_length[next_can_reach][i + car] = True
                    if length_sum - i <= ferry_length and num_car != 0:
                        reached_one = True
                        previous_from = i
                        loaded_previous_to_lhs[num_car + 1][i] = False
                        can_reach_length[next_can_reach][i] = True
            possible = reached_one
            if possible:
                num_car += 1
            can_reach_index = next_can_reach
    # Reconstruct
    print(num_car)
    out = []
    lhs_size, rhs_size = 0, 0
    for _ in range(num_car):
        if loaded_previous_to_lhs[num_car][previous_from]:
            out.append("port")
            previous_from -= cars[num_car - 1]
            lhs_size += cars[num_car - 1]
        else:
            out.append("starboard")
            rhs_size += cars[num_car - 1]
        num_car -= 1
    for direction in reversed(out):
        print(direction)