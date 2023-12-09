list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
countInTeam = int(len(list_players) / 2)
firstTeam = list_players[:countInTeam]
secondTeam = list_players[countInTeam:]
print(firstTeam)
print(secondTeam)