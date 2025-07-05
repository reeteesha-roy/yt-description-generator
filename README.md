# YouTube Video Title & Description Generator
This YouTube Title & Description Generator harnesses the power of OpenAI's GPT-4o-mini to create engaging, SEO-optimized content for content creators. The application features real-time character counting with color-coded warnings to ensure compliance with YouTube's limits, one-click copy functionality for seamless workflow integration, and built-in optimization tips based on YouTube best practices.

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key
- Git (optional)

## Project Structure
  yt-generator/
├── 📄 app.py                    # Flask backend application
├── 📁 templates/
│   └── 📄 index.html           # Main HTML template with AI output display
├── 📁 static/
│   └── 📄 styles.css           # Enhanced CSS with responsive design
├── 📄 .env                     # Environment variables (API keys)
├── 📄 requirements.txt         # Python dependencies
└── 📄 README.md               # Project documentation

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/yt-description-generator.git
cd yt-description-generator
```

## Step 2: Set Up a Virtual Environment

```bash
python -m venv venv
```

### Activate the environment

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Set the OpenAI API Key

Create a `.env` file in the root directory and add the following line:

```env
OPENAI_API_KEY=your-api-key-here
```

You can get your API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

## Step 5: Run the Application

```bash
python app.py
```

Once the server is running, open your browser and go to:

```
http://127.0.0.1:5000
```

The app is now ready to use.

