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

def getAnswer(answers):
    ent = input('   --> ').lower()
    while True:
        if ent == '':
            return None
        for word, al in als.aliases.items():
            if not word in answers:
                continue
            if ent in al:
                return word
        ent = input('Requette non valide, recomencer\n   --> ')

def createElement(model):
    for k in model:
        if k in MULTI_PARAM:
            model[k] = []
            while True:
                ent = input('Ajouter un ' + str(k) + ' (Appuyez sur "Entrée" pour terminer la saisi')
                if ent == '':
                    break
                model[k].append(ent)
        
        else:
            ent = input('Entrez une valeur de ' + str(k) + ' (Appuyez sur "Entrée" pour laisser vide')
            

            
            

def edit(element, **edits):
    
    for param, changes in edits.items():
        
        if changes == None:
            continue

        if param in MULTI_PARAM:
            for add in changes:
                element[param].append(add)
        elif param in element:
            element[param] = changes

