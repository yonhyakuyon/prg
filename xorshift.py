class Xorshift:
    def __init__(
        self,
        seed: int,
        a: int,
        b: int,
        c: int,
        d: int,
    ):
        self.state = seed if seed != 0 else 1
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def next(self) -> int:
        x = self.state
        a = self.a
        b = self.b
        c = self.c
        # d = self.d
        x ^= (x << a) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> b) & 0xFFFFFFFFFFFFFFFF
        x ^= (x << c) & 0xFFFFFFFFFFFFFFFF
        # x ^= (x >> d) & 0xFFFFFFFFFFFFFFFF
        self.state = x
        return x

    def stats(self, sequence):
        mean_value = sum(sequence) / len(sequence)
        variance = sum((x - mean_value) ** 2 for x in sequence) / len(sequence)
        print("Среднее значение: ", mean_value)
        print("Дисперсия: ", variance)


seed = int(input("Введите seed:"))
a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
d = int(input("Введите d:"))
steps = int(input("Введите кол-во последов."))

xor = Xorshift(seed, a, b, c, d)

sequence = []

# Генерация последовательности и запись в файл
with open("xorshift.txt", "w") as f:
    for _ in range(steps):
        x = xor.next()
        sequence.append(x)
        f.write(str(x) + "\n")

# Подсчет статистики
xor.stats(sequence)
