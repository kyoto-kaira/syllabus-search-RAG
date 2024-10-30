from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import pickle

path1 = 'data2\shirabasu_texts.pkl'
with open(path1, 'rb') as f:
    texts = pickle.load(f)
path2 = 'data2/shirabasu_metadatas.pkl'
with open(path2, mode='rb') as f:
    metadatas = pickle.load(f)
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