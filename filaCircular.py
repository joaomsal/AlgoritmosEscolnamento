import time
import fila as FL
from multiprocessing import Process

tt = 0

def inicializaPaginas(paginas):
    pages = []
    for p in paginas:
        aux = []
        aux.append(p)
        aux.append(False)
        pages.append(aux)

    return pages

def getTempo(tp):
	if tp !=[]:
		aux = tp.split(":")
		t = aux.pop(0)

		if t != ' ':
			return int(t)
		else:
			return 0

def getPage(tp):
	if len(tp) > 0:
		aux = tp.split(":")
		aux.pop(0)
		p = aux.pop(0)

	if p != ' ':
		return int(p)
	else:
		return 0

def alcoc(p, pages):
    for i in pages:
        if i[0] == p[0]:
            return True

    return False

#True = 1 e False = 0
def filaCircular(paginas, processo):
    pages = inicializaPaginas(paginas)
    pg = processo.getPages()
    i = 0
    while pg !=[]:
        pg0 = pg.pop(0)
        for p in pages:
            #if alcoc(p, pages)
            if not p[1] and alcoc((getPage(pg0), False), pages):
                if pg0 != ' ':
                    p[1] = True
                    p[0] = getPage(pg0)
                    time.sleep(getTempo(pg0)/1000000)
                    print("Executando o processo (", processo.getId(), ") \n")
            else: 
                p[1] = False 
                i+=1
                pages = inicializaPaginas(paginas)
                print("Processo ",processo.getId(),"| Page Faults = ", i)
                break
    return i
            
                


def inicia(processos, paginas):
    print(len(processos))
    for p in processos:
        print(len(p.getPages()))
		#Process(target= , args=(paginas, p)).start()
        #print("T = ", tt)
        x = Process(target=filaCircular, args=(paginas, p)).start()
                                   
