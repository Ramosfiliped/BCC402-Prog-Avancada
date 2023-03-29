#Não consegui fazer esse funcionar 100%

numberCanStack = [[-1]*105 for _ in range(505)]
bestTopFaceToUse = [[-1]*105 for _ in range(505)]

# Each cube, 0 and 1 pair, 2 and 3 pair, 4 and 5 pair
# so X pairs with X^1
cubes = [[-1]*6 for _ in range(505)]

def to_face(face_pos):
    # Função auxiliar para traduzir a posição da face em uma string representando a face
    faces = ["front", "back", "left", "right", "top", "bottom"]
    return faces[face_pos]

def print_out(cube, color):
    # Função para imprimir as faces de cada cubo empilhado a partir do cubo atual e da cor atual
    if cube == N:
        return
    
    if best_top_face_to_use[cube][color] == skipped:
        print_out(cube + 1, color)
    else:
        face_used = best_top_face_to_use[cube][color]
        print_out(cube + 1, cubes[cube][face_used])
        print(N - cube, to_face(face_used))
    
def num_can_stack(cube, color):
    # Função recursiva que calcula o número máximo de cubos que podem ser empilhados 
    # a partir do cubo atual e da cor atual
    if cube == N:
        return 0
    
    num = number_can_stack[cube][color]
    
    if num == -1:
        num = 0
        best_top_face = best_top_face_to_use[cube][color]
        best_top_face = skipped
        
        for face in range(6):
            if cubes[cube][face] == color:
                top_face = face ^ 1
                amount = num_can_stack(cube + 1, cubes[cube][top_face]) + 1
                
                if amount > num:
                    num = amount
                    best_top_face = top_face
        
        amount = num_can_stack(cube + 1, color)
        if amount > num:
            num = amount
            best_top_face = skipped
        
        number_can_stack[cube][color] = num
        best_top_face_to_use[cube][color] = best_top_face
    
    return num

T = 1

while True:
    N = int(input())
    if N == 0:
        break

    # Inicializa as variáveis
    skipped = 6
    number_can_stack = [[-1] * 105 for _ in range(505)]
    best_top_face_to_use = [[skipped] * 105 for _ in range(505)]
    cubes = [[0] * 6 for _ in range(505)]

    # Lê as faces dos cubos e as armazena em ordem reversa
    for cube in range(N - 1, -1, -1):
        faces = list(map(int, input().split()))
        for face in range(6):
            cubes[cube][face] = faces[face]

    best_num = 0
    best_start_cube = -1
    best_color = 0

    # Para cada combinação de cubo e face, calcula o número máximo de cubos que podem ser empilhados 
    # a partir daquela face e armazena o melhor resultado
    for cube in range(N):
        for face in range(6):
            num = num_can_stack(cube, cubes[cube][face])
            if num > best_num:
                best_num = num
                best_start_cube = cube
                best_color = cubes[cube][face]

    if T > 1:
        print()

    print("Case #{}".format(T))
    print(best_num)
    
    print_out(best_start_cube, best_color)
    
    T += 1