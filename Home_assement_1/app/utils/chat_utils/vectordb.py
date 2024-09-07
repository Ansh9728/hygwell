# import os
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from document_loaders import load_all_json_files, convert_to_langchain_documents


# def get_chunk_docs(documents):
#     text_splitter = RecursiveCharacterTextSplitter(
#         # Set a really small chunk size, just to show.
#         chunk_size=1000,
#         chunk_overlap=200,
#         length_function=len,
#         is_separator_regex=False,
#     )
#     docs = text_splitter.split_documents(documents)
#     return docs


# def create_vector_index(document_chunks, embedding_model):
#     # Initialize the vector index using FAISS
#     vector_index = FAISS.from_documents(document_chunks, embedding_model)
#     return vector_index


# def save_vector_index(file_path, document_chunks, embedding_model):
#     # Save the vector index to the specified file path
#     try:
#       if not os.path.exists(file_path):

#           print(f"Vector_index_creating at location : {file_path}")
#           vector_index = create_vector_index(document_chunks, embedding_model)

#           vector_index.save_local(file_path)
#           print('Saved Succusfully')

#       # Load the vector index from the saved file

#       print(f"Loading Vector_index Embedding Present")
#       new_vector_index = FAISS.load_local(file_path, embedding_model, allow_dangerous_deserialization=True)

#       return new_vector_index

#     except Exception as e:
#       print('Exception occured ',e)
#       # vector_index.save_local(file_path)

# model_name = "Snowflake/snowflake-arctic-embed-s"
# encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

# base_embedding_model = HuggingFaceEmbeddings(
#     model_name=model_name,
#     encode_kwargs=encode_kwargs
# )


# def get_embedding_model(base_embedding_model):
#    return base_embedding_model


# embedding_model = get_embedding_model(base_embedding_model)
# directory = os.getenv("DATA_DIRECTORY", os.path.join(os.getcwd(), "Data_Folder"))

# documents_dict = load_all_json_files(directory)
# documents = convert_to_langchain_documents(documents_dict)
# documents_chunks = get_chunk_docs(documents)
# print("document_chunks", documents_chunks)
# vector_index_path = directory
# save_vector_index(vector_index_path, documents_chunks, embedding_model)

import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .document_loaders import load_all_json_files, convert_to_langchain_documents


def get_chunk_docs(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    docs = text_splitter.split_documents(documents)
    return docs


def create_vector_index(document_chunks, embedding_model):
    # Initialize the vector index using FAISS
    vector_index = FAISS.from_documents(document_chunks, embedding_model)
    return vector_index


def save_vector_index(file_path, document_chunks, embedding_model):
    try:
        index_file = os.path.join(file_path, "index.faiss")
        if not os.path.exists(index_file):
            print(f"Vector index creating at location: {file_path}")
            vector_index = create_vector_index(document_chunks, embedding_model)
            vector_index.save_local(file_path)
            print('Saved successfully')
        else:
            print(f"Loading Vector index Embedding from: {file_path}")
            vector_index = FAISS.load_local(file_path, embedding_model, allow_dangerous_deserialization=True)

        return vector_index

    except Exception as e:
        print('Exception occurred:', e)
        return None


model_name = "Snowflake/snowflake-arctic-embed-s"
encode_kwargs = {'normalize_embeddings': True}

base_embedding_model = HuggingFaceEmbeddings(
    model_name=model_name,
    encode_kwargs=encode_kwargs
)

def get_embedding_model(base_embedding_model):
    return base_embedding_model

embedding_model = get_embedding_model(base_embedding_model)

# directory = os.getenv("DATA_DIRECTORY", os.path.join(os.getcwd(), "Data_Folder"))
# documents_dict = load_all_json_files(directory)
# documents = convert_to_langchain_documents(documents_dict)
# documents_chunks = get_chunk_docs(documents)
# vector_index_path = directory

# # Save or load vector index
# save_vector_index(vector_index_path, documents_chunks, base_embedding_model)

def get_vectordb():

    directory = os.getenv("DATA_DIRECTORY", os.path.join(os.getcwd(), "Data_Folder"))
    
    vector_index_path = os.path.join(directory,"faiss_index")

    documents_dict = load_all_json_files(directory)
    
    documents = convert_to_langchain_documents(documents_dict)
    
    documents_chunks = get_chunk_docs(documents)

    # Save or load vector index
    vector_index = save_vector_index(vector_index_path, documents_chunks, embedding_model)
    print(vector_index)
    return vector_index