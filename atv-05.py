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