from plyer import notification
from time import sleep
import requests, json


icon_path = "crypto.ico"
ignore_list = []


def request_crypto(currency, symbol, price):

    global icon_path

    if currency in ignore_list:
        return

    if symbol == ">":
        if float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=" + currency).json()["price"]) > price:
            
            notification.notify(title="Crypto notification", message=currency + " is higher than " + str(price), app_icon=icon_path)
            ignore_list.append(currency)

    elif symbol == "<":
        if float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol=" + currency).json()["price"]) < price:

            notification.notify(title="Crypto notification", message=currency + " is lower than " + str(price), app_icon=icon_path)
            ignore_list.append(currency)


def main():

    global icon_path

    with open("config.txt") as json_config:
        json_data = json.load(json_config)
        notification.notify(title="Crypto notification", message="Running", app_icon = icon_path)

    while True:
        for i in json_data["array"]:
            request_crypto(i[0], i[1], i[2])

        sleep(json_data["sleep"])


main()
