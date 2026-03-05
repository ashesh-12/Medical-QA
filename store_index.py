import os
from dotenv import load_dotenv
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.helper import download_embeddings, filter_to_minimal_docs, load_pdf_files, text_split


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


extracted_data = load_pdf_files("data/")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)


embeddings = download_embeddings()

Pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=Pinecone_api_key)


index_name = "medical-qa"

existing_indexes = [i.name for i in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine", 
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name
)