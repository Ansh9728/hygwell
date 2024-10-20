from langchain_core.documents.base import Document
import glob
import json
import os


# Document Loader
def load_all_json_files(directory):
    json_files = glob.glob(os.path.join(directory, "*.json"))
    documents = []
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
            documents.extend(existing_data)

    return documents


def convert_to_langchain_documents(dict_list):
    langchain_documents = [
        Document(page_content=doc['page_content'], metadata=doc['metadata']) 
        for doc in dict_list
    ]
    return langchain_documents
