class PromptLoader:
    """
    Designed for parsing and formatting chat transcripts or text content
    for use with OpenAI's Completion and ChatCompletion classes.

    Depending on the content of the input text, it decides to parse it as a chat transcript or a plain text string.

    A chat transcript should look like this:

    System: You are a technical support specialist. Assist the user.
    User: I need assistance with my device.
    Assistant: I'm here to help. Could you tell me more about the issue?

    Attributes:
        text (str): The original input text.
        prompt (list or str): The parsed prompt. If the input text is a chat transcript,
            this will be a list of dictionaries where each dictionary represents a single message.
            If the input text is a plain string, this will be the original string with \n
            characters preserved.

    Properties:
        content (str or list): Access this to get the output as either a repr string or a list of dictionaries,
            depending on the format of the input text. If the input text is a chat transcript, you get a list of
            dictionaries. If the input text is a plain string, you get a repr string with \n characters preserved.
        
        str_pretty (str): A property that provides a string representation of the prompt. If the input text is a 
            chat transcript, it formats the messages in a user-friendly way. If the input text is a plain string, 
            it replaces \n with actual newlines for better readability.

    Methods:
        load_chat(): Parses the input text as a chat transcript.
        load_completion(): Returns the input text as a string with \n characters preserved.
    """
    
    def __init__(self, text):
        self.text = text
        # Check for chat handles to determine if the input is a chat prompt or completion prompt
        if any(keyword in text for keyword in ["User:", "System:", "Assistant:"]):
            self.prompt = self.load_chat()
        else:
            self.prompt = self.load_completion()
    
    # If chat handles are detected, load as a standard JSON compatible with OpenAI
    def load_chat(self):
        messages = []
        roles = ["system", "user", "assistant"]

        current_role = None
        current_lines = []

        lines = iter(self.text.split('\n'))  # make lines iterable
        for line in lines:
            stripped_line = line.strip()

            for role in roles:
                if stripped_line.lower().startswith(role + ": "):
                    if current_role is not None:
                        # Join the current lines with '\n' to preserve newlines within a message
                        content = '\\n'.join(current_lines).strip()
                        # Remove trailing newlines
                        while content.endswith('\\n'):
                            content = content[:content.rfind('\\n')]
                        messages.append({
                            "role": current_role,
                            "content": content
                        })
                    current_role = role
                    current_lines = [stripped_line[len(role)+2:]]
                    break
            else:
                # If the line doesn't start with a role, treat it as a continuation of the current message
                current_lines.append(stripped_line)

        if current_role is not None:
            content = '\\n'.join(current_lines).strip()
            # Remove trailing newlines
            while content.endswith('\\n'):
                content = content[:content.rfind('\\n')]
            messages.append({
                "role": current_role,
                "content": content
            })

        return messages

    # If no chat handles are found, load as a completion prompt (string with escape newlines)
    def load_completion(self):
        lines = self.text.split('\n')
        lines = [line.replace('\r', '') for line in lines]
        content = '\\n'.join(lines)
        return content
    
    def prompt_to_str(self):
        formatted_prompt = []
        for message in self.prompt:
            formatted_content = message['content'].encode('unicode_escape').decode().replace('\\\\', '\\')
            formatted_prompt.append(f"{{'role': '{message['role']}', 'content': '{formatted_content}'}}")
        return '[' + ', '.join(formatted_prompt) + ']'
    
    # Contains either a list of dictionaries for chat prompts, or a string for completion prompts
    @property
    def content(self):
        if isinstance(self.prompt, list):
            return self.prompt
        else:
            return repr(self)[1:-1]
    
    # Printable format similar to the origin input format
    @property
    def str_pretty(self):
        if isinstance(self.prompt, str):
            return self.prompt.replace('\\n', '\n')
        else:
            formatted_prompt = ['{}: {}'.format(message["role"].capitalize(), message["content"].replace("\\n", "\n")) for message in self.prompt]
            return '\n'.join(formatted_prompt)

    def __str__(self):
        if isinstance(self.prompt, list):
            return self.prompt_to_str()
        else:
            return self.prompt

    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        if isinstance(self.prompt, str):
            yield self.prompt.replace('\\n', '\n')
        else:
            for message in self.prompt:
                yield message
