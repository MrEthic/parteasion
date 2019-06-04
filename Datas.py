import json
import os

partitions, compositeurs, editeurs, records, instruments = 2, None, None, None, None

D = {}

def load():
    with open('datas.json', encoding='utf8') as dataFile:
        datas = json.load(dataFile)

    D['partitions'] = datas['partitions']
    D['compositeurs'] = datas['compositeurs']
    #editeurs = datas['editeurs']
    #records = datas['records']
    #instruments = datas['instruments']

def save():
    datas = {
        'partitions':D['partitions'],
        'compositeurs':D['compositeurs'],
        'editeurs':0,
        'records':0,
        'instruments':0
    }
    os.remove('old.json')
    os.rename('datas.json', 'old.json')
    with open('datas.json', 'w', encoding='utf8') as dataFile:
        json.dump(datas, dataFile, indent=4)

def reloadBackup():
    os.rename('datas.json', 'bk.json')
    os.rename('old.json', 'datas.json')
    os.rename('bk.json', 'old.json')
    load()