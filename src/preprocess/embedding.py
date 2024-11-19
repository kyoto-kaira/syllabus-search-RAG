from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import json

with open('data2/shirabasu_texts.txt') as f:
    texts_txt = f.readlines()
texts = [t.replace('\n','') for t in texts_txt]

with open('data2/shirabasu_metadatas.json', 'rt') as f:
    metadatas = json.load(f)

ids = [str(i) for i in range(len(texts))]

embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

m = []
for meta in metadatas:
    d = {}
    d['科目名'] = meta['科目名']
    d['URL'] = meta['URL']
    d['ID'] = meta['ID']
    m.append(d)

vectorstore = FAISS.from_texts(texts,embedding,m,ids = ids)

vectorstore.save_local('data2/shirabasu_vectorstore')
#実際、GooglecolabでGPUを用いて実行して3分かかった