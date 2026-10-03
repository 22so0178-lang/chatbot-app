import os
import subprocess
import webbrowser
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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

    if "open" in msg:
        if "command prompt" in msg or "cmd" in msg:
            try:
                subprocess.Popen("cmd.exe")
                return "Opening Command Prompt..."
            except Exception:
                return "Could not open Command Prompt"

        elif "notepad" in msg:
            try:
                subprocess.Popen("notepad.exe")
                return "Opening Notepad..."
            except Exception:
                return "Could not open Notepad"

        elif "calculator" in msg or "calc" in msg:
            try:
                subprocess.Popen("calc.exe")
                return "Opening Calculator..."
            except Exception:
                return "Could not open Calculator"

        elif "youtube" in msg:
            try:
                webbrowser.open("https://www.youtube.com")
                return "Opening YouTube..."
            except Exception:
                return "Could not open YouTube"

        elif "google" in msg:
            try:
                webbrowser.open("https://www.google.com")
                return "Opening Google..."
            except Exception:
                return "Could not open Google"

        elif "github" in msg:
            try:
                webbrowser.open("https://github.com")
                return "Opening GitHub..."
            except Exception:
                return "Could not open GitHub"

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
