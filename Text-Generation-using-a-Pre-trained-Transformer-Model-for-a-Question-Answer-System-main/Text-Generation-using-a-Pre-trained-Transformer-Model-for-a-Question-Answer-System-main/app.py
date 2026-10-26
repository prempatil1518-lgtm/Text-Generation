import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import gradio as gr

MODEL_ID = "google/flan-t5-base"
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device:", device)

print("Loading FLAN-T5 model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
model = model.to(device)
print("Model loaded successfully!")

def answer_question(question, max_new_tokens=150):
    if not question or not question.strip():
        return "Please enter a question."

    prompt = (
        "Answer the following question clearly and accurately. "
        "If the question is asking for an explanation, explain it in simple language. "
        "Question: " + question
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=int(max_new_tokens),
            num_beams=4,
            early_stopping=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def qa_interface(question, max_new_tokens):
    return answer_question(question, max_new_tokens)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# AI Question–Answer System")
    gr.Markdown(
        "Enter a question below and the pre-trained FLAN-T5 model will generate an answer."
    )

    with gr.Row():
        with gr.Column():
            question_box = gr.Textbox(
                label="Enter Your Question",
                placeholder="Example: What is artificial intelligence?",
                lines=4
            )
            max_tokens = gr.Slider(
                minimum=30,
                maximum=300,
                value=150,
                step=10,
                label="Maximum Answer Length"
            )
            with gr.Row():
                ask_btn = gr.Button("Ask Question")
                clear_btn = gr.ClearButton()

        with gr.Column():
            answer_box = gr.Textbox(
                label="Generated Answer",
                lines=12
            )

    ask_btn.click(
        fn=qa_interface,
        inputs=[question_box, max_tokens],
        outputs=answer_box
    )
    clear_btn.add([question_box, answer_box])

if __name__ == "__main__":
    demo.launch()
