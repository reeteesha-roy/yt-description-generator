import os
from openai import OpenAI
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_title_description(video_summary):
    prompt = f"""
You are an expert YouTube content strategist.

Given this video summary: "{video_summary}"

1. Generate a short, clickable YouTube video title (max 70 characters).
2. Write a SEO-friendly, engaging description (around 100–150 words) with keywords, emojis, and hashtags if relevant.

Respond in this format:
Title: ...
Description: ...
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You help creators optimize YouTube metadata."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=300
    )

    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    title_desc = None
    if request.method == "POST":
        summary = request.form["summary"]
        title_desc = generate_title_description(summary)
    return render_template("index.html", title_desc=title_desc)

if __name__ == "__main__":
    app.run(debug=True)
