import fitz

def check_annotations(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc):
        annots = list(page.annots())
        if annots:
            print(f"Page {page_num + 1} has {len(annots)} annotations.")
        else:
            print(f"Page {page_num + 1} has no annotations.")

check_annotations("FGV-DAPP-2020-A-economia-de-Roraima-e-o-fluxo-vene_250323_141023.pdf")
