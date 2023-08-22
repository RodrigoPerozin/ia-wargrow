from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from google.cloud.vision_v1 import types
from classes.Utilidades import *
from google.cloud import vision
from classes.Predicao import *
from roboflow import Roboflow
from classes.Cor import *
from PIL import Image
import requests
import uvicorn
import json
import os
import io

app = FastAPI()

# Configuração do Google Cloud Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

#Configs Roboflow
rf = Roboflow(api_key="81gG6yXrCsPPzbHBRCuK")
project = rf.workspace().project("war-ia")
model = project.version(1).model

#variables
confianca = 20
sobrepos = 20

#class ImagePredicao:
#    def __init__(self, predicaos, image_width, image_height):
#        self.predicaos = predicaos
#       self.image_width = image_width
#       self.image_height = image_height
#
#    def __str__(self):
#        return f"ImagePredicao(predicaos={self.predicaos}, image_width={self.image_width}, image_height={self.image_height})"

@app.post("/predicao/")
async def predicaoJson(image: UploadFile = File(...)):
    try:
        conteudo = await image.read()
        imagemPIL = Image.open(io.BytesIO(conteudo))
        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        pastaTemporaria = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(pastaTemporaria):
            os.makedirs(pastaTemporaria)
        caminhoImagem = os.path.join(pastaTemporaria, "temp_image.png")
        imagemPIL.save(caminhoImagem)
        dados = model.predict(caminhoImagem, confidence=confianca, overlap=sobrepos).json()
        os.remove(caminhoImagem)  # Remover a imagem temporária após a previsão

        return dados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predicao-paises/")
