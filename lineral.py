# Линейный конгруэнтный алгоритм

x0 = int(input("Введите Х0: "))
a = int(input("Введите a: "))
c = int(input("Введите с: "))
m = int(input("Введите m: "))

x = x0
sequence = []

with open("result.txt", "w") as f:
    for n in range(m):
        x = (a * x + c) % m
        value = x / m
        f.write(str(x) + "\n")
        sequence.append(value)
    # print(" ".join([str(x) for x in sequence])) #frequency
    mean_value = sum(sequence) / len(sequence)
    variance = sum((x - mean_value) ** 2 for x in sequence) / len(sequence)
    print(f"\n\n Среднее значение: {mean_value}\n Дисперсия: {variance}")
# Хорошие коэффиценты:
# a = 106	c = 1283	m = 6075
