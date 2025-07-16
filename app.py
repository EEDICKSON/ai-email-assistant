from logic.auth import login, logout, session, users
from logic.email_gen import generate_email
from logic.history import format_history, download_txt, download_csv, download_pdf
from ui.layout import build_ui
import os

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
    app.launch()
