from texttable import Texttable
import Datas

MULTI_PARAM = ['records', 'instruments']
KEYED_PARAM = ['compositeur', 'editeur', 'format', 'records', 'instruments']

Counter = 0



def createElement(model): #Creation d'un disctionaire par apport a un modele
    element = model.copy()
    for k in element:
        stck = ''
        if k in KEYED_PARAM: #si le parametre est sous forme de clefs
            search = (str(k) + 's') if not str(k)[-1:] == 's' else str(k)
            stck = getattr(Datas, search) #recup les donnes specifique
        if k in MULTI_PARAM: #si le prametre est liée a une liste
            element[k] = []
            while True:
                ent = input('Ajouter un ' + str(k) + ' (Appuyez sur "Entrée" pour terminer la saisi)\t')
                if ent == '':
                    break
                elif (checkFor(ent, k, stck)): #verifie que la clef existe
                    element[k].append(ent) #ajoute cette clef a la list
        else:
            ent = input('Entrez une valeur de ' + str(k) + ' (Appuyez sur "Entrée" pour laisser vide)\t')
            if ent == '':
                return
            elif checkFor(ent, k, stck):
                element[k] = ent
    return element



            


def checkFor(value, key, indict):
    if not key in KEYED_PARAM or key == '': #le parametre n'est pas sous forme de clef
        return True
    elif value in indict.values(): #Si la clef est reconu
        #printElement(indict[value]) #imprime l'element
        return True
    else: #sinon
        print('Impossible de reconaitre la valeur entrée : ', value)
        rechercheElement(indict, value) #affiche la recherche correspondante
        return False

def rechercheElement(indict, value):
    args = value.split(' ')
    for e in indict.values():
        print('r')
               
            

def edit(element, **edits): #edition d'un disctionaire existant
    
    for param, changes in edits.items():

        stck = ''
        if param in KEYED_PARAM: #si le parametre est sous forme de clefs
            search = (str(param) + 's') if not str(param)[-1:] == 's' else str(param)
            stck = getattr(Datas, search) #recup les donnes specifique

        if changes == None:
            continue

        if param in MULTI_PARAM and param in element:
            for add in changes:
                if (checkFor(add, param, stck)): #verifie que la clef existe
                    element[param].append(add) #ajoute cette clef a la list
        elif param in element:
            if checkFor(add, param, stck):
                element[param] = add



t=Texttable()
MODELE_PARTITION = {
    'titre':'Clair de Lune',
    'tempo':'Andante',
    'identifiant':'P1',
    'ton':'majeur',
    'compositeur':'Debussy',
    'instruments':'piano'
}

length=len(MODELE_PARTITION)
keys=list(MODELE_PARTITION.keys())
values=list(MODELE_PARTITION.values())

t.add_rows([keys, values])
print(t.draw())


