from prompt_loader import PromptLoader

# Test Chat
with open('samples/chat_test.txt', 'r') as file:
    transcript = file.read()

chat_prompt = PromptLoader(transcript)

print(f"\n\nChat Prompt:\n\n{chat_prompt}")

# Test Completion
with open('samples/completion_test.txt', 'r') as file:
    text = file.read()

completion_prompt = PromptLoader(text)

print(f"\n\nCompletion Prompt:\n\n{completion_prompt}")