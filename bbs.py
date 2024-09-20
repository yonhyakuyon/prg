from random import randint


def generate_numbers(kp):
    p = 0
    q = 0
    while True:
        num = randint(100, 1000)
        if num % 4 == 3:  # Проверка условия p ≡ 3 (mod 4)
            if PrimeMR(num, kp) == 1:  # Проверка на простоту методом Миллера-Рабина
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


def generate_mutually_prime_number(M):
    while True:
        x = randint(1, 100)
        if NOD(x, M) == 1:
            return x


def NOD(a, b):
    if b == 0:
        return a
    else:
        while b != 0:
            a, b = b, a % b
        return a


def BBS(length):
    numbers = generate_numbers(5)  # Генерация p и q
    M = numbers[0] * numbers[1]  # Вычисление M = p * q
    x = generate_mutually_prime_number(M)  # Генерация x, взаимно простого с M
    x0 = x**2 % M  # Инициализация начального состояния
    generate_sequence = []  # Для хранения последовательности чисел
    binary_generated_sequence = []  # Для хранения последовательности битов
    for _ in range(length):
        xi = (x0 * x0) % M  # Вычисление следующего числа в последовательности
        generate_sequence.append(xi)
        binary_generated_sequence.append(xi % 2)  # Генерация бита
        x0 = xi  # Обновление текущего состояния
    print(generate_sequence)  # Печать всей последовательности чисел
    print(binary_generated_sequence)  # Печать последовательности битов


BBS(21)
