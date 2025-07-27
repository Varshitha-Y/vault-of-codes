from flask import Flask, request, render_template
from dotenv import load_dotenv
import google.generativeai as genai
import os

app = Flask(__name__)

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_ai_response(user_input, mode, model_name):
    if mode == "question":
        prompt = f"Answer this question clearly: {user_input}"
    elif mode == "summary":
        prompt = f"Summarize the following:\n{user_input}"
    elif mode == "creative":
        prompt = f"Write a short story or poem about: {user_input}"
    else:
        prompt = user_input

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        mode = request.form["mode"]
        model_name = request.form["model"]
        feedback = request.form.get("feedback", "")

        if feedback:
            with open("feedback_log.txt", "a") as f:
                f.write(f"Feedback: {feedback}\n")

        response = get_ai_response(user_input, mode, model_name)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
