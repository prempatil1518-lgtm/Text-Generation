# AI Question–Answer System — FLAN-T5

This project is based on the uploaded `EXPGENAI3.ipynb` notebook.

## What it does
A Gradio web interface accepts a question and uses Google's pre-trained
`google/flan-t5-base` model to generate an answer.

## Requirements
- Python 3.9–3.12 recommended
- Internet connection for the first model download
- GPU is optional. The application automatically uses CUDA when available
  and otherwise runs on CPU.

## Run on Windows

1. Extract this ZIP file.
2. Open Command Prompt/PowerShell inside the extracted folder.
3. Create a virtual environment:

   `python -m venv venv`

4. Activate it:

   PowerShell:
   `venv\Scripts\Activate.ps1`

   Command Prompt:
   `venv\Scripts\activate`

5. Install dependencies:

   `pip install -r requirements.txt`

6. Start the application:

   `python app.py`

7. Open the Gradio link shown in the terminal (usually
   `http://127.0.0.1:7860`).

## Run the original notebook
Open `EXPGENAI3.ipynb` in Jupyter Notebook or Google Colab and run the
cells in order. The notebook itself installs the required packages.

## Important
The FLAN-T5 model is downloaded from Hugging Face the first time the
program runs, so the first startup can take some time and requires
internet access. The model is not bundled inside this ZIP.
