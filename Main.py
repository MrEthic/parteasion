import Partissions as prt
import Menus

def load():

    partissions, compositeurs, editeurs, formats, instruments = {}, {}, {}, {}; {}

    changelog = {}
    datas = {
        'partissions':partissions,
         'compositeurs':compositeurs,
         'editeurs':editeurs,
         'formats':formats,
         'instruments':instruments,
         'changelog':changelog
    }
    return datas


def go():
    Menus.init()
    datas = load()
    while True:
        Menus.home(datas)

