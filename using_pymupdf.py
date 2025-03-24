import fitz  # PyMuPDF

def extract_highlights(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    highlighted_texts = []

    for page in doc:
        for annot in page.annots():
            if annot.type[0] == 8:  # Check if annotation is a highlight
                rect = annot.rect  # Get the bounding box of the annotation
                text = page.get_text("text", clip=rect)  # Extract text inside highlight
                if text.strip():
                    highlighted_texts.append(text.strip())

    if highlighted_texts:
        with open(output_txt_path, "w", encoding="utf-8") as f:
            for text in highlighted_texts:
                f.write(text + "\n\n")
        print(f"Extracted highlights saved to {output_txt_path}")
    else:
        print("No highlights found!")

# Example usage
extract_highlights("FGV-DAPP-2020-A-economia-de-Roraima-e-o-fluxo-vene_250323_141023.pdf", "highlights.txt")
