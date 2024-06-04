from langchain_community.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import Anthropic
from langchain.chains import ConversationChain
import pinecone
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Create an instance of the PineconeVectorStore class
# pinecone_instance = PineconeVectorStore(api_key=os.getenv("PINECONE_API_KEY"))
pinecone_instance = PineconeVectorStore()

index_name = "chatbot_index"

# Initialize OpenAI Embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Initialize Pinecone Vector Store
vectorstore = pinecone_instance.Index(index_name, embeddings)

# Initialize Claude3-Opus
llm = Anthropic(model="claude-3-sonnet-20240229")

# Initialize the ConversationChain
conversation = ConversationChain(llm=llm)

# Chat loop
while True:
    user_input = input("User: ")
    
    # Exit the chat if user types 'exit'
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    # Generate response using Claude3-Opus
    response = conversation.predict(input=user_input)
    print(f"Chatbot: {response}")
    
    # Create embeddings for user input and chatbot response
    user_embedding = embeddings.embed_query(user_input)
    response_embedding = embeddings.embed_query(response)
    
    # Store embeddings in Pinecone
    vectorstore.upsert(ids=[user_input], vectors=[user_embedding], metadata=[{"type": "user"}])
    vectorstore.upsert(ids=[response], vectors=[response_embedding], metadata=[{"type": "chatbot"}])
