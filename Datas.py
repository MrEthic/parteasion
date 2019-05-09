import json

partissions, compositeurs, editeurs, records, instruments = None, None, None, None, None

def load():
    with open('datas.json') as dataFile:
        datas = json.loads(dataFile)
    partissions = datas['partissions']
    compositeurs = datas['compositeurs']
    editeurs = datas['editeurs']
    records = datas['records']
    instruments = datas['instruments']