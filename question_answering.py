import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load cleaned data
df = pd.read_csv("app/data/cleaned_booking_data.csv")

# Load model & encode data
model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = df.apply(lambda x: f"{x['hotel']} booking on {x['arrival_date']} with price {x['adr']}", axis=1)
embeddings = model.encode(sentences.to_list())

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings, dtype='float32'))

def get_answer(query, top_k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding, dtype='float32'), top_k)
    results = df.iloc[indices[0]]
    return results[['hotel', 'arrival_date', 'adr']].to_dict(orient='records')
