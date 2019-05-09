import Aliases as als
import Utils as util
import Datas

def init():
    rtn = ' ' + 33*'/' + '|\n' + 2* ('||' + 30*' ' + '|||\n')
    rtn += '||' + 8*' ' + '______FUZETEAM' + 8*' ' + '|||\n'
    rtn += '||' + 8*' ' + 'PARTEASION APP' + 8*' ' + '|||\n'
    rtn += 2* ('||' + 30*' ' + '|||\n') + ' ' + 33*'\\' + '|\n\n'

    print(rtn)


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


def home():

    print('Que voulez faire ? (Ajouter, Supprimer, Gere, Sauvegarder, Quitter)')
    respond = getAnswer(['ajouter', 'supprimer', 'gere', 'sauvegarder', 'quitter'])
    actions.get(respond)()
                
def ajouter():
    print("Que voulez-vous ajouter ? ","\n" , " - partition","\n" , " - compositceur" ,"\n" ," - editeur","\n" ," - instrument","\n")
    ent = getAnswer(["partition","compositeur","editeur","instrument","format"])
    modele = 'MODELE_' + ent.upper()
    elem = util.createElement(modele)
    inStck = ent + 's'
    stck = getattr(Datas, inStck)
    lastId = stck[maxId]
    Id = int(lastId[1:]) + 1
    newId = ent[0].upper() + str(Id)
    stck[newId] = elem
    


def rechercher():
    print("que voulez-vous rechercher ? ", "\n", "1-partition", "\n", "2-compositceur", "\n")
    type = getAnswer(["partition", "compositeur"])

    if type == "partition":
        information = input("Donnez une information sur la partition")
        info = information.split(" ")
        solution = []
        score =[]
        for k,v in partitions.items():
            for param in v.values() :
                for c in range (0,len(info)):
                    if info[c] == v.values[param]:
                        for d in range (0,len(solution)):
                            if partitions.items[k] == solution[d]:
                                score[d]= score [d] +1
                            else:
                                solution.append = partitions.items[k]
                                score.append=1


actions = {
    'ajouter':ajouter,
    'rechercher':rechercher
}


MODELE_PARTITION = {
    'titre':None,
    'mouvement': None,
    'tempo':None,
    'identifiant':None,
    'ton':None,
    'compositeur':None,
    'editeur':None,
    'format':None,
    'enregistrement':None,
    'instruments':None
}

MODELE_COMPOSITEUR = {
    'nom':None,
    'prenom':None,
    'siecle':None
}

MODELE_EDITEUR = {
    'nom':None,
    'prenom':None,
    'siecle':None
}

MODELE_ENREGISTREMENT = {
    'nom':None,
    'date':None
}

MODELE_INSTRUMENT = {
    'nom':None,
    'type':None
}

