from datetime import datetime

class MessageFormatter:
    def format(self, rawForecastData):
        weatherMsg = "Станом на <b>" + rawForecastData['current']['last_updated'] + "</b> в <i>" + rawForecastData['location']['name'] + "," + rawForecastData['location']['region'] + "</i> <b>" + rawForecastData['current']['condition']['text'].lower() + "</b>.\n"
        weatherMsg += "Температура повітря <b>" + str(rawForecastData['current']['temp_c']) + " °C.</b> " + "Відчувається як <b>" + str(rawForecastData['current']['feelslike_c']) + "°C</b>\n"
        weatherMsg += "Швидкість вітру складає <b>" + str(rawForecastData['current']['wind_kph']) + " км/год</b> з поривами до <b>" + str(rawForecastData['current']['gust_kph']) + " км/год</b>\n"
        weatherMsg += "Видимість - <b>" + str(rawForecastData['current']['vis_km']) + " км</b>\n"
        weatherMsg += "Вологість повітря - <b>" + str(rawForecastData['current']['humidity']) + "%</b>\n"
        weatherMsg += "Хмарність - <b>" + str(rawForecastData['current']['cloud']) + "%</b>\n"
        weatherMsg += "Індекс ультрафіолету - <b>" + str(rawForecastData['current']['uv']) + "</b>\n"
        weatherMsg += "Якість повітря - <i>" + self.__getAirQuality(rawForecastData['current']['air_quality']) + "</i>\n\n"
        weatherMsg += "Погодинний прогноз на сьогодні:\n\n" + self.__getForecastForToday(rawForecastData['forecast']['forecastday'][0])

        return weatherMsg
    
    def __getAirQuality(self, airQualityData):
        gauges = "Окис вуглецю (чадний газ) - <b>" + str(airQualityData['co']) + " μg/m3</b>; "
        gauges += "Озон - <b>" + str(airQualityData['o3']) + " μg/m3</b>; "
        gauges += "Діоксид азоту - <b>" + str(airQualityData['no2']) + " μg/m3</b>; "
        gauges += "Діоксид сірки - <b>" + str(airQualityData['so2']) + " μg/m3</b>; "
        gauges += "Вміст твердих частинок до 2.5 мікрон - <b>" + str(airQualityData['pm2_5']) + " μg/m3</b>; "
        gauges += "Вміст твердих частинок до 10 мікрон - <b>" + str(airQualityData['pm10']) + " μg/m3</b>;"

        if airQualityData['us-epa-index'] == 1:
            return "<b>Добре</b> (" + gauges + ")"
        elif airQualityData['us-epa-index'] == 2:
            return "<b>Помірно</b> (" + gauges + ")"
        elif airQualityData['us-epa-index'] == 3:
            return "<b>Шкідливе для чутливих груп</b> (" + gauges + ")"
        elif airQualityData['us-epa-index'] == 4:
            return "<b>Шкідливе (" + gauges + ")"
        elif airQualityData['us-epa-index'] == 5:
            return "<b>Дуже шкідливе</b> (" + gauges + ")"
        elif airQualityData['us-epa-index'] == 6:
            return "<b>Небезпечне</b> (" + gauges + ")"
        
    def __getForecastForToday(self, forecastData):
        forecastStr = ""
        # Start from the next hour after the current one. We don't need a forecast for the time that already in the past.
        for forecastForHour in forecastData['hour'][datetime.now().hour + 1:]:
            forecastStr += "Станом на <b>" + forecastForHour['time'] + "</b>;\n"
            forecastStr += "\t Температура повітря - <b>" + str(forecastForHour['temp_c']) + "°C</b>. Відчувається як - <b>" + str(forecastForHour['feelslike_c']) + "°C</b>.\n"
            forecastStr += "\t Швидкість вітру складатиме <b>" + str(forecastForHour['wind_kph']) + " км/год</b> з поривами до <b>" + str(forecastForHour['gust_kph']) + " км/год</b>.\n"
            forecastStr += "\t Видимість - <b>" + str(forecastForHour['vis_km']) + " км</b>.\n"
            forecastStr += "\t Вологість повітря - <b>" + str(forecastForHour['humidity']) + "%</b>\n"
            forecastStr += "\t Хмарність - <b>" + str(forecastForHour['cloud']) + "%</b>\n"
            forecastStr += "\t <i>Очікується дощ</i>.\n" if forecastForHour['will_it_rain'] == 1 else "\t <i>Дощ не очікується</i>.\n"
            forecastStr += "---------------------------------------\n\n"
        
        return forecastStr;