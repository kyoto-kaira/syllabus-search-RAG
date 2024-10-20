from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import pickle

path = 'data2\shirabasu_texts.pkl'
with open(path, 'rb') as f:
    texts = pickle.load(f)

ids = [str(i) for i in range(len(texts))]

embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

vectorstore = FAISS.from_texts(texts,embedding, ids = ids)