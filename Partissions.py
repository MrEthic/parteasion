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

Counter = 0


def loadPartission(rawDatas):

    datas = rawDatas.split(',')
    partission = {}
    i = 0
    for arg in ARGUMENTS:
        partission[arg] = datas[i]
        i += 1

    return partission



def editPartission(part, **edits):
    
    for param, changes in edits.items():
        
        if changes == None:
            continue

        if param in ['records', 'instruments']:
            for add in changes:
                part[param].append(add)
        elif param in part:
            part[param] = changes

