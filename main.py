from datetime import datetime
from weatherapi.WeatherApiClient import WeatherApiClient
from telegram.formatter.MessageFormatter import MessageFormatter
from telegram.TelegramBotClient import TelegramBotClient

WEATHERAPI_API_KEY = "55998201356948a4a78194504232309"

TELEGRAM_BOT_API_KEY = "6300676794:AAEWeMnIolor4T7eErlmW5UUkXF7LCgbcnI"
TELEGRAM_CHANNEL = "@kodymaforecast"

print("Obtaining forecast for today: " + datetime.now().strftime("%B %d, %Y %H:%M:%S"))

weatherApiClient = WeatherApiClient(WEATHERAPI_API_KEY)
todayWeatherForecastData = weatherApiClient.todayWeather()

print("Forecast data obtained. Start formatting message for telegram")

messageFormatter = MessageFormatter()
formattedForecastMsg = messageFormatter.format(todayWeatherForecastData)

print("Message for telegram formatted. Start sending it to telegram")

tgClient = TelegramBotClient(TELEGRAM_BOT_API_KEY, TELEGRAM_CHANNEL)
tgClient.send(formattedForecastMsg)

print("Message was sent successfully")
