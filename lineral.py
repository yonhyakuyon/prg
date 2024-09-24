# # Линейный конгруэнтный алгоритм

# x0 = int(input("Введите Х0: "))
# a = int(input("Введите a: "))
# c = int(input("Введите с: "))
# m = int(input("Введите m: "))

# x = x0
# sequence = []

# with open("result.txt", "w") as f:
#     for n in range(m):
#         x = (a * x + c) % m
#         value = x / m
#         f.write(str(x) + "\n")
#         sequence.append(value)
#     mean_value = sum(sequence) / len(sequence)
#     variance = sum((x - mean_value) ** 2 for x in sequence) / len(sequence)
# Хорошие коэффиценты:
# a = 106	c = 1283	m = 6075
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка таблицы коэффициентов
coefficients = pd.read_csv("coefficients.csv")

# Список для хранения длины периодов для каждой строки
period_lengths = []

# Перебор всех строк с коэффициентами
for index, row in coefficients.iterrows():
    print(f"\nЗапуск для строки {index} с коэффициентами:")
    print(row)

    a = row["a"]
    c = row["c"]
    m = row["m"]

    x0 = 1  # x0 всегда равен 1

    x = x0
    sequence = []
    period_detected = False
    max_iterations = 10000000  # Увеличим количество итераций для лучшего поиска периода
    value_positions = {}  # Словарь для отслеживания позиций значений

    # Запуск линейного конгруэнтного алгоритма
    for n in range(1, max_iterations + 1):
        x = (a * x + c) % m
        value = x / m
        sequence.append(value)

        # Проверка на периодичность
        if value in value_positions:
            period_start = value_positions[value]
            period_length = n - period_start
            print(f"Период обнаружен! Длина периода: {period_length} (на итерации {n})")
            period_detected = True
            period_lengths.append(
                period_length
            )  # Добавляем длину периода для текущей строки
            break
        else:
            value_positions[value] = n

    if not period_detected:
        print(
            "Период не обнаружен. Возможно, требуется больше итераций или другие коэффициенты."
        )
        period_lengths.append(0)  # Если период не найден, добавляем 0

# График зависимости длины периода от строки коэффициентов
plt.figure(figsize=(10, 6))
plt.plot(range(len(period_lengths)), period_lengths, marker="o")
plt.title("Зависимость длины периода от строки коэффициентов")
plt.xlabel("Номер строки коэффициентов")
plt.ylabel("Длина периода")
plt.grid()
# plt.savefig("period_lengths_plot.png")
plt.show()
