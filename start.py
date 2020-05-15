from gpiozero import Button

import requests

button1pressed = False
button2pressed = False

button1 = Button(18)
button2 = Button(23)

while True:
    if button1.is_pressed:
        if button1pressed != True:
            button1pressed = True
            print("Button 1 pressed, is now true")
    else:
        if button1pressed:
            print("Sending obs action")
            requests.get(url="http://192.168.2.27:3000/macro",
                         params={'action': 'obs'})
            print("OBS request sent")
            button1pressed = False
            print("Button 1 released, is now False")

    if button2.is_pressed:
        if button2pressed != True:
            button2pressed = True
            print("Button 2 pressed, is now True")
    else:
        if button2pressed:
            print("Sending discord action")
            requests.get(url="http://192.168.2.27:3000/macro",
                         params={'action': 'discord'})
            print("Discord request sent")
            button2pressed = False
            print("Button 2 released, is now False")
