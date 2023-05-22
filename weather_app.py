import json
from urllib.request import Request, urlopen
from datetime import datetime

app_id = 'c341e34f9b7c327502cde34aa7817c5f'
url_template = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid={}'


class Weather:
    def __init__(self, data):
        self.__temp = data['main']['temp']
        self.__description = data['weather'][0]['description']
        self.__humidity = data['main']['humidity']
        self.__wind_speed = data['wind']['speed']
        self.__pressure = data['main']['pressure']
        self.__city_name = data['name']

    def __str__(self):
        currentTime = datetime.now().strftime("%H:%M:%S")

        return f"""[{currentTime}] Запрос погоды в городе: {self.__city_name}
Температура: {self.__temp} °C, {self.__description}
Влажность воздуха: {self.__humidity}%
Скорость ветра: {self.__wind_speed} м/с
Атмосферное давление: {self.__pressure} мм рт. ст\n"""


def main():
    city_name = input('Введите название города на английском: ')

    request = Request(url_template.format(city_name, app_id))
    with urlopen(request) as response:
        content = response.read().decode('UTF-8')
        data = json.loads(content)

    weather = Weather(data)

    print(weather.__str__())
    with open('./weather.txt', 'a', encoding="UTF-8") as log:
        log.write(weather.__str__())


main()
