import Partissions as prt
import Menus

def load():

    partissions, compositeurs, editeurs, formats, instruments = {}, {}, {}, {}; {}

    datas = {
         'partissions':partissions,
         'compositeurs':compositeurs,
         'editeurs':editeurs,
         'formats':formats,
         'instruments':instruments
    }
    return datas


def go():
    Menus.init()
    datas = load()
    while True:
        Menus.home(datas)

