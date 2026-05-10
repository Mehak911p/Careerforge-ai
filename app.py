from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=f"""
            You are CareerForge AI.
            Help users with:
            - UK jobs
            - CV improvement
            - interview preparation
            - sponsorship guidance
            - cover letters

            User message:
            {user_msg}
            """
        )

        reply = response.output_text

    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
