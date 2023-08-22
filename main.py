from classes.Jogo import *
from classes.Predicao import *
from classes.Cores import *
from classes.Paises import *
from classes.Exercitos import *
from classes.Continentes import *
from classes.Fronteiras import *
from classes.Tarefas import *
from classes.Utilidades import *
from view.VisaoConsole import *

info = Utilidades.carregarInformacoes()

#info structure contains:
#-List with 5 info items such as:
#--fronteiras(list)
#--exercitos(list)
#--continentes(list)
#--paises(list)
#--objetivos(list)

jogo = Jogo()

#Jogo structure contains:
#-Constants with game settings such as:
#--objetivo(list)

#Receber o objetivo

objetivoIndex = VisaoConsole.coletarObjetivo()

Utilidades.atualizaObjetivo(objetivoIndex, jogo)

