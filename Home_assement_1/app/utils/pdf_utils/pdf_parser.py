from PyPDF2 import PdfReader
from io import BytesIO


def extract_pdf_content(file):

    file_content = file.file.read()
    
    pdf_stream = BytesIO(file_content)

    reader = PdfReader(pdf_stream)

    page_text = ''
    
    for page in reader.pages:

        text = page.extract_text()
        page_text+=text

    return page_text


# path = "/home/ansh/Downloads/learn-computer-vision-using-opencv-with-deep-learning-cnns-and-rnns-1st-ed-978-1-4842-4260-5978-1-4842-4261-2_compress.pdf"
# pa = extract_pdf_content(path)
# print(pa)