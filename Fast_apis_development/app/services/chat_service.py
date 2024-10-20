import os
from app.utils.chat_utils.vectordb import get_vectordb

def generate_chat_response(chat_id, user_message):

    if user_message:
        vector_index = get_vectordb()
        retriever = vector_index.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k":5, 'score_threshold': 0.8}
        )
        similar_docs = retriever.get_relevant_documents(user_message)

        # print("similar_docs", similar_docs)
        if similar_docs:
            return similar_docs
        return f"Not any similar docs of question : {user_message}"
    
    return f"Question is Null"
    
    