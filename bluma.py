from random import randint


def generate_numbers(kp):
    p = 0
    q = 0
    while True:
        num = randint(100, 1000)
        if num % 4 == 3:
            if PrimeMR(num, kp) == 1:
                if p == 0:
                    p = num
                else:
                    q = num
                    break
    return [p, q]


def PrimeMR(p, kp):
    if p == 2:
        return 1
    elif p % 2 == 0:
        return 0
    q = p - 1
    k = 0
    while q % 2 == 0:
        q = q // 2
        k = k + 1
    s = 0
    pr = 1
    while s < kp and pr == 1:
        a = randint(3, p - 1)
        b = DegreeM(a, q, p)
        c = 0
        while c < k and b != 1 and b != p - 1:
            b = DegreeM(b, 2, p)
            c = c + 1
        if b != 1 and b != p - 1 and c == k:
            pr = 0
        s = s + 1
    return pr


def DegreeM(a, k, n):
    b = 1
    while k != 0:
        if k % 2 == 1:
            b = (b * a) % n
        k = k // 2
        a = (a * a) % n
    return b


def gennerate_mutually_prime_number(M):
    x = randint(1, 100)
    if NOD(x, M) == 1:
        return x


def NOD(a, b):
    if b == 0:
        return a
    else:
        r = 1
        while r != 0:
            r = a % b
            a = b
            b = r
        return a


def BBS(length):
    numbers = generate_numbers(5)
    M = numbers[0] * numbers[1]
    x = gennerate_mutually_prime_number(M)
    x0 = x**2 % M
    generte_sequence = []
    binary_generated_sequence = []
    for _ in range(length):
        xi_1 = x0
        xi = (xi_1 * xi_1) % M
        generte_sequence.append(xi)
        binary_generated_sequence.append(xi % 2)
        x0 = xi
    print(generte_sequence)
    print(binary_generated_sequence)


BBS(21)
