import openai

#put your own API Key here
openai.api_key = "sk-"

def chat_with_me(prompt):
    #model is current model
    #role:system can be removed to have regular chatbot
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        # you can test out what ever "personality" you want your assistant to have
        messages=[{"role":"system", "content": "you are a sassy assistant"},
                  {"role":"user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        uinput = input("Me: ")
        if uinput.lower() in ["quit","exit", "stop", "bye"]:
            break
        response = chat_with_me(uinput)
        print("Assistant: ", response)
