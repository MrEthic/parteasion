import Aliases as als
import Utils as util

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


def home(datas):

    print('Que voulez faire ? (Ajouter, Supprimer, Gere, Sauvegarder, Quitter)')
    respond = getAnswer(['ajouter', 'supprimer', 'gere', 'sauvegarder', 'quitter'])
    actions.get(respond)(datas)
                
def ajouter():
    print('ajouter')

def rechercher():
    print('rechercher')


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

