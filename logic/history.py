import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from logic.email_gen import get_history

def format_history():
    history = get_history()
    if not history:
        return "No history yet."
    return "\n\n".join([
        f"[{h['timestamp']}] ({h['user']})\nTone: {h['tone']}\nPrompt: {h['prompt']}\nResponse: {h['response']}"
        for h in history
    ])

def download_txt():
    history = get_history()
    if not history:
        return None
    path = "downloads/email_history.txt"
    with open(path, "w") as f:
        for h in history:
            f.write(f"[{h['timestamp']}] ({h['user']})\nTone: {h['tone']}\nPrompt: {h['prompt']}\nResponse: {h['response']}\n\n")
    return path

def download_csv():
    history = get_history()
    if not history:
        return None
    df = pd.DataFrame(history)
    path = "downloads/email_history.csv"
    df.to_csv(path, index=False)
    return path

def download_pdf():
    history = get_history()
    if not history:
        return None
    path = "downloads/email_history.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter
    y = height - 40
    for h in history:
        for line in [
            f"[{h['timestamp']}] ({h['user']})",
            f"Tone: {h['tone']}",
            f"Prompt: {h['prompt']}",
            f"Response: {h['response']}", ""
        ]:
            c.drawString(40, y, line)
            y -= 16
            if y < 40:
                c.showPage()
                y = height - 40
    c.save()
    return path
