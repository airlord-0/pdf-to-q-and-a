import pymupdf

def pdf_extractor(file_path) :
    doc = pymupdf.open (file_path)
    out = ""
    for page in doc :
        out += page.get_text()
    return out

