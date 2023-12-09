# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, separator=","):
    list1 = str1.split(separator)
    list2 = str2.split(separator)
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))