from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from your frontend

# Set your OpenAI API key
openai.api_key = "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"


# Root route to handle the homepage (this will prevent 404 on /)
@app.route('/')
def index():
    return "Welcome to the Chatbot API! Access the /chat endpoint to communicate with the chatbot."

# Define the chat route for handling messages
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if user_message:
        try:
            # Send the user's message to the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )

            # Extract the chatbot's response
            bot_reply = response.choices[0].message['content']

            return jsonify({"reply": bot_reply})
        except Exception as e:
            print(f"Error: {e}")  # Log the error for debugging
            return jsonify({"reply": "Sorry, there was an error processing your request."}), 500

    return jsonify({"reply": "No message provided."}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
