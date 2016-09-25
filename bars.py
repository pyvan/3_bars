import json


def load_data(filepath):
    with open(filepath, 'r') as infile:
        input_data = json.loads(infile.read())
    return input_data


def get_biggest_bar(data):
    max_seats = 0
    bar = data[0]
    for item in data:
        if item['Cells']['SeatsCount'] > max_seats:
            max_seats = item['Cells']['SeatsCount']
            bar = item
    return bar['Cells']['Name'], bar['Cells']['Address']


def get_smallest_bar(data):
    min_seats = data[0]['Cells']['SeatsCount']
    bar = data[0]
    for item in data:
        if item['Cells']['SeatsCount'] < min_seats:
            min_seats = item['Cells']['SeatsCount']
            bar = item
    return bar['Cells']['Name'], bar['Cells']['Address']


def get_closest_bar(data, longitude, latitude):
    bar = data[0]
    min_long = abs(bar['Cells']['geoData']['coordinates'][0] - longitude)
    min_lat = abs(bar['Cells']['geoData']['coordinates'][1] - latitude)
    for item in data:
        data_long, data_lat = item['Cells']['geoData']['coordinates']
        long = abs(data_long - longitude)
        lat = abs(data_lat - latitude)
        if long < min_long and lat < min_lat:
            min_long = long
            min_lat = lat
            bar = item
    return bar['Cells']['Name'], bar['Cells']['Address']


if __name__ == '__main__':
    help_message = """
    1 - Бар с максимальной наполняемостью.
    2 - Бар с минимальной наполняемостью.
    3 - Ближайший бар.
    4 - Список команд.
    0 - Выход.
    """
    print(help_message)
    while True:
        data = load_data('data.json')
        action = input('Ваше действие: ')
        if action not in ('1', '2', '3', '4', '0'):
            print('Некорректное действие!')
        elif action == '1':
            bar_name, bar_address = get_biggest_bar(data)
            print('Вас интересует бар: "{}", по адресу "{}"'.format(
                bar_name, bar_address
            ))
        elif action == '2':
            bar_name, bar_address = get_smallest_bar(data)
            print('Вас интересует бар: "{}", по адресу "{}"'.format(
                bar_name, bar_address
            ))
        elif action == '3':
            long, lat = input('Введите координаты, через точку с заятой: ').split(';')
            bar_name, bar_address = get_closest_bar(
                data, float(long), float(lat)
            )
            print('Вас интересует бар: "{}", по адресу "{}"'.format(
                bar_name, bar_address
            ))
        elif action == '4':
            print(help_message)
        elif action == '0':
            print('Всего хорошего!')
            break
