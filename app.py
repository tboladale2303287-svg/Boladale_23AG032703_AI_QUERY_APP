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
     import google.generativeai as genai

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(question)
answer = response.text

    return render_template("index.html", answer=answer)
