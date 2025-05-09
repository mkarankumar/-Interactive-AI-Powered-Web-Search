from link_collection import googlesearch
from Data_colection import scrape_dynamic_website
from embeddings import embeddings, search
from langchain.llms import OpenAI 
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
import numpy as np

def search_and_respond(user_query, index, stored_chunks, embedding_model):
    embedded_query = embedding_model.encode([user_query]).astype(np.float32)
    distances, indices = index.search(embedded_query, k=5)  
    retrieved_chunks = [stored_chunks[i] for i in indices[0]]
    docs = [Document(page_content=chunk) for chunk in retrieved_chunks]
    llm = OpenAI(temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.run(input_documents=docs, question=user_query)
    return result

def chat_with_knowledge_base(index, stored_chunks, embedding_model):
    print("Ask your questions. Type 'stop' to end.\n")
    while True:
        user_query = input("You: ")
        if user_query.strip().lower() in ["stop", "end", "exit", "quit"]:
            print("Chat ended.")
            break
        try:
            response = search_and_respond(user_query, index, stored_chunks, embedding_model)
            print("LLM:", response)
        except Exception as e:
            print(f"Error: {e}")
