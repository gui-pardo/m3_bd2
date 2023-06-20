from typing import List, Dict

from pymongo import MongoClient
from sqlalchemy.orm.collections import collection
from sqlalchemy.testing import db

client = MongoClient('localhost', 27017)
dataBase = client['Veiculo']

collections = dataBase['Veiculo']
db = client.Veiculo

# print(client.list_databases())

db.Carro.insert_many(
    [
        {'id': 1,
     'id_modelo': 2,
     'nome': 'Jaguar',
     'renavam': 123456789,
     'placa': 'ABC1234',
     'valor': 10000.0,
     'ano': 2022}
     ]
)


carro = {

    'id': 2,
    'id_modelo': 3,
    'nome': 'Ferrari',
    'renavam': 987654321,
    'placa': 'XYZ5678',
    'valor': 150000.0,
    'ano': 2023


}
db.Carro.insert_one(carro)


carros = db.Carro.find()




carro = db.Carro.find_one({'placa': 'ABC1234'})


db.Carro.update_one({'placa': 'ABC1234'}, {'$set': {'valor': 12000.0}})

db.Carro.delete_one({'id':2})
#percorrendo na tabela de carros
for carro in carros:
    print(carro)


