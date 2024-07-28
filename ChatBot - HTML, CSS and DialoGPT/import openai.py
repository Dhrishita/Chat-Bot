import openai
openai.api_key = "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"
def chat_wiht_gpt(prompt):
    response=open.ai.ChatCompletion.create(
        mode="gpt-3.5-turbo",
        messages=[{"role":"user", "content" : prompt}]
    )
    return response.choices[0].message.content.strip()
if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            breakresponse = chat_wiht_gpt(user_input)
            print("Chatbot: ",response)