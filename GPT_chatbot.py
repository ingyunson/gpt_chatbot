import openai

openai.api_key = "[YOUR_OPENAI_API]"

chat_history = [{"role": "system", "content": "You are a assistant."}]

def bot_message(input):
    chat_history.append({"role": "user", "content": f"{input}"})
    chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chat_history
    )

    return chat

def start_conversation():
    print("Hi, I'm a chatbot. How can I help you today?")
    token_count = 0
    while True:
        user_input = input("> ")
        prompt = f"{user_input}"
        response = bot_message(prompt)
        role = response.choices[0].message.role
        answer = response.choices[0].message.content
        
        return_message = f"BOT : {answer}"
        history_message = {"role": f'{role}', "content": f"{answer}"}
        chat_history.append(history_message)

        completion_token = response.usage.completion_tokens
        prompt_token = response.usage.prompt_tokens
        used_tokens = completion_token + prompt_token
        token_count = token_count + used_tokens

        token_message = f"In this conversation, you use {used_tokens} tokens. Completion : {completion_token}, Prompt : {prompt_token}"
        total_token_message = f"You used {token_count} Tokens"

        print(return_message)
        print(token_message)
        print(total_token_message)
        
    
start_conversation()