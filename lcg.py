class LCG:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.x = seed

    def next(self):
        sequence = []
        with open("result.txt", "w") as f:
            for n in range(self.m):
                self.x = (self.a * self.x + self.c) % self.m
                value = self.x / self.m
                f.write(str(self.x) + "\n")
                sequence.append(value)
        mean_value = sum(sequence) / len(sequence)
        variance = sum((self.x - mean_value) ** 2 for self.x in sequence) / len(
            sequence
        )
        print("Среднее значение: ", mean_value)
        print("Дисперсия: ", variance)


x0 = int(input("Введите Х0: "))
a = int(input("Введите a: "))
c = int(input("Введите с: "))
m = int(input("Введите m: "))

lcg = LCG(x0, a, c, m)
lcg.next()
