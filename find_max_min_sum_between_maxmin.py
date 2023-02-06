temp_array = [2, 6, 6, 4, 64135, 13, 2, 5, 4, 654413456, 513,1]


""" ищем совпадения """

array = []
for i in temp_array:
    if i not in array:
        array.append(i)

"""Вводные"""

max_number = array[0]
min_number = array[0]
max_index = 0
min_index = 0
index = 0

"""Ищем максимальное и минимальное значение и их индексы"""

while index < len(array):
    if array[index] > max_number:
        max_number = array[index]
        max_index = index

    if array[index] < min_number:
        min_number = array[index]
        min_index = index
    index += 1

print(array)
print('минимальное число ', min_number, ' его индекс ', min_index)
print('максимальное число ', max_number, ' его индекс ', max_index)

""" Ищем сумму между максимальным и минимальным значением """

""" Проверка равенства элементов  НЕ НУЖНА!!!
if max_index == min_index:
    sum = max_number
    
    print('сумма между максимальным и минимальным значением ', sum) """

sum = 0
if max_index > min_index:

    while min_index <= max_index:
        sum += array[min_index]
        min_index += 1

else:

    while max_index <= min_index:
        sum += array[max_index]
        max_index += 1
print('сумма между максимальным и минимальным значением ', sum)