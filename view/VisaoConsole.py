from classes.Objetivos import *

class VisaoConsole:
    def coletarObjetivo():
        objetivoIndex = int(input("\n\nLista de objetivos:\n"
            +"\n0 - "+Objetivos.objetivos[0]
            +"\n1 - "+Objetivos.objetivos[1]
            +"\n2 - "+Objetivos.objetivos[2]
            +"\n3 - "+Objetivos.objetivos[3]
            +"\n4 - "+Objetivos.objetivos[4]
            +"\n5 - "+Objetivos.objetivos[5]
            +"\n6 - "+Objetivos.objetivos[6]
            +"\n7 - "+Objetivos.objetivos[7]
            +"\n8 - "+Objetivos.objetivos[8]
            +"\n9 - "+Objetivos.objetivos[9]
            +"\n10 - "+Objetivos.objetivos[10]
            +"\n11 - "+Objetivos.objetivos[11]
            +"\n12 - "+Objetivos.objetivos[12]
            +"\n13 - "+Objetivos.objetivos[13]
            +"\n\nInforme o item que corresponde ao objetivo do jogo: "))
        return objetivoIndex