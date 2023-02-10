numbers = [1, 8, 3, 8, 2, 6, 8, 8]
index = 0
maximum = numbers[0]
count_maximal = 0
while index < len(numbers):
    if numbers[index] > maximum:
        maximum = numbers[index]
        count_maximal = 1
    else:
        if numbers[index] == maximum:
            count_maximal = count_maximal + 1
    index = index + 1
print(count_maximal)
