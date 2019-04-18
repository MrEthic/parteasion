# Partission format :
#
# {
#   titre:String
#   compositeur:String (id)
#   editeur:String (id)
#   mouvement:String
#   tempo:String
#   ton:String
#   format:String (id)
#   enregistrements:[date,]
#   instruemnts:[id,]
# }

MODEL_PARTISSIONT = {
    'titre':None,
    'compositeur':None,
    'editeur':None,
    'mouvement':None,
    'tempo':None,
    'ton':None,
    'format':None,
    'records':None,
    'instruments':None
}

MULTI_PARAM = ['records', 'instruments']
KEYED_PARAM = ['compositeur', 'editeur', 'format', 'records', 'instruments']

Counter = 0



def createElement(model):
    element = model.copy()
    for k in element:
        stck = ''
        if k in KEYED_PARAM: #si le parametre est sous forme de clefs
            stck = getattr(Datas, str(k)) #recup les donnes specifique
        if k in MULTI_PARAM: #si le prametre est liée a une liste
            element[k] = []
            while True:
                ent = input('Ajouter un ' + str(k) + ' (Appuyez sur "Entrée" pour terminer la saisi')
                if ent == '':
                    break
                elif (checkFor(ent, k, stck)): #verifie que la clef existe
                    element[k].append(ent) #ajoute cette clef a la list
        else:
            ent = input('Entrez une valeur de ' + str(k) + ' (Appuyez sur "Entrée" pour laisser vide')
            if ent == '':
                return
            elif checkFor(ent, k, stck):
                element[k] = ent



            


def checkFor(value, key, indict):
    if not key in KEYED_PARAM: #le parametre n'est pas sous forme de clef
        return True
    elif value in indict.values(): #Si la clef est reconu
        printElement(indict[value]) #imprime l'element
        return True
    else: #sinon
        print('Impossible de reconaitre la valeur entrée : ', value)
        rechercheElement(indict, value) #affiche la recherche correspondante
        return False

            
            

def edit(element, **edits):
    
    for param, changes in edits.items():
        
        if changes == None:
            continue

        if param in MULTI_PARAM:
            for add in changes:
                element[param].append(add)
        elif param in element:
            element[param] = changes

