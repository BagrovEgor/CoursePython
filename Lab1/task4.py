users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
info = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
count = len(users)
unique = set(users)
info["Общее количество"] = count
info["Уникальные посещения"] = len(unique)
print(info)