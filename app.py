from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    
    if not user_message:
        return jsonify({"reply": "Please type a message."})
    
    response = generate_reply(user_message)
    return jsonify({"reply": response})

def generate_reply(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you today?"
    elif "how are you" in msg:
        return "I'm doing great, thanks for asking!"
    elif "name" in msg:
        return "I'm your chatbot assistant."
    elif "bye" in msg or "goodbye" in msg:
        return "Goodbye! Have a great day."
    else:
        return "Thanks for your message! I’m here to help."

if __name__ == "__main__":
    app.run(debug=True)
