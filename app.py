from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
       user_message = request.form.get("message", "")
       image = request.files.get("image") 

       response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                ...
                {
                    "role": "system",
                    "content": "You are CareerForge AI, a smart career assistant helping people with jobs, CVs, interview tips, career advice, software development learning, and skill development."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)
