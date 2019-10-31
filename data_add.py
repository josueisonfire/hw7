from elasticsearch import Elasticsearch
import elasticsearch
import json

es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])


with open('data.json', 'r') as f:
    data_dict = json.load(f)

i = 1

for datum in data_dict:
    print('Printing input data: %s \n' %datum)
    es.index(index='test', doc_type='movie data', id=i, body=datum)
    i = i + 1