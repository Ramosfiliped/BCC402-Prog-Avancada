class SternBrocot():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # Como o problema de sternbrocot pode ser descrito como um problema
    # de árvore, recursão é a maneira mais fácil de resolver
    def find(self, a=0, b=1, c=1, d=0):
        # a b => a/b (primeira fração da esquerda)
        # c d => c/d (primeira fração da direita)
        m = int(a + c)
        n = int(b + d)

        # Se for igual, pode retornar o resultado acumulado do retorno
        if self.x == m and self.y == n:
            return ""
        
        # Se em uma multiplicação cruzada, meu numerador ficar maior, significa
        # que o caminho é pela esquerda
        if self.x * n < self.y * m:
            return "L" + self.find(a=a,b=b,c=m,d=n)
        else:
            return "R" + self.find(a=m,b=n,c=c,d=d)     

solver = SternBrocot(5, 7)
print(solver.find())

solver = SternBrocot(878, 323)
print(solver.find())