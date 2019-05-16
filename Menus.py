import Aliases as als
import Utils as util
import Datas

def init():
    rtn = ' ' + 33*'/' + '|\n' + 2* ('||' + 30*' ' + '|||\n')
    rtn += '||' + 8*' ' + '______FUZETEAM' + 8*' ' + '|||\n'
    rtn += '||' + 8*' ' + 'PARTEASION APP' + 8*' ' + '|||\n'
    rtn += 2* ('||' + 30*' ' + '|||\n') + ' ' + 33*'\\' + '|\n\n'

    print(rtn)

    Datas.load()
    home()


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

    print('Que voulez faire ? (Ajouter, Supprimer, Gerer, Sauvegarder, Quitter)')
    respond = getAnswer(['ajouter', 'supprimer', 'gerer', 'sauvegarder', 'quitter'])
    actions.get(respond)()
                
def ajouter():
    print("Que voulez-vous ajouter ? ","\n" , " - partition","\n" , " - compositeur" ,"\n" ," - editeur","\n" ," - instrument","\n")
    ent = getAnswer(["partition","compositeur","editeur","instrument","format"])
    modele = 'MODELE_' + ent.upper()
    elem = util.createElement(MODELE[modele])
    inStck = ent + 's'
    
    stck = Datas.D[inStck]

    #stck = getattr(Datas, inStck)
    lastId = stck['maxId']
    L = lastId[0]
    Id = int(lastId[1:]) + 1
    newId = ent[0].upper() + str(Id)
    stck['maxId'] = L + str(Id)
    stck[newId] = elem
    Datas.save()
    home()
    
def rechercher():
    return 0




actions = {
    'ajouter':ajouter,
    'rechercher':rechercher
}

MODELE = {
    'MODELE_PARTITION': {
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
    },
    'MODELE_COMPOSITEUR': {
        'nom':None,
        'prenom':None,
        'siecle':None
    },

    'MODELE_EDITEUR': {
        'nom':None,
        'prenom':None,
        'siecle':None
    },

    'MODELE_ENREGISTREMENT': {
        'nom':None,
        'date':None
    },

    'MODELE_INSTRUMENT': {
        'nom':None,
        'type':None
    }
}


init()

