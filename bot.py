from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

stored_responses = []

def call_assistant(user_message, stored_responses):
    messages = [{"role": "system", "content": "You are a professional doctor that helps clients and provides detailed analysis"}]
    for history in stored_responses:
        messages.append({"role": "user", "content": history['user']})
        messages.append({"role": "assistant", "content": history['assistant']})
    
    messages.append({"role": "user", "content": user_message})
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = completion.choices[0].message.content
    print(response)
    stored_responses.append({"user": user_message, "assistant": response})
    return response


while True:
    userInput = input("What would you like to ask the NurseBot? (Type 'exit' to exit)")
    
    if userInput.lower() == 'exit':
        print("Thank you for using NurseBot")
        break   
    
    call_assistant(userInput, stored_responses)
    
    
    
    
    