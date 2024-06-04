
from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "memory-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=8, # Replace with your model dimensions
        metric="cosine", # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
    )