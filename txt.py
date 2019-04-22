import texturas
import globais

def check(pts):
    if pts == '0':
        texturas.init_tex(globais.imgload[18], globais.img[18])
    elif pts == '1':
        texturas.init_tex(globais.imgload[19], globais.img[19])
    elif pts == '2':
        texturas.init_tex(globais.imgload[20], globais.img[20])
    elif pts == '3':
        texturas.init_tex(globais.imgload[21], globais.img[21])
    elif pts == '4':
        texturas.init_tex(globais.imgload[22], globais.img[22])
    elif pts == '5':
        texturas.init_tex(globais.imgload[23], globais.img[23])
    elif pts == '6':
        texturas.init_tex(globais.imgload[24], globais.img[24])
    elif pts == '7':
        texturas.init_tex(globais.imgload[25], globais.img[25])
    elif pts == '8':
        texturas.init_tex(globais.imgload[26], globais.img[26])
    elif pts == '9':
        texturas.init_tex(globais.imgload[27], globais.img[27])

def Pts(id):
    globais.pts = str(int(globais.pts))
    if id == 13 and len(globais.pts) >= 1:
        check(globais.pts[-1])
    elif id == 12 and len(globais.pts) >= 2:
        check(globais.pts[-2])
    elif id == 11 and len(globais.pts) >= 3:
        check(globais.pts[-3])
    elif id == 10 and len(globais.pts) >= 4:
        check(globais.pts[-4])
    globais.pts = int(globais.pts)