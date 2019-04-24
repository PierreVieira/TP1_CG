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

def check2(pts):
    if pts == '0':
        texturas.init_tex(globais.imgload[53], globais.img[53])
    elif pts == '1':
        texturas.init_tex(globais.imgload[54], globais.img[54])
    elif pts == '2':
        texturas.init_tex(globais.imgload[55], globais.img[55])
    elif pts == '3':
        texturas.init_tex(globais.imgload[56], globais.img[56])
    elif pts == '4':
        texturas.init_tex(globais.imgload[57], globais.img[57])
    elif pts == '5':
        texturas.init_tex(globais.imgload[58], globais.img[58])
    elif pts == '6':
        texturas.init_tex(globais.imgload[59], globais.img[59])
    elif pts == '7':
        texturas.init_tex(globais.imgload[60], globais.img[60])
    elif pts == '8':
        texturas.init_tex(globais.imgload[61], globais.img[61])
    elif pts == '9':
        texturas.init_tex(globais.imgload[62], globais.img[62])

def Pts(id):
    if globais.pts < 1000:
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
    else:
        globais.pts = str(int(globais.pts))
        if id == 13 and len(globais.pts) >= 1:
            check2(globais.pts[-1])
        elif id == 12 and len(globais.pts) >= 2:
            check2(globais.pts[-2])
        elif id == 11 and len(globais.pts) >= 3:
            check2(globais.pts[-3])
        elif id == 10 and len(globais.pts) >= 4:
            check2(globais.pts[-4])
        globais.pts = int(globais.pts)
