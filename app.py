import os
from logic.auth import login, logout, session, users
from logic.email_gen import generate_email
from logic.history import format_history, download_txt, download_csv, download_pdf
from ui.layout import build_ui

if not os.path.exists("downloads"):
    os.makedirs("downloads")

app = build_ui(
    login_fn=login,
    logout_fn=logout,
    email_fn=generate_email,
    history_fn=format_history,
    download_txt_fn=download_txt,
    download_csv_fn=download_csv,
    download_pdf_fn=download_pdf
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))  # Render sets PORT env variable automatically
    app.launch(server_name="0.0.0.0", server_port=port)
