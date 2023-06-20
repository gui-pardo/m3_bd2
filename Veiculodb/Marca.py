from pymongo import MongoClient
client = MongoClient('localhost', 27017)
dataBase = client['Veiculo']

collections = dataBase['Veiculo']
db = client.Veiculo

db.Marca.insert_many(
    [
        {'id': 1,

     'nome': 'Porshe'}
     ]
)

marca = {
    'id':2,
    'nome':'Lamborghini'
}

db.Marca.insert_one(marca)

marcas = db.Marca.find()

marca = db.Marca.find_one({'id':2})

print(marca)
update_dados = {'$set':{'nome': 'Lamborghini Aventador'}}

atualizaDoc = db.Marca.update_one({'id': 2}, update_dados)
print(f"atualizado com sucesso: {atualizaDoc.modified_count}")

#db.Carro.delete_one({'id':2})
#percorrendo na tabela de carros
for marca in marcas:
    print(marca)
