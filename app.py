from flask import Flask, render_template, request, jsonify
import openai
import subprocess
import webbrowser
import os

app = Flask(__name__)

# Add your OpenAI API key here
openai.api_key = "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"

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

    # Open apps/websites
    if "open" in msg:
        if "command prompt" in msg or "cmd" in msg:
            subprocess.Popen("cmd.exe")
            return "Opening Command Prompt..."
        elif "notepad" in msg:
            subprocess.Popen("notepad.exe")
            return "Opening Notepad..."
        elif "calculator" in msg or "calc" in msg:
            subprocess.Popen("calc.exe")
            return "Opening Calculator..."
        elif "youtube" in msg:
            webbrowser.open("https://www.youtube.com")
            return "Opening YouTube..."
        elif "google" in msg:
            webbrowser.open("https://www.google.com")
            return "Opening Google..."
        elif "github" in msg:
            webbrowser.open("https://www.github.com")
            return "Opening GitHub..."
        elif "facebook" in msg:
            webbrowser.open("https://www.facebook.com")
            return "Opening Facebook..."
        elif "twitter" in msg or "x.com" in msg:
            webbrowser.open("https://www.twitter.com")
            return "Opening Twitter..."

    # Try to use OpenAI for any question
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
