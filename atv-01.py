# https://www.geeksforgeeks.org/check-if-any-king-is-unsafe-on-the-chessboard-or-not/

#Função para checar se algum rei está sob ataque
def checkBoard(board):
    # Acha a posição dos dois reis
    for i in range(8):
        for j in range(8):
            # Procura alguma peça que pode atacar o rei branco
            if board[i][j] == 'k':
               
                # Cavalo
                if lookForn(board, 'N', i, j):
                    return 1
 
                # Peão
                if lookForp(board, 'P', i, j):
                    return 1
 
                # Torre
                if lookForr(board, 'R', i, j):
                    return 1
 
                # Bispo
                if lookForb(board, 'B', i, j):
                    return 1
 
                # Rainha
                if lookForq(board, 'Q', i, j):
                    return 1
 
                # Rei
                if lookFork(board, 'K', i, j):
                    return 1
 
            # Procura alguma peça que pode atacar o rei preto
            if board[i][j] == 'K':
                # Cavalo
                if lookForn(board, 'n', i, j):
                    return 2
 
                # Peão
                if lookForp(board, 'p', i, j):
                    return 2
 
                # Torre
                if lookForr(board, 'r', i, j):
                    return 2
 
                # Bispo
                if lookForb(board, 'b', i, j):
                    return 2
 
                # Rainha
                if lookForq(board, 'q', i, j):
                    return 2
 
                # Rei
                if lookFork(board, 'k', i, j):
                    return 2
    return 1

#Confere se o rei está atacando o outro
def lookFork(board, c, i, j):
    # Armazena todas possíveis movimentações do rei
    x = [ -1, -1, -1, 0, 0, 1, 1, 1 ]
    y = [ -1, 0, 1, -1, 1, -1, 0, 1 ]
 
    for k in range(8):
        # Incrementa o indice
        m = i + x[k]
        n = j + y[k]
 
        # Verifica se não ultrapassou o limite do tabuleiro
        if inBounds(m, n) and board[m][n] == c:
            return True
    return False
 
# Checa se a rainha está atacando o rei
def lookForq(board, c, i, j):
   
    # A rainha se move como uma
    # combinação do bispo e da torre
    if lookForb(board, c, i, j) or lookForr(board, c, i, j):
        return True
    return False
 
# Checa se o bispo ataca o rei
def lookForb(board, c, i, j):
    # Diagonal inferior direita
    k = 0
    while inBounds(i + ++k, j + k):
        if board[i + k][j + k] == c:
            return True
        if board[i + k][j + k] != '-':
            break
 
    # Diagonal inferior esquerda
    k = 0
    while inBounds(i + ++k, j - k):
        if board[i + k][j - k] == c:
            return True
        if board[i + k][j - k] != '-':
            break
 
    # Diagonal superior direita
    k = 0
    while inBounds(i - ++k, j + k):
        if board[i - k][j + k] == c:
            return True
        if board[i - k][j + k] != '-':
            break
 
    # Diagonal superior esquerda
    k = 0
    while inBounds(i - ++k, j - k):
        if board[i - k][j - k] == c:
            return True
        if board[i - k][j - k] != '-':
            break
 
    return False
 
# Confere se a torre está atacando o rei
def lookForr(board, c, i, j):
    # Abaixo
    k = 0
    while inBounds(i + ++k, j):
        if board[i + k][j] == c:
            return True
        if board[i + k][j] != '-':
            break
 
    # Acima
    k = 0
    while inBounds(i + --k, j):
        if board[i + k][j] == c:
            return True
        if board[i + k][j] != '-':
            break
 
    # Direita
    k = 0
    while inBounds(i, j + ++k):
        if board[i][j + k] == c:
            return True
        if board[i][j + k] != '-':
            break
 
    # Esquerda
    k = 0
    while inBounds(i, j + --k):
        if board[i][j + k] == c:
            return True
        if board[i][j + k] != '-':
            break
    return False
 
# Confere se o cavalo está atacando o rei
def lookForn(board, c, i, j):
    # Todas as possibilidades de movimentação do cavalo
    x = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
    y = [ 1, -1, 1, -1, 2, -2, 2, -2 ]
 
    for k in range(8):
        # Incrementa os índices
        m = i + x[k]
        n = j + y[k]
 
        # Verifica se não ultrapassou o limite do tabuleiro
        if inBounds(m, n) and board[m][n] == c:
            return True
    return False
 
# Confere se o peão está atacando o rei
def lookForp(board, c, i, j):
    if ord(c) >= 65 and ord(c) <= 90:
        # Para peões brancos
        lookFor = 'P'
        if inBounds(i + 1, j - 1) and board[i + 1][j - 1] == lookFor:
            return True
 
        if inBounds(i + 1, j + 1) and board[i + 1][j + 1] == lookFor:
            return True
    else:
        # Para peões pretos
        lookFor = 'p'
        if inBounds(i - 1, j - 1) and board[i - 1][j - 1] == lookFor:
            return True
        if inBounds(i - 1, j + 1) and board[i - 1][j + 1] == lookFor:
            return True
    return False
 
# Checa se os índices não ultrapassam o limite do tabuleiro
def inBounds(i, j):
    return i >= 0 and i < 8 and j >= 0 and j < 8
 
# Testes
board1 = [
  [ '-', '-', 'k', '-', '-', '-', '-', '-' ],
  [ 'p', 'p', 'p', '-', 'p', 'p', 'p', 'p' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ '-', 'R', '-', '-', '-', 'B', '-', '-' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P' ],
  [ 'K', '-', '-', '-', '-', '-', '-', '-' ] 
]

board2 = [
  [ '-', '-', '-', 'k', '-', '-', '-', '-' ],
  [ 'p', 'p', 'p', '-', 'p', 'p', 'p', 'p' ],
  [ '-', '-', '-', '-', '-', 'b', '-', '-' ],
  [ '-', '-', '-', 'R', '-', '-', '-', '-' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ 'P', '-', 'P', 'P', 'P', 'P', 'P', 'P' ],
  [ 'K', '-', '-', '-', '-', '-', '-', '-' ] 
]

board3 = [
  [ 'r', 'n', 'b', 'q', 'k', '-', 'n', 'r' ],
  [ 'p', 'p', 'p', '-', '-', 'p', 'p', 'p' ],
  [ '-', '-', '-', '-', 'p', '-', '-', '-' ],
  [ '-', '-', '-', 'p', '-', '-', '-', '-' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ '-', '-', '-', '-', '-', '-', '-', '-' ],
  [ 'P', 'P', '-', '-', 'P', 'P', 'P', 'P' ],
  [ 'R', 'N', 'B', 'Q', 'K', 'B', '-', 'R' ] 
]


board = board1
if checkBoard(board) == 0:
  print("No king in danger")
elif checkBoard(board) == 1:
  print("White king in danger")
else:
  print("Black king in danger")