
import random

#Инициализируем переменные
height = random.randint(4, 8)
width = random.randint(4, 8)

#Создаём список
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

#Создаём множество для хранения уникальных элементов, кратных 3
three = set()

#Инициализируем переменную суммы для хранения суммы чисел из списка three
total_sum = 0 

#Создаём матрицу с случайными элементами
table = [[random.choice(numbers) for j in range(width)] for i in range(height)]

#Выводим матрицу в форматированном виде
print("Сгенерированная матрица:")
for row in table:
    print("  ".join(map(str, row)))

#цикл по строкам матрицы
for row in table:
    #проходимся по элементам строки
    for element in row:
        #Если элемент кратен 3, добавляем его в three
        if element % 3 == 0:
            three.add(element)

#Выводим на экран уникальные числа
print(f"Числа, кратные трем: {sorted(three)}")

#Считаем сумму уникальных чисел
total_sum = sum(three)

#Выводим итоговую сумму чисел
print("Сумма равна:", total_sum)