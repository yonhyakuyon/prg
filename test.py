import math


# Проверка числа на простоту
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Нахождение НОД (необходим для проверки seed)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Алгоритм BBS
class BBS:
    def __init__(self, p, q, seed):
        # Проверка, что p и q - простые числа и удовлетворяют условию p ≡ q ≡ 3 (mod 4)
        if not (is_prime(p) and is_prime(q)):
            raise ValueError("p и q должны быть простыми числами")
        if p % 4 != 3 or q % 4 != 3:
            raise ValueError("p и q должны быть сравнимы с 3 по модулю 4")

        # Вычисляем модуль n = p * q
        self.n = p * q

        # Проверяем, что seed взаимно прост с n
        if gcd(seed, self.n) != 1:
            raise ValueError("seed должен быть взаимно прост с n")

        # Устанавливаем начальное состояние (seed)
        self.state = seed

    # Генерация следующего псевдослучайного числа
    def next_number(self):
        # Генерируем новое состояние
        self.state = (self.state**2) % self.n

        # Возвращаем текущее состояние как псевдослучайное число
        return self.state

    # Генерация последовательности псевдослучайных чисел и младших битов
    def generate_sequence_and_bits(self, length):
        sequence = []
        bits = []
        for _ in range(length):
            number = self.next_number()
            sequence.append(number)
            bits.append(number % 2)  # Добавляем младший бит текущего состояния
        return sequence, bits


# Пример использования
p = 11
q = 29
seed = 3
bbs = BBS(p, q, seed)

# Генерация 10 псевдослучайных чисел и младших битов
random_sequence, random_bits = bbs.generate_sequence_and_bits(10)

print("Псевдослучайные числа:", random_sequence)
print("Последовательность младших битов:", random_bits)
