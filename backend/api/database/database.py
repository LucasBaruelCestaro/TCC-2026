import pymongo
cliente = pymongo.MongoClient("mongodb+srv://root:123@cluster0.nqep0zl.mongodb.net/?appName=Cluster0")
banco_de_dados = cliente["tcc2026"]
questao = banco_de_dados['questao']
