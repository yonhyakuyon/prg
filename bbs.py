from random import randint
import sympy


# Нахождение НОД (необходим для проверки seed)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class BBS:

    def __init__(self, q, p, seed):

        # Проверка, что p и q - простые числа
        if not (sympy.isprime(p) and sympy.isprime(q)):
            raise ValueError("Оба числа должны быть простыми")

        # Проверка, что p и q не равны
        if p == q:
            raise ValueError("Числа p и q не должны быть равны")
        # Проверка, что p и q удовлетворяют условию p % 4 == 3 и q % 4 == 3
        if p % 4 != 3 or q % 4 != 3:
            raise ValueError("Числа p и q должны быть вида 3 (mod 4)")

        # Вычисляем модуль n = p * q
        self.n = p * q

        if gcd(seed, self.n) != 1:
            raise ValueError("seed должен быть взаимно прост с n")

        # Устанавливаем начальное состояние (seed)
        self.state = seed

    def DegreeM(a, k, n):
        b = 1
        while k != 0:
            if k % 2 == 1:
                b = (b * a) % n
            k = k // 2
            a = (a * a) % n
        return b

    def next_number(self):
        # Генерируем следующее состояние
        self.state = (self.state**2) % self.n
        return self.state

    def generate_sequence_and_bits(self, length):
        with open("bbs.txt", "w") as f:
            with open("bbs_bits.txt", "w") as f2:
                for _ in range(length):
                    number = self.next_number()
                    f.write(str(number) + "\n")
                    f2.write(str(number % 2) + "\n")


# Использование
p = int(input("Введите p"))
q = int(input("Введите q"))
seed = int(input("Введите seed"))
length = int(input("Введите длинну последовательности"))
bbs = BBS(p, q, seed)
bbs.generate_sequence_and_bits(length)
