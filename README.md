# PromptLoader

A Python utility designed to streamline the process of managing and editing prompts for OpenAI's Completion and ChatCompletion classes.

In Python, extensive text strings, often seen in OpenAI prompts, require escaped newline characters (\\n). This often results in long lines of text in code editors, disrupting the reading flow and making editing cumbersome. This tool mitigates this issue by interpreting text inputs, identifying them as either a chat transcript or completion (used in text-davinci-003), and automatically formatting them accordingly. This functionality enables easier prompt creation by editing a .txt file before loading them into Python.

The parsed prompts are formatted for use with the OpenAI API or Python package.

## Installation
```bash
pip install git+https://github.com/johnballentine/prompt_loader.git
```

## Writing Chat Transcripts in Plain Text
```text
System: You are a technical support specialist. Assist the user.
User: I need assistance with my device.
Assistant: I'm here to help. Could you tell me more about the issue?
```

### The above plain text will be parsed into a list of dictionaries compatible with the OpenAI ChatCompletion <i>messages</i> parameter:
```python
[
    {"role": "system", "content": "You are a technical support specialist. Assist the user."},
    {"role": "user", "content": "I need assistance with my device."},
    {"role": "assistant", "content": "I'm here to help. Could you tell me more about the issue?"}
]
```

## Usage
```python
from prompt_loader import PromptLoader

with open("chat_transcript.txt", "r") as file:
    text = file.read()

# Create a PromptLoader instance with the text from the file
loader = PromptLoader(text)

print(loader.content) # Either a string or list depending on completion or chat
print(loader.str_pretty) # Formats a chat or completion in a human-readable way
print(loader) # Prints as a string in either case
```
Depending on the content of the text, it will parse it as a chat transcript or as a plain text string.

## Features
- Type conversion with strings, lists, etc.
- Preserves newlines in messages but not in-between messages in chat transcripts.
- Parses a plain text string from completion prompts, preserving newline characters.
- Simple API with easy type conversion and formatting properties.

## License
This project is licensed under the MIT License.
