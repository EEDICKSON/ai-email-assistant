import gradio as gr

# Session state
session = {"logged_in": False, "username": None}

# Dummy user DB
users = {
    "admin": "admin123",
    "eric": "1234"
}

def login(username, password):
    if users.get(username) == password:
        session["logged_in"] = True
        session["username"] = username
        return gr.update(visible=False), gr.update(visible=True), f"✅ Welcome {username}!"
    return gr.update(visible=True), gr.update(visible=False), "❌ Login failed. Check credentials."

def logout():
    session["logged_in"] = False
    session["username"] = None
    return gr.update(visible=True), gr.update(visible=False), ""
