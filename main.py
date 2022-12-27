# mastyDev 2022.12
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import openai
import gtts 
import pygame
import time
import keys

openai.api_key = keys.API # OpenAI API
pygame.init()
pygame.mixer.init()

def speak(text, language='en'):
    tts = gtts.gTTS(text,lang=language,slow=False)
    tts.save('_temp3.mp3')
    pygame.mixer.music.load("_temp3.mp3")
    pygame.mixer.music.play()

#input
desc=input(f"ME >:\n")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=desc,
  temperature=0.9,
  max_tokens=512,
  top_p=1,
  frequency_penalty=-0.0,
  presence_penalty=0.7,
)
#output
speak(response.choices[0].text)
print(f"\nAI >:{response.choices[0].text}")
while pygame.mixer.music.get_busy() == True:
    time.sleep(1)
else:
    pygame.mixer.music.stop()
    time.sleep(1)