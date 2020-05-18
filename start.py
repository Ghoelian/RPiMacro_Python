from gpiozero import Button
import requests

button1 = Button(18)
button2 = Button(23)
button3 = Button(12)
button4 = Button(25)
button5 = Button(16)

def sendRequest(action):
    print("Sending " + action + " request")

    try:
        requests.get(url="http://192.168.2.27:3000/macro",
                     params={'action': action})
        print(action + " request sent")
    except requests.exceptions.RequestException as e:
        print("Sending request failed: " + e)

print("App started")

while True:
    button1.when_released = sendRequest("obs")
    button2.when_released = sendRequest("discord")
    button3.when_released = sendRequest("toggleplay")
    button4.when_released = sendRequest("previous")
    button5.when_released = sendRequest("next")