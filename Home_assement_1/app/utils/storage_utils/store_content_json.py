
import os
import json
from ..data_cleaning.content_cleaner import clean_content
from langchain_core.documents.base import Document
from datetime import datetime

def get_langchain_document(file_content):
    documents = []
    for filename, file_text in file_content.items():
        document = Document(
            page_content=file_text,
            metadata={
                "source": filename,
                "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            }
        )
        documents.append(document)
    return documents


def store_content(file_content, directory=None):
    try:
        if directory is None:
            directory = os.getenv("DATA_DIRECTORY", os.path.join(os.getcwd(), "Data_Folder"))

        clean_file_content = clean_content(file_content)

        langchain_documents = get_langchain_document(clean_file_content)  # make the langchain documents

        os.makedirs(directory, exist_ok=True)

        output_file = os.path.join(directory, "output_file.json")

        # Initialize the data list
        existing_data = []

        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)

        # Append new documents to the existing data list
        existing_data.extend([doc.__dict__ for doc in langchain_documents])  # Convert to dict before appending

        # Write the updated data back to the file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

        print(f"Data has been appended to {output_file}")
        return True

    except Exception as e:
        print(f"Error occurred: {e}")
        return False