async def predicao_paises(imagem: UploadFile = File(...)):
    try:
        conteudo = await imagem.read()
        imagemPIL = Image.open(io.BytesIO(conteudo))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        pastaTemporaria = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(pastaTemporaria):
            os.makedirs(pastaTemporaria)
        caminhoImagem = os.path.join(pastaTemporaria, "temp_image.png")
        imagemPIL.save(caminhoImagem)

        dados = model.predict(caminhoImagem, confidence=confianca, overlap=sobrepos).json()
        os.remove(caminhoImagem)  # Remover a imagem temporária após a previsão

        predicaos = []
        nomes_classe_achados = [] 

        for predicao_dados in dados["predictions"]:
            predicao = Predicao(
                x=predicao_dados["x"],
                y=predicao_dados["y"],
                width=predicao_dados["width"],
                height=predicao_dados["height"],
                confidence=predicao_dados["confidence"],
                class_name=predicao_dados["class"],
                image_path=predicao_dados["image_path"],
                predicao_type=predicao_dados["predicao_type"]
            )
            predicaos.append(predicao)
            
            if predicao_dados["class"] not in nomes_classe_achados:
                nomes_classe_achados.append(predicao_dados["class"])
                
        return {
            "Quantidade de Paises: ": len(nomes_classe_achados),
            "Paises Encontrados": nomes_classe_achados
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/visualizar-predicao/")
async def visualizar_predicao(imagem: UploadFile = File(...)):
    try:
        conteudo = await imagem.read()
        imagemPIL = Image.open(io.BytesIO(conteudo))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        pastaTemporaria = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(pastaTemporaria):
            os.makedirs(pastaTemporaria)
        caminhoImagemParam = os.path.join(pastaTemporaria, "temp_image.png")
        imagemPIL.save(caminhoImagemParam)

        dados = model.predict(caminhoImagemParam, confidence=confianca, overlap=sobrepos)

        pastaTemporaria = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(pastaTemporaria):
            os.makedirs(pastaTemporaria)
        
        nomeArquivoImagem = "Resultado.png"
        caminhoImagem = os.path.join(pastaTemporaria, nomeArquivoImagem)

        dados.save(output_path=caminhoImagem)

        if not os.path.exists(caminhoImagem):
            raise HTTPException(status_code=404, detail="Imagem não encontrada.")
        
        os.remove(caminhoImagemParam)
        return FileResponse(caminhoImagem)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/coletar-cor-pixel/")
async def coletar_cor_pixel(imagem: UploadFile = File(...)):
    try:
        conteudo = await imagem.read()
        imagemPIL = Image.open(io.BytesIO(conteudo))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        pastaTemporaria = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(pastaTemporaria):
            os.makedirs(pastaTemporaria)
        caminhoImagem = os.path.join(pastaTemporaria, "temp_image.png")
        imagemPIL.save(caminhoImagem)
        
        

        imagem_predicao = model.predict(caminhoImagem, confidence=confianca, overlap=sobrepos)
        imagem_predicao.save(output_path=os.path.join(pastaTemporaria, "Resultado.png"))
    
        dados = imagem_predicao.json()
        predicaos = []
        
        for predicao_data in dados["predicaos"]:
            predicoes = Predicao(
                x=predicao_data["x"],
                y=predicao_data["y"],
                width=predicao_data["width"],
                height=predicao_data["height"],
                confidence=predicao_data["confidence"],
                class_name=predicao_data["class"],
                image_path=predicao_data["image_path"],
                predicao_type=predicao_data["predicao_type"]
            )
            predicoes.append(predicoes)
    
        caminhoImagem = os.path.join(pastaTemporaria, "Resultado.png")
        imagem = Image.open(caminhoImagem)

        resultado = []

        for pred in predicoes:
            x = pred.x
            y = pred.y
            
            largura, altura = imagem.size
            if x < 0 or x >= largura or y < 0 or y >= altura:
                continue

            cor_pixel = imagem.getpixel((x, y))
            
            info_cor = Utilidades.coletarInfoCor(Utilidades.RgbParaHex(cor_pixel))

            resultado.append({"class_name": pred.class_name, "color_name": info_cor.nome, "hex": info_cor.hexNomeProx})

        os.remove(caminhoImagem)  # Remover a imagem temporária após o processamento

        return resultado

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/value")
async def extract_text_from_image(image: UploadFile = File(...)):
    try:
        conteudo = await image.read()
        imagemPIL = Image.open(io.BytesIO(conteudo))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        pastaTemporaria = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(pastaTemporaria):
            os.makedirs(pastaTemporaria)
        caminhoImagem = os.path.join(pastaTemporaria, "temp_image.png")
        imagemPIL.save(caminhoImagem)

        confidence = 20
        overlap = 20
        predict_image = model.predict(caminhoImagem, confidence=confianca, overlap=sobrepos)
    
        data = predict_image.json()
        predicaos = []
        
        for predicao_data in data["predicaos"]:
            predicao = Predicao(
                x=predicao_data["x"],
                y=predicao_data["y"],
                width=predicao_data["width"],
                height=predicao_data["height"],
                confidence=predicao_data["confidence"],
                class_name=predicao_data["class"],
                image_path=predicao_data["image_path"],
                predicao_type=predicao_data["predicao_type"]
            )
            predicaos.append(predicao)
        
        result = []
        image_paths = []

        image_original = os.path.join(pastaTemporaria, "temp_image.png")
        
        for pred in predicaos:
            x = pred.x
            y = pred.y
            width = pred.width
            height = pred.height
            
            image_or = Image.open(image_original)
            caminhoImagem = os.path.join(pastaTemporaria, pred.class_name + '.png')
            
            x1 = x - width / 2
            x2 = x + width / 2
            y1 = y - height / 2
            y2 = y + height / 2

            # Verificações para garantir que as coordenadas não estejam fora dos limites da imagem
            image_width, image_height = image_or.size
            x1 = max(0, x1)
            x2 = min(image_width, x2)
            y1 = max(0, y1)
            y2 = min(image_height, y2)

            box = (x1, y1, x2, y2)
            cropped_image = image_or.crop(box=box)
            cropped_image.save(caminhoImagem)
            image_paths.append({"class_name": pred.class_name, "image_path": image_path})
            
        for images in image_paths:
            client = vision.ImageAnnotatorClient()
            with open(images["image_path"], 'rb') as image_file:
                conteudo = image_file.read()

            image = types.Image(content=content)
            response = client.text_detection(image=image, max_results=1, image_context={"language_hints": ["pt"]})
            texts = response.text_annotations
            if len(texts) > 0:
                result.append({"class_name": images["class_name"], "troop": texts[1].description})
                for text in texts: 
                    class_name_exists = any(entry["class_name"] == images["class_name"] for entry in result)
                    if not class_name_exists: 
                        result.append({"class_name": images["class_name"], "value": texts[1].description})
            else:
                class_name_exists = any(entry["class_name"] == images["class_name"] for entry in result)
                if not class_name_exists:
                    result.append({"class_name": images["class_name"], "troop": "Não identificado"})
                    
        # Remover os arquivos de imagem temporários
        for images in image_paths:
            os.remove(images["image_path"])

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predict/result")
async def apply_logic():
    with open('resultado.json', 'r') as json_file:
        data = json.load(json_file)
        
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
