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

ARGUMENTS = {
    'titre':('obl',),
    'compositeur':('obl', 'id'),
    'editeur':('fac', 'id'),
    'mouvement':('fac',),
    'tempo':('fac',),
    'ton':('fac',),
    'format':('fac','id'),
    'records':('list',),
    'instruments':('list', 'id')
}

MULTI_PARAM = ['records', 'instruments']

Counter = 0



def createElement(model):
    for k in model:
        if k in MULTI_PARAM:
            model[k] = []
            while True:
                ent = input('Ajouter un ' + str(k) + ' (Appuyez sur "Entrée" pour terminer la saisi')
                if checkFor(ent, )
                if ent == '':
                    break
                model[k].append(ent)
        
        else:
            ent = input('Entrez une valeur de ' + str(k) + ' (Appuyez sur "Entrée" pour laisser vide')
            
def checkFor(value, indict):
    if value in indict.values():
        printElement(indict[value])
        return True
    else:
        print('Impossible de reconaitre la valeur entrée : ', value)
        rechercheElement(indict, value)
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

