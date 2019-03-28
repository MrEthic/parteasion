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

ARGUMENTS = ['titre', 'compositeur', 'editeur', 'mouvement', 'tempo', 'ton', 'format', 'records', 'instruments']

Counter = 0


def createPartission(rawDatas):

    datas = rawDatas.split(',')
    partission = {}

    for arg in ARGUMENTS:
        partission[arg] = datas[ARGUMENTS.index(arg)]

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

