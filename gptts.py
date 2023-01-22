# @mastyDev 2022.12
import os
import time
import openai
import gtts
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

openai.api_key = os.environ["OPENAI_API_KEY"] # OpenAI API
pygame.init()
pygame.mixer.init()

def speak(text, language='en'):
    filename="_temp.mp4"
    tts = gtts.gTTS(text,lang=language,tld="co.uk", slow=False)
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

print("chatGPTTS")
#input
desc=input(f"\nHuman:\n")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=desc,
  temperature=.8,
  max_tokens=128,
  top_p=1,
  frequency_penalty=-0.0,
  presence_penalty=0.0,
)
#output
speak(response.choices[0].text)
print(f"\nAI:\n{response.choices[0].text.strip()}")
while pygame.mixer.music.get_busy() == True:
    time.sleep(1)
else:
    pygame.mixer.music.stop()
