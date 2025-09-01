__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from chromadb.utils import embedding_functions 

default_ef = embedding_functions.DefaultEmbeddingFunction()

name = "Paulo"

emb = default_ef(name)

print(emb)