from texttable import Texttable
import Datas

MULTI_PARAM = ['records', 'instruments']
KEYED_PARAM = ['compositeur', 'editeur', 'records', 'instruments']

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
                continue
            elif checkFor(ent, k, stck):
                element[k] = ent
    return element



            


def checkFor(value, key, indict):
    if not key in KEYED_PARAM or key == '': #le parametre n'est pas sous forme de clef
        return True
    elif value in indict.values(): #Si la clef est reconu
        printElements([indict[value]]) #imprime l'element
        return True
    else: #sinon
        print('Impossible de reconaitre la valeur entrée : ', value)
        search = rechercheElement(indict, value) #affiche la recherche correspondante
        prt = [(x, indict[x]) for x in search]
        printElements(prt)
        return False

def rechercheElement(indict, value):
    temp = [] #list des resultat valide en vrac
    value = value.lower()
    args = value.split(' ') #list des arguments de la recherche
    for n, e in indict.items():
        if n == 'maxId':
            continue
        rslt = []  #tableau des correspondance
        for v in e.values():
            test = v if isinstance(v, list) else v.split(' ') if isinstance(v, str) else None #transforme les valeurs en list
            if test == None:
                continue
            test = [x.lower() for x in test]
            rslt = rslt + [x for x in test if x in args] #ajoute les nouvelles correspondances
        score = len(rslt) #calcule du score
        if n in args:
            score += 100 #++ le score si la clef fait partie des args
        if score > 0:
            t = (score, n)
            temp.append(t) #ajout de cette list aux resultats
    sortedTemp = sorted(temp, reverse=True, key=lambda item:item[0]) #trie des listes
    results = [x[1] for x in sortedTemp] #garde que les element (sans le score)
    return results



               
            

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

def printElements(elements):
    prt = Texttable()
    prt.set_max_width(0)
    temp = []
    if isinstance(elements[0], tuple):
        keys = ['ID'] + list(elements[0][1].keys())
        param = [x[1] for x in elements]
    else:
        keys = ['ID'] + elements[0].keys()
        param = elements

    temp.append(keys)
    for e in elements:
        if isinstance(e, tuple):
            val = [e[0]] + list(e[1].values())
        else:
            val = e.values()
        temp.append(val)
    prt.add_rows(temp, header=True)
    print(prt.draw())



