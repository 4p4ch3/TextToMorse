import json
import time

from playsound import playsound

sounds = {".": "sounds/shortbeep.mp3", "-": "sounds/longbeep.mp3"}

with open("characters.json", 'r') as characters:
    data = json.load(characters)

text = input("Enter text you want to translate > ")
morse_text = []

for i in text.lower():
    if i.isspace():
        morse_text.append('/ ')
    else:
        try:
            morse_text.append(data[i])
        except KeyError:
            morse_text.append(' ')
        morse_text.append(' ')

morse_text = ''.join(morse_text)
print(morse_text)

for i in morse_text:
    if i.isspace():
        continue
    elif i == "/":
        time.sleep(0.7)
        continue
    else:
        playsound(sounds[i])
