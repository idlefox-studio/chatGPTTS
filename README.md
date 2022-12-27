# chatGPTTS

Simple Integration of OpenAI chatGPT with gTTS

## Documentation

See the [OpenAI API docs](https://beta.openai.com/docs/api-reference?lang=python).

See the [gTTS Documentation](https://gtts.readthedocs.io/en/latest/).

## Installation

In order to be able to run the script you have to make sure that you have the requiered Libraries installed

```sh
pip install --upgrade openai # chatGPT 
```
```sh
pip install gtts # Google Text-to-Speech
```
```sh
pip install pygame # for audio playback
```
- - - -
## Usage
The library needs to be configured with your account's secret key which is available on the [website](https://beta.openai.com/account/api-keys). 

Either set it as the `OPENAI_API_KEY` environment variable before using the library:

### Linux / MacOS Set-up

1. Run the following command in your terminal, replacing `yourkey` with your [API Keys](https://beta.openai.com/account/api-keys).
```bash
echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc
```
2. Update the shell with the new variable:
```bash
source ~/.zshrc
```
3. Confirm that you have set your environment variable using the following command. 
```bash
echo $OPENAI_API_KEY
# The value of your API key will be the resulting output.
```

### Import

You can set `OPENAI_API_KEY` Environment Variable using bash
by replacing `.zshrc` with `.bash_profile`.

###

```python
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]
```

Or set `openai.api_key` to its value:

```python
import openai
openai.api_key = "sk-..."
```

Althogh you should use environment variables or a secret management tool to expose your key to your applications.

- - - -

#### Example
Given a prompt, **OpenAi** model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position. **gTTS** will generate the response and output the audio along with text

 
```
Human:
whats on your mind?

AI: 
I am thinking about how to best manage my day so I can make the most of my time and be productive.
```
```
Human:
can you tell me the shortest route from Rome to Milan

AI: 
The shortest route from Rome to Milan is about 300 miles and can be driven in about 5 hours.
The fastest route would be via the Autostrada del Sole, which travels from Rome to Bologna
and then on to Milan.
```

### Language Customization

For a complete list of available languages you can check with
```sh
gtts-cli --all
```

#### Italian
```python
# change the default language 
def speak(text, language='it'):
    tts = gtts.gTTS(text,lang=language,slow=False)
```
```
Human:
puoi dirmi la via piu breve da Roma a Milano

AI: 
La via più breve da Roma a Milano è prendere l'autostrada A1, passando per Firenze.
L'intero viaggio richiede circa 5 ore.
```
#### Japanese
```python
def speak(text, language='ja'):
    tts = gtts.gTTS(text,lang=language,slow=True)
```
```
Human:
AI のさまざまなドメイン/サブセットとは?

AI: 
AIのさまざまなドメイン/サブセットとは、人工知能の分野を構成するさまざまな専門領域に関するものです。
例えば、機械学習、自然言語処理、コンピュータビジョン、ロボティクスなどです。
これらのドメイン/サブセットでは AIの要素が多くの方法で用いられています。
通常、AI強化学習などの技術を用いて、分野の特性を学んでいきます。
```

- - - -

#### Localized ‘accents’

For a given language, Google gTTS can speak in different local ‘accents’ depending on the Google domain (google.**tld**) of the request, with some examples shown in the table below.

| Local                    | Language | Top-level domain |
| left                     | center   | right            |
| :----------------------- | :------: | ---------------: |
| English (United States)  | en       | com #default     |
| English (Australia)      | en       | com.au           |
| English (United Kingdom) | en       | co.uk            |
| English (India)          | en       | co.in            |
| French (Canada)          | en       | co.in            |
