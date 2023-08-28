from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from roboflow import Roboflow
import uvicorn
import os
from PIL import Image, ImageDraw
import requests
import io
import json

from google.cloud import vision
from google.cloud.vision_v1 import types

## Configuração do Google Cloud Vision API ##
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


rf = Roboflow(api_key="81gG6yXrCsPPzbHBRCuK")
app = FastAPI()
project = rf.workspace().project("war-ia")
model = project.version(1).model
confidence = 20
overlap = 20

class Prediction:
    def __init__(self, x, y, width, height, confidence, class_name, image_path, prediction_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.confidence = confidence
        self.class_name = class_name
        self.image_path = image_path
        self.prediction_type = prediction_type

    def __str__(self):
        return f"Prediction(class={self.class_name}, x={self.x}, y={self.y}, width={self.width}, height={self.height}, confidence={self.confidence}, image_path={self.image_path}, prediction_type={self.prediction_type})"

class ImagePrediction:
    def __init__(self, predictions, image_width, image_height):
        self.predictions = predictions
        self.image_width = image_width
        self.image_height = image_height

    def __str__(self):
        return f"ImagePrediction(predictions={self.predictions}, image_width={self.image_width}, image_height={self.image_height})"
    
class ColorInfo:
    def __init__(self, name_value, closest_named_hex):
        self.value = name_value
        self.closest_named_hex = closest_named_hex
    
def rgb_to_hex(rgb):
    return '{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    

# def get_color_info_api(hex_value: str):
#     api_url = f"https://www.thecolorapi.com/id?hex={hex_value}"
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         color_info_json = response.json()
#         name_value = color_info_json["name"]["value"]
#         closest_named_hex = color_info_json["name"]["closest_named_hex"]
#         return ColorInfo(name_value, closest_named_hex)
#     else:
#         return "Falha ao obter informações da cor."
    
color_mapping = {
    "Amarelo": "#FFFF00",
    "Vermelho": "#FF0000",
    "Verde": "#008000",
    "Roxo": "#800080",
    "Azul": "#0000FF"
}

@app.post("/predict/")
async def predict_json(image: UploadFile = File(...)):
    try:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_path = os.path.join(temp_folder, "temp_image.png")
        pil_image.save(image_path)

        data = model.predict(image_path, confidence=confidence, overlap=overlap).json()
        os.remove(image_path)  # Remover a imagem temporária após a previsão

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-countries/")
async def predict_countries(image: UploadFile = File(...)):
    try:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_path = os.path.join(temp_folder, "temp_image.png")
        pil_image.save(image_path)

        data = model.predict(image_path, confidence=confidence, overlap=overlap).json()
        os.remove(image_path)  # Remover a imagem temporária após a previsão

        predictions = []
        class_names_found = [] 

        for prediction_data in data["predictions"]:
            prediction = Prediction(
                x=prediction_data["x"],
                y=prediction_data["y"],
                width=prediction_data["width"],
                height=prediction_data["height"],
                confidence=prediction_data["confidence"],
                class_name=prediction_data["class"],
                image_path=prediction_data["image_path"],
                prediction_type=prediction_data["prediction_type"]
            )
            predictions.append(prediction)
            
            if prediction_data["class"] not in class_names_found:
                class_names_found.append(prediction_data["class"])
                
        return {
            "Quantidade de Paises: ": len(class_names_found),
            "Paises Encontrados": class_names_found
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-view/")
async def predict_view(image: UploadFile = File(...)):
    try:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_path_param = os.path.join(temp_folder, "temp_image.png")
        pil_image.save(image_path_param)

        data = model.predict(image_path_param, confidence=confidence, overlap=overlap)

        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        
        image_filename = "Resultado.png"
        image_path = os.path.join(temp_folder, image_filename)

        data.save(output_path=image_path)

        if not os.path.exists(image_path):
            raise HTTPException(status_code=404, detail="Imagem não encontrada.")
        
        os.remove(image_path_param)
        return FileResponse(image_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/get-pixel-color/")
async def get_pixel_color(image: UploadFile = File(...)):
    try:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_path = os.path.join(temp_folder, "temp_image.png")
        pil_image.save(image_path)

        predict_image = model.predict(image_path, confidence=confidence, overlap=overlap)
    
        data = predict_image.json()
        predictions = []
        
        for prediction_data in data["predictions"]:
            prediction = Prediction(
                x=prediction_data["x"],
                y=prediction_data["y"],
                width=prediction_data["width"],
                height=prediction_data["height"],
                confidence=prediction_data["confidence"],
                class_name=prediction_data["class"],
                image_path=prediction_data["image_path"],
                prediction_type=prediction_data["prediction_type"]
            )
            predictions.append(prediction)
        
        image = Image.open(image_path)

        result = []

        for pred in predictions:
            x = pred.x
            y = pred.y
            
            width, height = image.size
            if x < 0 or x >= width or y < 0 or y >= height:
                continue

            pixel_color = image.getpixel((x, y))
            
            rgb_color = hex_to_rgb(rgb_to_hex(pixel_color))
            
            closest_color = None
            min_distance = float('inf')
            
            for color_name, color_hex in color_mapping.items():
                color_rgb = hex_to_rgb(color_hex)
                distance = sum((a - b) ** 2 for a, b in zip(rgb_color, color_rgb))
                
                if distance < min_distance:
                    min_distance = distance
                    closest_color = color_name

            result.append({"class_name": pred.class_name, "color_name": closest_color})

        os.remove(image_path)  # Remover a imagem temporária após o processamento
        
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/value")
async def extract_text_from_image(image: UploadFile = File(...)):
    try:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_path = os.path.join(temp_folder, "temp_image.png")
        pil_image.save(image_path)

        confidence = 20
        overlap = 20
        predict_image = model.predict(image_path, confidence=confidence, overlap=overlap)
    
        data = predict_image.json()
        predictions = []
        
        for prediction_data in data["predictions"]:
            prediction = Prediction(
                x=prediction_data["x"],
                y=prediction_data["y"],
                width=prediction_data["width"],
                height=prediction_data["height"],
                confidence=prediction_data["confidence"],
                class_name=prediction_data["class"],
                image_path=prediction_data["image_path"],
                prediction_type=prediction_data["prediction_type"]
            )
            predictions.append(prediction)
        
        result = []

        image_original = os.path.join(temp_folder, "temp_image.png")
        image_paths = []
        
        for pred in predictions:
            x = pred.x
            y = pred.y
            width = pred.width
            height = pred.height
            
            image_or = Image.open(image_original)
            image_path = os.path.join(temp_folder, pred.class_name + '.png')
            
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
            cropped_image.save(image_path)
            image_paths.append({"class_name": pred.class_name, "image_path": image_path})
            
        for images in image_paths:
            client = vision.ImageAnnotatorClient()
            with open(images["image_path"], 'rb') as image_file:
                content = image_file.read()

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
        # for images in image_paths:
        #     os.remove(images["image_path"])

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/predict/result")
async def apply_logic():
    with open('resultado.json', 'r') as json_file:
        data = json.load(json_file)
    
    
    return data

@app.post("/examine-pixel/")
async def get_pixel_color(image: UploadFile = File(...)):
    try:
        content = await image.read()
        pil_image = Image.open(io.BytesIO(content))

        # Salvar a imagem temporariamente para poder passar o caminho para o modelo
        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        image_path = os.path.join(temp_folder, "temp_image.png")
        pil_image.save(image_path)

        predict_image = model.predict(image_path, confidence=confidence, overlap=overlap)
    
        data = predict_image.json()
        predictions = []
        
        for prediction_data in data["predictions"]:
            prediction = Prediction(
                x=prediction_data["x"],
                y=prediction_data["y"],
                width=prediction_data["width"],
                height=prediction_data["height"],
                confidence=prediction_data["confidence"],
                class_name=prediction_data["class"],
                image_path=prediction_data["image_path"],
                prediction_type=prediction_data["prediction_type"]
            )
            predictions.append(prediction)
        
        image = Image.open(image_path)

        marked_image = pil_image.copy()
        draw = ImageDraw.Draw(marked_image)
        result = []
        
        for pred in predictions:
            x = pred.x
            y = pred.y
            
            if pred.class_name == "Peru":   
                x = x - 7
            if pred.class_name == "Argentina":
                x = x + 5
            if pred.class_name == "Mexico":
                x = x - 9
                y = y + 7
            if pred.class_name == "Venezuela":
                y = y + 3
            if pred.class_name == "Suecia":
                x = x - 7
            if pred.class_name == "Polinia":
                y = y - 6
                x = x + 5
            if pred.class_name == "Egito":
                x = x + 7
            if pred.class_name == "Islandia":
                x = x + 7
            if pred.class_name == "Inglaterra":
                x = x + 7
            if pred.class_name == "Sudao":
                x = x - 10
            if pred.class_name == "Madagascar":
                x = x - 10
            if pred.class_name == "Dudinka":
                x = x + 8
            if pred.class_name == "india":
                x = x - 10
            if pred.class_name == "Nova Guine":
                x = x - 3
            if pred.class_name == "Groenlandia":
                y = y - 40
            
                    
            pixel_color = pil_image.getpixel((x, y)) 
            
            rgb_color = hex_to_rgb(rgb_to_hex(pixel_color))
            
            closest_color = None
            min_distance = float('inf')
            
            for color_name, color_hex in color_mapping.items():
                color_rgb = hex_to_rgb(color_hex)
                distance = sum((a - b) ** 2 for a, b in zip(rgb_color, color_rgb))
                
                if distance < min_distance:
                    min_distance = distance
                    closest_color = color_name

            result.append({"class_name": pred.class_name, "color_name": closest_color})
            
            
            radius = 1
            ellipse_coords = (x - radius, y - radius, x + radius, y + radius)
            
            draw.ellipse(ellipse_coords, outline=(255, 255, 255))
        
        marked_image_path = os.path.join(temp_folder, "marked_image.png")
        marked_image.save(marked_image_path)
        
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
