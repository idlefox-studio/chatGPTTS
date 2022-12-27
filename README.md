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
```
The value of your API key will be the resulting output.

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



## Example Code
Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position. gTTS will translate the response and output the audio along with the text

```sh
chatGPTTS - beta

Human:
whats on your mind\?

AI: 
I am thinking about how to best manage my day so I can make the most of my \time and be productive.
```