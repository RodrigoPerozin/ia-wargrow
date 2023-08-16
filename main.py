from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from roboflow import Roboflow
import uvicorn
import os
from PIL import Image
import requests
import io

from google.cloud import vision
from google.cloud.vision_v1 import types

## Configuração do Google Cloud Vision API ##
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


rf = Roboflow(api_key="81gG6yXrCsPPzbHBRCuK")
app = FastAPI()
project = rf.workspace().project("war-ia")
model = project.version(1).model

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
    

def get_color_info_api(hex_value: str):
    api_url = f"https://www.thecolorapi.com/id?hex={hex_value}"
    response = requests.get(api_url)

    if response.status_code == 200:
        color_info_json = response.json()
        name_value = color_info_json["name"]["value"]
        closest_named_hex = color_info_json["name"]["closest_named_hex"]
        return ColorInfo(name_value, closest_named_hex)
    else:
        return "Falha ao obter informações da cor."

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

        confidence = 40
        overlap = 30
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

        confidence = 40
        overlap = 30
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

        confidence = 40
        overlap = 30
        data = model.predict(image_path_param, confidence=confidence, overlap=overlap)

        temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        
        image_filename = "Resultado.png"
        image_path = os.path.join(temp_folder, image_filename)

        data.save(output_path=image_path)
        print(image_path)

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

        confidence = 40
        overlap = 30
        predict_image = model.predict(image_path, confidence=confidence, overlap=overlap)
        predict_image.save(output_path=os.path.join(temp_folder, "Resultado.png"))
    
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
    
        image_path = os.path.join(temp_folder, "Resultado.png")
        image = Image.open(image_path)

        result = []

        for pred in predictions:
            x = pred.x
            y = pred.y
            
            width, height = image.size
            if x < 0 or x >= width or y < 0 or y >= height:
                continue

            pixel_color = image.getpixel((x, y))
            
            color_info = get_color_info_api(rgb_to_hex(pixel_color))

            result.append({"class_name": pred.class_name, "color_name": color_info.value, "hex": color_info.closest_named_hex})

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

        confidence = 40
        overlap = 30
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
        image_paths = []

        image_original = os.path.join(temp_folder, "temp_image.png")
        
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
            
        print(image_paths)
        for images in image_paths:
            client = vision.ImageAnnotatorClient()
            with open(images["image_path"], 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)
            response = client.text_detection(image=image, max_results=1, image_context={"language_hints": ["pt"]})
            texts = response.text_annotations
            print(texts)
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
