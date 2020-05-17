from gpiozero import Button

import requests

button1pressed = False
button2pressed = False
button3pressed = False
button4pressed = False
button5pressed = False

button1 = Button(18)
button2 = Button(23)
button3 = Button(12)
button4 = Button(25)
button5 = Button(16)


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

    if button3.is_pressed:
        if button3pressed != True:
            button3pressed = True
            print("Button 3 pressed, is now True")
    else:
        if button3pressed:
            print("Sending discord action")
            requests.get(url="http://192.168.2.27:3000/macro",
                         params={'action': 'toggleplay'})
            print("Discord request sent")
            button3pressed = False
            print("Button 3 released, is now False")
    
    if button4.is_pressed:
        if button4pressed != True:
            button4pressed = True
            print("Button 4 pressed, is now True")
    else:
        if button4pressed:
            print("Sending discord action")
            requests.get(url="http://192.168.2.27:3000/macro",
                         params={'action': 'previous'})
            print("Discord request sent")
            button4pressed = False
            print("Button 4 released, is now False")

    if button5.is_pressed:
        if button5pressed != True:
            button5pressed = True
            print("Button 5 pressed, is now True")
    else:
        if button5pressed:
            print("Sending discord action")
            requests.get(url="http://192.168.2.27:3000/macro",
                         params={'action': 'next'})
            print("Discord request sent")
            button5pressed = False
            print("Button 5 released, is now False")