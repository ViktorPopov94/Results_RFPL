"""
В данном модуле осуществляется запуск модулей 'Matchday' и 'Prediction'. Прогнозируемые результаты
записываются в файл 'Results.txt'.
"""
enter = input('Введите "1" для записи результатов тура: ')

if enter == '1':
    import prediction
    print('Результаты записаны в файл Results.txt')
