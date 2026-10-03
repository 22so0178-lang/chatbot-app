import os
import subprocess
import webbrowser
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("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"))

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

    # Check for open commands FIRST
    if "open" in msg:
        if "command prompt" in msg or "cmd" in msg:
            try:
                subprocess.Popen("cmd.exe")
                return "Opening Command Prompt..."
            except:
                return "Could not open Command Prompt"
        
        elif "notepad" in msg:
            try:
                subprocess.Popen("notepad.exe")
                return "Opening Notepad..."
            except:
                return "Could not open Notepad"
        
        elif "calculator" in msg or "calc" in msg:
            try:
                subprocess.Popen("calc.exe")
                return "Opening Calculator..."
            except:
                return "Could not open Calculator"
        
        elif "youtube" in msg:
            try:
                webbrowser.open("https://www.youtube.com")
                return "Opening YouTube..."
            except:
                return "Could not open YouTube"
        
        elif "google" in msg:
            try:
                webbrowser.open("https://www.google.com")
                return "Opening Google..."
            except:
                return "Could not open Google"
        
        elif "github" in msg:
            try:
                webbrowser.open("https://github.com")
                return "Opening GitHub..."
            except:
                return "Could not open GitHub"
        
        elif "facebook" in msg:
            try:
                webbrowser.open("https://www.facebook.com")
                return "Opening Facebook..."
            except:
                return "Could not open Facebook"
        
        elif "twitter" in msg or "x.com" in msg:
            try:
                webbrowser.open("https://www.twitter.com")
                return "Opening Twitter..."
            except:
                return "Could not open Twitter"

    # For other questions, use OpenAI
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
