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

def ajouter():
    print("que voulez-vous ajouter ? ","\n" , "1-partition","\n" , "2-compositceur" ,"\n" ,"3-editeur","\n" ,"4-instrument","\n" ,"5-format"))
    type=getAnswer("partition","compositeur","editeur","instrument","format")

    if type == "partition":
        partition=util.createElement(MODEL_PARTITION)
        numero="P"+ Datas.lastP
        Datas.partitions[numero]=partition
        Datas.lastP=Datas.lastP+1

    if type == "compositeur":
        compositeur=util.createElement(MODEL_COMPOSITEUR)
        numero="C"+ Datas.lastC
        Datas.compositeurs[numero]=compositeur
        Datas.lastC=Datas.lastC+1

    if type == "editeur":
        editeur=util.createElement(MODEL_EDITEUR)
        numero="E"+ Datas.lastE
        Datas.editeurs[numero]=editeur
        Datas.lastE=Datas.lastE+1

    if type == "instrument":
        instrument=util.createElement(MODEL_INSTRUMENT)
        numero="P"+ Datas.lastI
        Datas.instruments[numero]=instrument
        Datas.lastI=Datas.lastI+1

    if type == "format":
        format=util.createElement(MODEL_FORMAT)
        numero="P"+ Datas.lastF
        Datas.formats[numero]=format
        Datas.lastF=Datas.lastF+1

#"blablabla".higher ---------> BLABLABLA
#"BLABLABLA".lower - --------> blablabla



actions = {
    'ajouter':ajouter,
    'rechercher':rechercher
}