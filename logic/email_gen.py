import openai
from datetime import datetime
from logic.auth import session

openai.api_key = os.getenv("OPENAI_API_KEY")
history = []

def generate_email(prompt, tone):
    if not session["logged_in"]:
        return "⚠️ Please log in first."
    formatted_prompt = f"Write a {tone.lower()} professional email for the following situation:\n\n{prompt}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=formatted_prompt,
        max_tokens=300
    )
    reply = response.choices[0].text.strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        "timestamp": timestamp,
        "user": session["username"],
        "prompt": prompt,
        "tone": tone,
        "response": reply
    })
    return reply

def get_history():
    return history
