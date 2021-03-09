import json
from Matchday import current_week

for i in current_week:  # перебор матчей тура
    i = i.split('\t')
    print(i[0])  # вывод даты и времени матча
    teams = str(i[1]).split(' - ')  # деление группы из двух команд на отдельные элементы
    with open('stats_rfpl.json', 'r', encoding='utf-8') as f:  # чтение файла со статистическими данными
        data = json.load(f)
        for team_stat in data:  # поиск домашней команды в json
            for key, value in team_stat.items():  # перебор команд в stats.rfpl
                if value == teams[0]:  # если название команды в json == обрабатываемой команде
                    Xg_for_Home = float(team_stat['xG_for_At_Home'])  # запись в переменные стат.данных
                    Xg_against_Home = float(team_stat['xG_against_At_Home'])
                    Goals_for_Home = float(team_stat['Scored_Match'])
                    Goals_against_Home = float(team_stat['Conceded_Match'])
        for team_stat in data:  # поиск гостевой команды в json
            for key, value in team_stat.items():
                if value == teams[1]:
                    # в случае обнаружения нужной команды производится расчёт голов обеих команд
                    score_home = ((Xg_for_Home + float(team_stat['xG_against_At_Away']))/2) * (((Goals_for_Home / Xg_for_Home) + (float(team_stat['Conceded_Match']) / float(team_stat['xG_against_At_Away'])))/2)
                    score_away = ((float(team_stat['xG_for_At_Away']) + Xg_against_Home)/2) * (((float(team_stat['Scored_Match']) / float(team_stat['xG_for_At_Away'])) + (Goals_against_Home / Xg_against_Home))/2)

                    # вывод на экран результатов
                    print(teams[0], round(score_home), '-', round(score_away), teams[1])
                    print(i[2])
                    print()
                    with open('Results.txt', 'a') as results:
                        results.write(i[0] + '\n')  # запись даты и времени проведения матча
                        results.write(teams[0] + ' ')  # название домашней команды
                        results.write(str(round(score_home)))  # голы домашней команды
                        results.write('-')
                        results.write(str(round(score_away)) + ' ')  # голы гостевой команды
                        results.write(teams[1] + '\n')  # название гостевой команды
                        results.write(i[2] + '\n' + '\n')  # стадион
