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

Here is the video summary:
\"\"\"{video_summary}\"\"\"

Respond in this format:
Title: <your generated title>
Description:<your generated description>
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
    title_text = ""
    desc_text = ""
    
    if request.method == "POST":
        summary = request.form["summary"]
        full_output = generate_title_description(summary)

        # Check if both 'Title:' and 'Description:' exist in the output
        if "Title:" in full_output and "Description:" in full_output:
            try:
                title_text = full_output.split("Title:")[1].split("Description:")[0].strip()
                desc_text = full_output.split("Description:")[1].strip()
            except IndexError:
                title_text = "⚠️ Couldn't extract title. Please try again."
                desc_text = "⚠️ Couldn't extract description. Please try again."
        else:
            title_text = "⚠️ Unexpected format from AI. Please try again."
            desc_text = full_output  # Show full output for debugging

    return render_template("index.html", title=title_text, description=desc_text)

# To run locally
if __name__ == "__main__":
   app.run(debug=True) 
