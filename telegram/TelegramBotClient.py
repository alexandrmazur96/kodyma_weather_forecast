import requests
import json
import sys

class TelegramBotClient:
    BASE_URL = "https://api.telegram.org/"
    SEND_MESSAGE_URI = "/sendMessage"

    def __init__(self, apiKey, telegramChannel):
        self.apiKey = apiKey
        self.telegramChannel = telegramChannel

    def send(self, formattedMessage):
        requestData = {
            "chat_id": self.telegramChannel,
            "text": formattedMessage,
            "parse_mode": "HTML"
        }
        response = requests.post(self.BASE_URL + self.__getToken() + self.SEND_MESSAGE_URI, requestData)
        if response.status_code != 200:
            sys.stderr.write("Unable to send message to telegram using bot API. Status code: " + str(response.status_code) + "; Details: " + str(response.content))
            exit(1)
        return json.loads(response.content)

    def __getToken(self):
        return "bot" + self.apiKey