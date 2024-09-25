def find_period_from_file(filename):
    # Чтение сгенерированных чисел из файла
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f]

    # Поиск периода
    sequence = []
    for x in numbers:
        if x in sequence:
            first_occurrence = sequence.index(x)
            period = len(sequence) - first_occurrence
            return period, sequence
        sequence.append(x)

    # Если повторений не найдено, период равен длине последовательности
    return None, sequence


# Выполняем тест
filename = input("Введите имя файла: ")
period, sequence = find_period_from_file(filename)

# Вывод результатов
if period:
    print(f"Период: {period}")
else:
    print("Период не найден")
