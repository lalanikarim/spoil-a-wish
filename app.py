import gradio as gr
import os
from agent import WishSpoiler

account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
api_token = os.getenv("CLOUDFLARE_API_TOKEN")
model_name = os.getenv("MODEL_NAME", "@cf/meta/llama-3.1-70b-instruct")

wish_spoiler = WishSpoiler(account_id, api_token, model_name)

def spoil_wish(wish: str):
    wish_response = wish_spoiler.spoil_wish(wish)
    return wish_response.result.response


with gr.Blocks(css="""
    .gradio-container {
        display: flex;
        flex-direction: column;
        max-width: 1000px !important;
    }
    .btn.success {
        background-color: #4CAF50;
        color: white;
    }
    .btn.danger {
        background-color: #F44336;
        color: white;
    }
""") as demo:
    gr.HTML("""
    <center>
      <h1>Spoil-A-Wish</h1>
    </center>
    """)
    with gr.Row():
        with gr.Column():
            user_wish = gr.TextArea(label="Wish")
            spoiler_response = gr.TextArea(label="Spoiler Response", visible=False)
            submit = gr.Button("Spoil Wish", elem_classes="btn success")
            reset = gr.Button("Try Again!", elem_classes="btn danger", visible=False)

    gr.Examples(
        examples=[
            ["I wish for a million dollars"],
            ["I wish for a new car"],
            ["I wish for a new house"],
            ["I wish for a new job"]
        ],
        inputs=[user_wish],
        label="Try these"

    )

    gr.on(
        triggers=submit.click,
        outputs=[user_wish, spoiler_response, submit],
        fn=lambda: [gr.TextArea(interactive=False), gr.TextArea(visible=True), gr.Button(visible=False)],
        api_name=False
    ).then(
        fn=spoil_wish,
        inputs=user_wish,
        outputs=spoiler_response
    ).then(
        outputs=reset,
        fn=lambda: gr.Button(visible=True),
        api_name=False
    )
    gr.on(
        triggers=reset.click,
        outputs=[spoiler_response, reset, user_wish, submit],
        fn=lambda: [gr.TextArea(visible=False), gr.Button(visible=False), gr.TextArea(interactive=True, value=None),
                    gr.Button(visible=True)],
        api_name=False
    )


if __name__ == "__main__":
    demo.launch()