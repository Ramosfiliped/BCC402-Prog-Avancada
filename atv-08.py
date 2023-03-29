# Esse problema é resolvido com algoritmo A*
# O código contém quatro funções que giram as peças do quebra-cabeça em quatro direções diferentes. 
# As funções turn_1, turn_2, turn_3 e turn_4 representam as rotações 
# no sentido horário dos quadrantes superior esquerdo, superior direito, inferior esquerdo e inferior direito, respectivamente.

def turn_1(a):
    temp_1 = a[10]
    temp_2 = a[11]
    a[2:12] = a[0:10]
    a[0] = temp_1
    a[1] = temp_2
    a[21:24] = a[9:12]
    return a

def turn_2(a):
    temp_1 = a[12]
    temp_2 = a[13]
    a[14:24] = a[12:22]
    a[22] = temp_1
    a[23] = temp_2
    a[9:12] = a[21:24]
    return a

def turn_3(a):
    temp_1 = a[0]
    temp_2 = a[1]
    a[0:10] = a[2:12]
    a[10] = temp_1
    a[11] = temp_2
    a[21:24] = a[9:12]
    return a

def turn_4(a):
    temp_1 = a[22]
    temp_2 = a[23]
    a[14:24] = a[16:26]
    a[12] = temp_1
    a[13] = temp_2
    a[9:12] = a[21:24]
    return a

def generate_first(prev, depth, cur, seq, m):
    if depth == 9:
        return
    cur_str = ''.join(cur)
    if not cur_str in m or len(m[cur_str]) > len(seq) or (len(m[cur_str]) == len(seq) and m[cur_str] > seq):
        m[cur_str] = seq
    if prev != 1:
        generate_first(3, depth + 1, turn_3(cur), '1' + seq, m)
    if prev != 2:
        generate_first(4, depth + 1, turn_4(cur), '2' + seq, m)
    if prev != 3:
        generate_first(1, depth + 1, turn_1(cur), '3' + seq, m)
    if prev != 4:
        generate_first(2, depth + 1, turn_2(cur), '4' + seq, m)

def solve(prev, depth, cur, seq, m):
    if depth == 9:
        return
    cur_str = ''.join(cur)
    if cur_str in m:
        if sol == "0" or len(sol) > len(seq) + len(m[cur_str]) or (len(m[cur_str]) == len(seq) + len(m[cur_str]) and m[cur_str] > seq):
            sol = seq + m[cur_str]
    if prev != 3:
        solve(1, depth + 1, turn_1(cur), seq + '1', m)
    if prev != 4:
        solve(2, depth + 1, turn_2(cur), seq + '2', m)
    if prev != 1:
        solve(3, depth + 1, turn_3(cur), seq + '3', m)
    if prev != 2:
        solve(4, depth + 1, turn_4(cur), seq + '4', m)

def main():
    m = {}
    c = int(input())
    generate_first(0, 0, list("034305650121078709a90121"), "", m)
    for i in range(c):
        s = ""
        for i in range(24):
            a = int(input())
            if a == 10:
                s += 'a'
            else:
                s += str(a)

        if s == "034305650121078709a90121":
            print("PUZZLE ALREADY SOLVED")
            continue
        else:
            sol = "0"
            solve(0, 0, s, "")
            if sol != "0":
                print(sol)
            else:
                print("NO SOLUTION WAS FOUND IN 16 STEPS")


main()