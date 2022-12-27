# chatGPTTS

Simple Integration of OpenAI chatGPT with gTTS

## Documentation

See the [OpenAI API docs](https://beta.openai.com/docs/api-reference?lang=python).

See the [gTTS Documentation](https://gtts.readthedocs.io/en/latest/).

## Installation

In order to be able to run the script you have to make sure that you have the principle Libraries

```sh
pip install --upgrade openai
```

## Usage
The library needs to be configured with your account's secret key which is available on the [website](https://beta.openai.com/account/api-keys). Either set it as the `OPENAI_API_KEY` environment variable before using the library:

### Linux / MacOS Set-up

1. Run the following command in your terminal, replacing your key with your [API Keys](https://beta.openai.com/account/api-keys).
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

Or set `openai.api_key` to its value:

```python
import openai
openai.api_key = "sk-..."

# list engines
engines = openai.Engine.list()

# print the first engine's id
print(engines.data[0].id)

# create a completion
completion = openai.Completion.create(engine="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)
```