import re

def clean_content(file_content:dict):
    
    cleaned_content = {}

    for filename, text_content in file_content.items():

        # strip_text = text_content.strip()
        # strip_text.replace(" ", '').replace('\n', '')
        content = re.sub(r'\n+', '\n', text_content)
        content = re.sub(r'\s+', ' ', content)
        content = content.strip()

        cleaned_content[filename] = content

    return cleaned_content