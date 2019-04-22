import texturas
import globais

def check(pts):
    if pts == '0':
        texturas.init_tex(globais.imgload[16], globais.img[16])
    elif pts == '1':
        texturas.init_tex(globais.imgload[0], globais.img[0])
    elif pts == '2':
        texturas.init_tex(globais.imgload[1], globais.img[1])
    elif pts == '3':
        texturas.init_tex(globais.imgload[2], globais.img[2])
    elif pts == '4':
        texturas.init_tex(globais.imgload[3], globais.img[3])
    elif pts == '5':
        texturas.init_tex(globais.imgload[4], globais.img[4])
    elif pts == '6':
        texturas.init_tex(globais.imgload[5], globais.img[5])
    elif pts == '7':
        texturas.init_tex(globais.imgload[16], globais.img[16])
    elif pts == '8':
        texturas.init_tex(globais.imgload[16], globais.img[16])
    elif pts == '9':
        texturas.init_tex(globais.imgload[16], globais.img[16])

def Pts(id):
    globais.pts = str(int(globais.pts))
    if id == 10 and len(globais.pts) == 1:
        check(globais.pts[0])
    elif id == 11 and len(globais.pts) == 2:
        check(globais.pts[1])
    elif id == 12 and len(globais.pts) == 3:
        check(globais.pts[2])
    elif id == 13 and len(globais.pts) == 4:
        check(globais.pts[3])
    globais.pts = int(globais.pts)