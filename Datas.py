import json
import os

partissions, compositeurs, editeurs, records, instruments = None, None, None, None, None

def load():
    with open('datas.json') as dataFile:
        datas = json.loads(dataFile)

    partissions = datas['partissions']
    compositeurs = datas['compositeurs']
    editeurs = datas['editeurs']
    records = datas['records']
    instruments = datas['instruments']

def save():
    datas = {
        'partissions':partissions,
        'compositeurs':compositeurs,
        'editeurs':editeurs,
        'records':records,
        'instruments':instruments
    }
    os.remove('old.json')
    os.rename('datas.json', 'old.json')
    with open('datas.json', 'w') as dataFile:
        json.dump(datas, dataFile)