from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import json

with open('db/data2/syllabus_texts.txt') as f:
    texts_txt = f.readlines()
texts = [t.replace('\n','') for t in texts_txt]

with open('db/data2/syllabus_metadatas.json', 'rt') as f:
    metadatas = json.load(f)

ids = [str(i) for i in range(len(texts))]

embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

vectorstore = FAISS.from_texts(texts,embedding,metadatas,ids = ids)

vectorstore.save_local('db/data2/syllabus_vectorstore')
#実際、GooglecolabでGPUを用いて実行して3分かかった