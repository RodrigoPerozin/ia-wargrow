from classes.Predicao import *
from classes.Cores import *
from classes.Paises import *
from classes.Exercitos import *
from classes.Continentes import *
from classes.Fronteiras import *
from classes.Tarefas import *
from classes.Utils import *

info = Utils.loadInfo()

#info structure contains:
#-List with 5 info items such as:
#--fronteiras
#--exercitos
#--continentes
#--paises
#--objetivos

print(f'País info: {info[0][0].pais}\nFronteira info:{info[0][0].fronteiras}')