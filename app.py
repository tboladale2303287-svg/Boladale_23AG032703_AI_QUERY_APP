from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        api_key = os.getenv("GEMINI_API_KEY")
        # Call Gemini API here and get the answer
        answer = "This is where the AI response will go."
    return render_template("index.html", answer=answer)
