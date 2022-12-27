# mastyDev 2022.12
import os
import openai # pip install openai
import gtts 
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import time

openai.api_key = os.environ["OPENAI_API_KEY"] # OpenAI API
pygame.init()
pygame.mixer.init()

def speak(text, language='en'):
    tts = gtts.gTTS(text,lang=language,slow=True)
    tts.save('_temp3.mp3')
    pygame.mixer.music.load("_temp3.mp3")
    pygame.mixer.music.play()

#input
# start_sequence = "\nAI:"
# restart_sequence = "\nHuman: "
print("chatGPTTS - beta")
desc=input(f"\nHuman:\n")
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
print(f"\nAI:{response.choices[0].text}")
while pygame.mixer.music.get_busy() == True:
    time.sleep(1)
else:
    pygame.mixer.music.stop()
    time.sleep(0)