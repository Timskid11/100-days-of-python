from pypdf import PdfReader
import tkinter as tk
from tkinter import filedialog
from gtts import gTTS


# Select PDF file
def select_pdf():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=(("PDF Files", "*.pdf"),)
    )
    root.destroy()
    return file_path


# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  # avoid None
            text += page_text

    return text


# Main program
pdf_path = select_pdf()

if pdf_path:
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text.strip():
        tts = gTTS(text=pdf_text, lang="en", slow=False)

        root = tk.Tk()
        root.withdraw()
        audio_path = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=(("MP3 files", "*.mp3"),),
            title="Save audio file"
        )
        root.destroy()

        if audio_path:
            tts.save(audio_path)
            print("✅ Successfully converted PDF to speech!")
    else:
        print("❌ No readable text found in the PDF.")
else:
    print("❌ No PDF selected.")
