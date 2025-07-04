import os
from openai import OpenAI
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_title_description(video_summary):
    prompt = f"""
You are an expert YouTube content strategist. Given the script or summary of a video, generate the following:

1. A **catchy, click-worthy video title** (max 100 characters)
2. An **SEO-optimized video description** (1–2 paragraphs)
3. Optionally include **3–5 relevant hashtags** at the end of the description

Make sure the title:
- Hooks the viewer emotionally or intellectually
- Avoids clickbait
- Fits within YouTube's mobile display limit (70–100 characters)

Make sure the description:
- Includes **target keywords**
- Summarizes the value of the video clearly
- Uses natural, engaging tone


Respond in this format:
Title: ...
Description: ...
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that formats YouTube metadata."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=500
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
