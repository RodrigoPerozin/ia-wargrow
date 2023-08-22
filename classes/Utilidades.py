from classes.Paises import *
from classes.Exercitos import *
from classes.Continentes import *
from classes.Fronteiras import *
from classes.Objetivos import *
from classes.Cor import *
import requests

class Utilidades:
    
    def carregarInformacoes():
        
        fronteirasBrasil = Fronteiras("brasil", ["argentina", "peru", "venezuela", "argelia"])
        fronteirasArgentina = Fronteiras("argentina", ["peru", "brasil"])
        fronteirasPeru = Fronteiras("peru", ["brasil", "argentina", "venezuela"])
        fronteirasVenezuela = Fronteiras("venezuela", ["brasil", "peru", "mexico"])
        fronteirasMexico = Fronteiras("mexico", ["venezuela", "nova_york", "california"])
        fronteirasNovaYork = Fronteiras("nova_york", ["mexico", "california", "ottawa", "labrador"])
        fronteirasCalifornia = Fronteiras("california", ["nova_york", "ottawa", "vancouver", "mexico"])
        fronteirasOttawa = Fronteiras("ottawa", ["labrador", "nova_york", "california", "vancouver", "mackenzie"])
        fronteirasVancouver = Fronteiras("vancouver", ["mackenzie", "alaska", "ottawa", "california"])
        fronteirasLabrador = Fronteiras("labrador", ["ottawa", "nova_york", "groenlandia"])
        fronteirasMackenzie = Fronteiras("mackenzie", ["alaska", "vancouver", "ottawa", "groenlandia"])
        fronteirasGroenlandia = Fronteiras("groenlandia", ["mackenzie", "islandia"])
        fronteirasAlaska = Fronteiras("alaska", ["mackenzie", "vancouver", "vladvostok"])
        fronteirasIslandia = Fronteiras("islandia", ["groenlandia", "inglaterra"])
        fronteirasInglaterra = Fronteiras("inglaterra", ["islandia", "suecia", "alemanha", "franca"])
        fronteirasFranca = Fronteiras("franca", ["polonia", "alemanha", "inglaterra", "argelia"])
        fronteirasPolonia = Fronteiras("polonia", ["alemanha", "moscou", "franca", "oriente_medio", "egito"])
        fronteirasAlemanha = Fronteiras("alemanha", ["inglaterra", "polonia", "franca"])
        fronteirasSuecia = Fronteiras("suecia", ["moscou", "inglaterra"])
        fronteirasMoscou = Fronteiras("moscou", ["suecia", "omsk", "oriente_medio", "polonia", "aral"])
        fronteirasEgito = Fronteiras("egito", ["argelia", "sudao", "oriente_medio", "polonia", "franca"])
        fronteirasArgelia = Fronteiras("argelia", ["congo", "sudao", "egito", "franca", "brasil"])
        fronteirasSudao = Fronteiras("sudao", ["egito", "argelia", "congo", "madagascar"])
        fronteirasCongo = Fronteiras("congo", ["sudao", "africa_do_sul", "argelia"])
        fronteirasAfricaDoSul= Fronteiras("africa_do_sul", ["madagascar", "congo", "sudao"])
        fronteirasMadagascar = Fronteiras("madagascar", ["africa_do_sul", "sudao"])
        fronteirasVladvostok = Fronteiras("vladvostok", ["siberia", "tchita", "china", "japao", "alaska"])
        fronteirasSiberia = Fronteiras("siberia", ["vladvostok", "tchita", "dudinka"])
        fronteirasTchita = Fronteiras("tchita", ["mongolia", "dudinka", "siberia", "vladvostok", "china"])
        fronteirasDudinka = Fronteiras("dudinka", ["siberia", "tchita", "omsk", "mongolia"])
        fronteirasOmsk = Fronteiras("omsk", ["mongolia", "dudinka", "moscou", "aral", "china"])
        fronteirasAral = Fronteiras("aral", ["omsk", "china", "moscou", "oriente_medio", "india"])
        fronteirasOrienteMedio = Fronteiras("oriente_medio", ["aral", "india", "egito", "polonia", "moscou"])
        fronteirasMongolia = Fronteiras("mongolia", ["china", "tchita", "omsk", "dudinka"])
        fronteirasVietna = Fronteiras("vietna", ["india", "china", "borneo"])
        fronteirasJapao = Fronteiras("japao", ["china", "vladvostok"])
        fronteirasChina = Fronteiras("china", ["vladvostok", "tchita", "mongolia", "aral", "india", "vietna", "japao", "omsk"])
        fronteirasIndia = Fronteiras("india", ["oriente_medio", "china", "aral", "vietna", "sumatra"])
        fronteirasSumatra = Fronteiras("sumatra", ["australia", "india"])
        fronteirasBorneo = Fronteiras("borneo", ["australia", "nova_guine", "vietna"])
        fronteirasNovaGuine = Fronteiras("nova_guine", ["australia", "borneo"])
        fronteirasAustralia = Fronteiras("australia", ["sumatra", "borneo", "nova_guine"])

        fronteiras = [fronteirasBrasil, fronteirasArgentina, fronteirasPeru, fronteirasVenezuela,
                    fronteirasMexico, fronteirasNovaYork, fronteirasCalifornia, fronteirasOttawa,
                    fronteirasVancouver, fronteirasLabrador, fronteirasMackenzie, fronteirasGroenlandia,
                    fronteirasAlaska, fronteirasIslandia, fronteirasInglaterra, fronteirasFranca,
                    fronteirasPolonia, fronteirasAlemanha, fronteirasSuecia, fronteirasMoscou, fronteirasEgito,
                    fronteirasArgelia, fronteirasSudao, fronteirasCongo, fronteirasAfricaDoSul, fronteirasMadagascar,
                    fronteirasVladvostok, fronteirasSiberia, fronteirasTchita, fronteirasDudinka, fronteirasOmsk,
                    fronteirasAral, fronteirasOrienteMedio, fronteirasMongolia, fronteirasVietna, fronteirasJapao,
                    fronteirasChina, fronteirasIndia, fronteirasSumatra, fronteirasBorneo, fronteirasNovaGuine,
                    fronteirasAustralia]

        exercitosAzul = Exercitos("azul", 0)
        exercitosVermelho = Exercitos("vermelho", 0)
        exercitosVerde = Exercitos("verde", 0)
        exercitosRoxo = Exercitos("roxo", 0)
        exercitosAmarelo = Exercitos("amarelo", 0)
        exercitosCinza = Exercitos("cinza", 0)
        
        exercitos = [exercitosAzul, exercitosVermelho, exercitosVerde, exercitosRoxo, exercitosAmarelo, exercitosCinza]

        continenteAmericaDoSul = Continentes("america_do_sul", ["brasil", "argentina", "peru", "venezuela"])
        continenteAmericaDoNorte = Continentes("america_do_norte", ["mexico", "california", "nova_york", "ottawa", "vancouver", "labrador", "mackenzie", "alaska", "groenlandia"])
        continenteAsia = Continentes("asia", ["mexico", "california", "nova_york", "ottawa", "vancouver", "labrador", "mackenzie", "alaska", "groenlandia"])
        continenteEuropa = Continentes("europa", ["moscou", "suecia", "polonia", "alemanha", "inglaterra", "islandia", "franca"])
        continenteAfrica = Continentes("africa", ["africa_do_sul", "madagascar", "congo", "sudao", "egito", "argelia"])
        continenteOceania = Continentes("oceania", ["australia", "sumatra", "borneo", "nova_guine"])

        continentes = [continenteAmericaDoSul, continenteAmericaDoNorte, continenteAsia,
                       continenteEuropa, continenteAfrica, continenteOceania]

        paisBrasil = Paises("brasil", None, 0)
        paisPeru = Paises("peru", None, 0)
        paisVenezuela = Paises("venezuela", None, 0)
        paisMexico = Paises("mexico", None, 0)
        paisNovaYork = Paises("nova_york", None, 0)
        paisCalifornia = Paises("california", None, 0)
        paisOttawa = Paises("ottawa", None, 0)
        paisVancouver = Paises("vancouver", None, 0)
        paisLabrador = Paises("labrador", None, 0)
        paisMackenzie = Paises("mackenzie", None, 0)
        paisGroenlandia = Paises("groenlandia", None, 0)
        paisAlaska = Paises("alaska", None, 0)
        paisIslandia = Paises("islandia", None, 0)
        paisInglaterra = Paises("inglaterra", None, 0)
        paisFranca = Paises("franca", None, 0)
        paisPolonia = Paises("polonia", None, 0)
        paisAlemanha = Paises("alemanha", None, 0)
        paisSuecia = Paises("suecia", None, 0)
        paisMoscou = Paises("moscou", None, 0)
        paisEgito = Paises("egito", None, 0)
        paisArgelia = Paises("argelia", None, 0)
        paisSudao = Paises("sudao", None, 0)
        paisCongo = Paises("congo", None, 0)
        paisAfricaDoSul = Paises("africa_do_sul", None, 0)
        paisMadagascar = Paises("madagascar", None, 0)
        paisVladvostok = Paises("vladvostok", None, 0)
        paisSiberia = Paises("siberia", None, 0)
        paisTchita = Paises("tchita", None, 0)
        paisDudinka = Paises("dudinka", None, 0)
        paisOmsk = Paises("omsk", None, 0)
        paisOmsk = Paises("aral", None, 0)
        paisOrienteMedio = Paises("oriente_medio", None, 0)
        paisMongolia = Paises("mongolia", None, 0)
        paisVietna = Paises("vietna", None, 0)
        paisJapao = Paises("japao", None, 0)
        paisChina = Paises("china", None, 0)
        paisIndia = Paises("india", None, 0)
        paisSumatra = Paises("sumatra", None, 0)
        paisBorneo = Paises("borneo", None, 0)
        paisNovaGuine = Paises("nova_guine", None, 0)
        paisAustralia = Paises("australia", None, 0)
        
        paises = [paisBrasil, paisPeru, paisVenezuela, paisMexico, paisNovaYork, paisCalifornia, paisOttawa,
                  paisVancouver, paisLabrador, paisMackenzie, paisGroenlandia, paisAlaska, paisIslandia, paisInglaterra,
                  paisFranca, paisPolonia, paisAlemanha, paisSuecia, paisMoscou, paisEgito, paisArgelia, paisSudao, paisCongo,
                  paisAfricaDoSul, paisMadagascar, paisVladvostok, paisSiberia, paisTchita, paisDudinka, paisOmsk, paisOmsk,
                  paisOrienteMedio, paisMongolia, paisVietna, paisJapao, paisChina, paisIndia, paisSumatra, paisBorneo, paisNovaGuine,
                  paisAustralia]
        
        objetivos = Objetivos.objetivos
        
        info = [fronteiras, exercitos, continentes, paises, objetivos]
        
        return info
    
    def atualizaObjetivo(objetivoIndex, jogo):
        jogo.objetivo = [objetivoIndex, Utilidades.carregarInformacoes()[4][objetivoIndex]]
        
    def RgbParaHex(rgb):
        return '{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    
    def coletarInfoCor(valor_hex: str):
        api_url = f"https://www.thecolorapi.com/id?hex={valor_hex}"
        resposta = requests.get(api_url)
        if resposta.status_code == 200:
            info_cor_json = resposta.json()
            nome = info_cor_json["name"]["value"]
            hexNomeProx = info_cor_json["name"]["closest_named_hex"]
            return Cor(nome, hexNomeProx)
        else:
            return "Falha ao obter informações da cor."