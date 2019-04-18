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

def ajouter(datas):
    

def ajouterPartition(datas):
    args = prt.ARGUMENTS.copy()
    print('Remplissez les champs suivants : (les champs * sont obligatoire, laissez vide pour ne pas rensseigner)')
    for arg, param in args:
        print('Entrez un ' + arg)
        while True:
            ent = input('   --> ')
            if 'fac' in param and ent == '':
                args[arg] = None
                break
            if 'id' in param and arg in datas:
                for key, value in datas[args].items():
                    if ent == key or ent in value.values():
                        ent = key
                        break
                ent = None
                if 'obl' in param:
                    print('Ce paramètre est obligatoire, votre entré est non valide, recommencer')
                    continue

            if not 'list' in param:
                args[arg] = ent
                break
            
            if ent == None:
                continue
            
            if not isinstance(args[arg], list):
                args[arg] = [ent]

            args[arg].append(ent)

            

                
            




def rechercher():
    print('')


actions = {
    'ajouter':ajouter,
    'rechercher':rechercher
}
