numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
valid_numbers = [num for num in numbers if num is not None]
sum_numbers = sum(valid_numbers)
count_numbers = len(valid_numbers) + 1
average = sum_numbers / count_numbers

result = [average if num is None else num for num in numbers]


print("Измененный список:", result)
