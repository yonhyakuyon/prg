class Xorshift:
    def __init__(
        self,
        seed: int,
        a: int,
        b: int,
        c: int,
        d: int,
    ):
        self.state = seed if seed != 0 else 1  # Нулевой seed недопустим
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def next(self) -> int:
        x = self.state
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x ^= (x << a) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> b) & 0xFFFFFFFFFFFFFFFF
        x ^= (x << c) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> d) & 0xFFFFFFFFFFFFFFFF
        self.state = x
        return x


seed = int(input("Введите seed:"))
a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
d = int(input("Введите d:"))
steps = int(input("Введите кол-во последов."))

xor = Xorshift(seed, a, b, c, d)

for i in range(steps):
    with open("xorshift.txt", "w") as f:
        f.write(str(xor.next()) + "\n")
