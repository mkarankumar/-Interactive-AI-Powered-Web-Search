from Data_collections import scrape_dynamic_website
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

#embedding the scraped data
def embeddings(text):
    text = text.strip(",")
    chunks = [text[i:i+100] for i in range(0, len(text), 100)]
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_embeddings = model.encode(chunks)
    dimension = chunk_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(chunk_embeddings))
    return index,model

#search the user input
def search(user_query, model, index, chunks, top_k=5):
    embedded_query = model.encode([user_query])
    embedded_query = np.array(embedded_query).astype("float32")
    distances, indices = index.search(embedded_query, top_k)
    results = [chunks[i] for i in indices[0]]

    return results
