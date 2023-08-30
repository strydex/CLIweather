import pip._vendor.requests

city = 'Екатеринбург'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = pip._vendor.requests.get(url).json()

temperature = round(weather_data['main']['temp'])

print('Сейчас в городе', city, str(temperature), '°C')