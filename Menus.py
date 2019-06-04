import Aliases as als
import Utils as util
import Datas
import sys

def init():
    rtn = '\t\t\t' + ' ' + 33*'/' + '|\n' + 2* ('\t\t\t' + '||' + 30*' ' + '|||\n')
    rtn += '\t\t\t' + '||' + 8*' ' + '______FUZETEAM' + 8*' ' + '|||\n'
    rtn += '\t\t\t' + '||' + 8*' ' + 'PARTEASION APP' + 8*' ' + '|||\n'
    rtn += 2* ('\t\t\t' + '||' + 30*' ' + '|||\n') + '\t\t\t' + ' ' + 33*'\\' + '|\n'

    print(rtn)

    Datas.load()
    while True:
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

    print('\nQue voulez faire ? (Ajouter, Rechercher, Supprimer, Modifier, Sauvegarder, Quitter ou recharger un backup)')
    respond = getAnswer(['ajouter', 'rechercher', 'supprimer','modifier', 'sauvegarder', 'quitter', 'backup'])
    if not respond == None:
        actions.get(respond)()

                
def ajouter():
    print("\nQue voulez-vous ajouter ? ","\n" , " - partition","\n" , " - compositeur" ,"\n" ," - editeur","\n" ," - instrument","\n")
    ent = getAnswer(["partition","compositeur","editeur","instrument"])
    modele = 'MODELE_' + ent.upper()
    elem = util.createElement(MODELE[modele])
    inStck = ent + 's'
    
    stck = Datas.D[inStck]

    lastId = stck['maxId']
    L = lastId[0]
    Id = int(lastId[1:]) + 1
    newId = ent[0].upper() + str(Id)
    stck['maxId'] = L + str(Id)
    stck[newId] = elem

def getId(dico):
    while True:
        val = input('\nEntrez un Id ou une recherche :\t')
        if val == '':
            print("Anulation -- retour menu principale")
            return None
        if not val in dico.keys():
            result = util.rechercheElement(dico, val)
            elements = [(x, dico[x]) for x in result]
            util.printElements(elements)
            print('Id invalide')
            continue
        break
    return val

def modifier():
    print('\nQuel element voulez-vous modifier ?',"\n" , " - partition","\n" , " - compositeur" ,"\n" ," - editeur","\n" ," - instrument","\n")
    ent = getAnswer(["partition","compositeur","editeur","instrument"])
    modele = 'MODELE_' + ent.upper()
    inStck = ent + 's'
    stck = Datas.D[inStck]
    val = getId(stck)
    if val == None:
        return
    util.printElements([(val, stck[val])])
    elem = util.createElement(MODELE[modele])
    util.edit(stck[val], **elem)
    


    
def rechercher():
    print("\nQuelle élément voulez vous rechercher ?""\n" , " - partition","\n" , " - compositeur" ,"\n" ," - editeur","\n" ," - instrument")
    ent = getAnswer(["partition","compositeur","editeur","instrument"])
    value = input('\nSaisie de recherche :\t')
    inStck = ent + 's'
    stck = Datas.D[inStck]
    result = util.rechercheElement(stck, value)
    elements = [(x, stck[x]) for x in result]
    util.printElements(elements)

def supprimer():
    print('\nQuel element voulez-vous supprimer ?',"\n" , " - partition","\n" , " - compositeur" ,"\n" ," - editeur","\n" ," - instrument","\n")
    ent = getAnswer(["partition","compositeur","editeur","instrument"])
    inStck = ent + 's'
    stck = Datas.D[inStck]
    val = getId(stck)
    if val == None:
        return
    del(stck[val])


def save():
    try:
        Datas.save()
    except:
        print('\n[WARNING] Erreur pendant la sauvegarde')
    else:
        print('\nDonnées sauvegardé sur disque dans "datas.json", backup effectué dans "old.json"\nUtilisez "load backup (lb)" pour recharger le backup')
    

def backup():
    print('\nVoulez vous vraiment recherger la dernière backup ?')
    ent = getAnswer(['oui', 'non'])
    if ent == 'non':
        print('Anulation')
    elif ent == 'oui':
        try:
            Datas.reloadBackup()
        except:
            print('\n[WARNING] Erreur pendant le rechergement du backup')
        else:
            print('\nRechargement du backup terminé')
    

def quitter():
    print('\nVous etes sur le point de quitter, souhaitez vous sauvegarder les modification ? (oui, non ou annuler)')
    ent = getAnswer(['oui', 'non', 'annuler'])
    if ent == 'oui':
        save()
        sys.exit()
    elif ent == 'annuler':
        print('\nRetour au menu :')
    elif ent == 'non':
        sys.exit()
    
    



actions = {
    'ajouter':ajouter,
    'rechercher':rechercher,
    'supprimer': supprimer,
    'modifier': modifier,
    'sauvegarder':save,
    'backup': backup,
    'quitter': quitter
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

