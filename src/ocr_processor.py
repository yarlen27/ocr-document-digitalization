import os
import subprocess

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def apply_ocr_to_pdf(pdf_filename):
    input_path = os.path.join(INPUT_FOLDER, pdf_filename)
    output_path = os.path.join(OUTPUT_FOLDER, pdf_filename.replace(".pdf", "_ocr.pdf"))

    command = [
        "ocrmypdf",
        "--optimize", "3",
        "--deskew",
        "--output-type", "pdf",
        input_path,
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"OCR aplicado a: {pdf_filename}")
    except subprocess.CalledProcessError:
        print(f"❌ Error al procesar: {pdf_filename}")

def main():
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith(".pdf"):
            apply_ocr_to_pdf(file)

if __name__ == "__main__":
    main()
