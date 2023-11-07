# Открываем файл
f = open('17_2024.txt')
# Считываем строки, записываюся в список
f = f.readlines()
# При помоши map преобразуем значения в списке из str в int
f = list(map(int,f))
# Находим макимальное число оканчивающееся на 13, тот же цикл for только в более короткой форме
max_13 = max(x for x in f if x % 100 == 13)
# Создаем 2 переменные для подсчета количества удовлетворяющих значений и максимальной суммы
count_value_numbers = 0
max_sum_numbers = 0

for i in range(len(f) - 2):
    sum_numbers = f[i] + f[i + 1] + f[i + 2] # тут сразу ищем сумму элементов
    if (
        (len(str(f[i])) == 3) + (len(str(f[i + 1])) == 3) + (len(str(f[i + 2])) == 3) == 2 and 
        sum_numbers < max_13
        ):# Условие, на занятии немного не внимательно прочитал задание, нужно 2 трехзначных числа
        count_value_numbers += 1 #Количество чисел
        max_sum_numbers = max(sum_numbers, max_sum_numbers) # Максимальная сумма
print(count_value_numbers, max_sum_numbers) 


