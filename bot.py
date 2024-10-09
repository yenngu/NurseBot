from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def call_assistant(user_message):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role" :"system", "content": "You are a personal nurse, skilled in the medical field. Only respond if it's medical related."},
            {"role" :"user", "content": user_message}
        ]   
    )

    response = completion.choices[0].message.content
    print(response)
    return response

call_assistant(input("What would you like to ask NurseBot?"))