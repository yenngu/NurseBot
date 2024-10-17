from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

stored_responses = []

def call_assistant(user_message, stored_responses):
    messages = [{"role": "system", "content": "You are a professional doctor that helps clients and provides detailed analysis."}]
    for history in stored_responses:
        messages.append({"role": "user", "content": history['user']})
        messages.append({"role": "assistant", "content": history['assistant']})
    
    messages.append({"role": "user", "content": user_message})
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = completion.choices[0].message.content
    stored_responses.append({"user": user_message, "assistant": response})
    return response


@app.route('/ask', methods = ['POST'])
def ask_bot():
    data = request.get_json()
    user_message = data['message']
    response = call_assistant(user_message, stored_responses)
    return jsonify({'response': response})
    
if __name__ == '__main__':
    app.run(debug=True)
    
    