# A ideia desse algoritmo é para cada cideade com pelo menos uma estradad de saída,
# executa uma busca em profundidade (DFS) para identificar as cidades que podem ser alcançadas a partir dela.
# Se alguma cidade não foi alcançada e pertence ao mesmo componente conexo da cidade de origem,
# então a cidade de origem preisa de uma câmera de segurança

# Link: https://github.com/Zeronfinity/UVa-Solutions/blob/master/10199%20-%20Tourist%20Guide.cpp

'''
Exemplos de teste:

(1)
6
sugarloaf
maracana
copacabana
ipanema
corcovado
lapa
7
ipanema copacabana
copacabana sugarloaf
ipanema sugarloaf
maracana lapa
sugarloaf maracana
corcovado sugarloaf
lapa corcovado

(2)
5
guanabarabay
downtown
botanicgarden
colombo
sambodromo
4
guanabarabay sambodromo
downtown sambodromo
sambodromo botanicgarden
colombo sambodromo
0

'''

import sys
sys.setrecursionlimit(1000000) # aumenta o limite de recursão

n = 0
components = []
paths = []
reached = []

# Função para formar componentes conexos do grafo
def form_component(node, current_component):
    components[node] = current_component
    for i in range(len(paths[node])):
        if components[paths[node][i]] == -1:
            form_component(paths[node][i], current_component)

# Função para fazer a busca em profundidade no grafo
def search(current):
    reached[current] = True
    for i in range(len(paths[current])):
        if not reached[paths[current][i]]:
            search(paths[current][i])

t = 1
sep = ""
while True:
    n = int(input())
    if n == 0:
        break
    
    print(sep)
    sep = "\n"
    
    m = {}
    order = []
    for i in range(n):
        temp = input()
        m[temp] = i
        order.append(temp)
    
    R = int(input())
    paths = [[] for i in range(n)]
    for i in range(R):
        temp, other = input().split()
        f = m[temp]
        s = m[other]
        paths[f].append(s)
        paths[s].append(f)
    
    components = [-1] * n
    num_components = 0
    for i in range(n):
        if components[i] == -1:
            form_component(i, num_components)
            num_components += 1
    
    special = []
    reached = [False] * n
    for i in range(n):
        if len(paths[i]) == 0:
            continue
        current_component = components[i]
        for j in range(n):
            reached[j] = False
        reached[i] = True
        search(paths[i][0])
        for j in range(n):
            if not reached[j] and components[j] == current_component:
                special.append(order[i])
                break
    
    special.sort()
    print("City map #{}: {} camera(s) found".format(t, len(special)))
    for sp in special:
        print(sp)
    
    t += 1

