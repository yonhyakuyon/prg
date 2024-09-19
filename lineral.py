# Линейный конгруэнтный алгоритм

x0 = int(input("Введите Х0: "))
c = int(input("Введите с: "))
a = int(input("Введите a: "))
m = int(input("Введите m: "))

x = x0
sequence = []

with open("result.txt", "w") as f:
    for n in range(m):
        x = (a * x + c) % m
        value = x / m
        f.write(str(x) + "\n")
        sequence.append(value)
    f.write(" ".join([str(x) for x in sequence]))
    mean_value = sum(sequence) / len(sequence)
    variance = sum((x - mean_value) ** 2 for x in sequence) / len(sequence)
    f.write(f"\n\n midValue: {mean_value}\n Dispersion: {variance}")
