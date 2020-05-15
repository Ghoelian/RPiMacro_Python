from gpiozero import Button

import requests

button1pressed = False
button2pressed = False

button1 = Button(18)
button2 = Button(23)

while True:
  if button1.is_pressed:
    if button1pressed != True:
      print("Sending obs action")
      requests.get(url = "http://192.168.2.27:3000/macro", params = { 'action': 'obs' })
      button1pressed = True
      print("OBS request sent, button1pressed is true")
  else:
    if button1pressed:
      button1pressed = False
      print("Button 1 released, is now False")

  if button2.is_pressed:
    if button2pressed != True:
      print("Sending discord action")
      requests.get(url = "http://192.168.2.27:3000/macro", params = { 'action': 'discord' })
      button2pressed = True
      print("Discord action sent, button2pressed is True")
  else:
    if button2pressed:
      button2pressed = False
      print("Button 2 released, is now False")
