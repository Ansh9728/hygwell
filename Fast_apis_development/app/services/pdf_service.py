from app.utils.pdf_utils.pdf_parser import extract_pdf_content


def process_pdf(files: list):

    files_data = {}

    for file in files:
        filename = file.filename
        
        if filename.endswith('.pdf'):
            text = extract_pdf_content(file)
            files_data[filename] = text

    return files_data