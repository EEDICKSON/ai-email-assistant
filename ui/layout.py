import gradio as gr

def build_ui(login_fn, logout_fn, email_fn, history_fn, download_txt_fn, download_csv_fn, download_pdf_fn):
    with open("assets/style.css") as f:
        css = f.read()

    with gr.Blocks(css=css) as app:
        gr.Markdown("<h1 style='text-align:center;'>✉️ AI Email Assistant</h1>")

        with gr.Column(visible=True, elem_classes="card") as login_panel:
            username = gr.Textbox(label="Username")
            password = gr.Textbox(label="Password", type="password")
            login_btn = gr.Button("Login")
            login_msg = gr.Textbox(interactive=False, label="", elem_classes="status-msg")

        with gr.Column(visible=False, elem_classes="card") as main_panel:
            gr.Markdown("### 📝 Compose Email")
            prompt = gr.Textbox(label="Describe the situation")
            tone = gr.Dropdown(label="Select Tone", choices=["Formal", "Friendly", "Supportive", "Concise"], value="Formal")
            generate_btn = gr.Button("Generate Email")
            output_email = gr.Textbox(label="Generated Email", lines=10, interactive=False)

            gr.Markdown("### 📜 Email History")
            history_display = gr.Textbox(label="History", lines=10, interactive=False)

            with gr.Row():
                download_txt_btn = gr.Button("⬇ .txt")
                download_csv_btn = gr.Button("⬇ .csv")
                download_pdf_btn = gr.Button("⬇ .pdf")
            download_output = gr.File()

            logout_btn = gr.Button("Logout", variant="secondary")

        # Link logic
        login_btn.click(login_fn, inputs=[username, password], outputs=[login_panel, main_panel, login_msg])
        logout_btn.click(logout_fn, outputs=[login_panel, main_panel, login_msg])
        generate_btn.click(email_fn, inputs=[prompt, tone], outputs=[output_email])
        generate_btn.click(history_fn, outputs=[history_display])

        download_txt_btn.click(download_txt_fn, outputs=[download_output])
        download_csv_btn.click(download_csv_fn, outputs=[download_output])
        download_pdf_btn.click(download_pdf_fn, outputs=[download_output])

    return app
