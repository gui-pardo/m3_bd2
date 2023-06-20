from pymongo import MongoClient
client = MongoClient('localhost', 27017)
dataBase = client['Veiculo']

collections = dataBase['Veiculo']
db = client.Veiculo

db.Modelo.insert_many(
    [
        {'id': 1,
     'id_marca': 1,
     'nome': '911'
     }
     ]
)

modelo ={
    'id':2,
    'id_marca': 2,
    'nome': 'spyder'

    }

db.Modelo.insert_one(modelo)

modelos = db.Modelo.find()

modelo = db.Modelo.find_one({'id':2})
print(modelo)

update_dados = {'$set':{'nome': 'Ferrari Urus'}}

atualizaDoc = db.Modelo.update_one({'id': 2}, update_dados )
print(f"atualizado com sucesso: {atualizaDoc.modified_count}")

db.Carro.delete_one({'id':2})
#percorrendo na tabela de carros
for modelo in modelos:
    print(modelo)
