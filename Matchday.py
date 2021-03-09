"""
С официального сайта Российской Футбольной Премьер-Лиги извлекаются матчи текущего тура.
"""

import requests
from bs4 import BeautifulSoup
import re

current_week = []

url = 'https://premierliga.ru/tournaments/championship/calendar/'  # расписание ближайшего тура
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

matches_html = soup.find_all('tr', class_='matchtr')  # поиск строк по тэгу <tr>

pattern = r'(.*)((-:-.*\ничья.*)|(\d\:\d))(\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2})(.*)'  # шаблон для поиска

for game in matches_html:
    game = game.text.strip()  # удаление пробельных символов
    game_clear = re.match(pattern, game)  # поиск соответствия строки шаблону
    stroka = str(game_clear.group(5) + '\t' + game_clear.group(1) + '\t' + game_clear.group(6))  # запись нужных групп
    current_week.append(stroka)  # запись времени, команд и места проведения матча
