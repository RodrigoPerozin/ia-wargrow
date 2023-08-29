from fastapi import File, UploadFile
from PIL import Image, ImageDraw
import io
import os
import json
from fastapi import HTTPException
from fastapi.responses import FileResponse

from Util.apply_adjustments import apply_adjustments
from Util.create_temp_folder import create_temp_folder
from Util.hex_to_rgb import hex_to_rgb
from Util.get_folder_temp import get_folder_temp
from Util.rgb_to_hex import rgb_to_hex
from Util.color_mapping import color_mapping
from Util.save_temp_image import save_temp_image
from Model.Prediction import Prediction
from Model.RoboflowPredictor import RoboflowPredictor

async def predict_json(image: UploadFile = File(...)):
    content = await image.read()
    pil_image = Image.open(io.BytesIO(content))

    # Salvar a imagem temporariamente para poder passar o caminho para o modelo
    image_path = save_temp_image(pil_image)
    roboflow_instance = RoboflowPredictor()  
    data = await roboflow_instance.predict_json(image_path)
        
    os.remove(image_path)  # Remover a imagem temporária após a previsão

    return data
    
async def predict_countries_map(image: UploadFile = File(...)):
    content = await image.read()
    pil_image = Image.open(io.BytesIO(content))

    # Salvar a imagem temporariamente para poder passar o caminho para o modelo
    image_path = save_temp_image(pil_image)
    
    roboflow_instance = RoboflowPredictor()  
    data = await roboflow_instance.predict_json(image_path)
    os.remove(image_path)  # Remover a imagem temporária após a previsão

    class_names_found = [] 

    for prediction_data in data["predictions"]:            
        if prediction_data["class"] not in class_names_found:
            class_names_found.append(prediction_data["class"])
                
    return {
        "Quantidade de Paises: ": len(class_names_found),
        "Paises Encontrados": class_names_found
    }
    
async def predict_view_result(image: UploadFile = File(...)):
    content = await image.read()
    pil_image = Image.open(io.BytesIO(content))

    # Salvar a imagem temporariamente para poder passar o caminho para o modelo
    image_path_param = save_temp_image(pil_image)

    pil_image.save(image_path_param)
    
    roboflow_instance = RoboflowPredictor()  
    data = await roboflow_instance.predict_view(image_path_param)
    
    temp_folder = create_temp_folder()

    image_path = os.path.join(temp_folder, "Resultado.png")

    data.save(output_path=image_path)

    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada.")
        
    os.remove(image_path_param)
    return FileResponse(image_path)

async def get_colors_image(image: UploadFile = File(...)):
    content = await image.read()
    temp_folder = get_folder_temp()
    pil_image = Image.open(io.BytesIO(content))
    
    image_path = save_temp_image(pil_image)

    roboflow_instance = RoboflowPredictor()  
    data = await roboflow_instance.predict_json(image_path)
    
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
        x, y = apply_adjustments(pred.class_name, pred.x, pred.y)
        pixel_color = pil_image.getpixel((x, y)) 
        
        rgb_color = hex_to_rgb(rgb_to_hex(pixel_color))
            
        closest_color = None
        min_distance = float('inf')
        
        for color_name, color_hex in color_mapping().items():
            color_rgb = hex_to_rgb(color_hex)
            distance = sum((a - b) ** 2 for a, b in zip(rgb_color, color_rgb))
                
            if distance < min_distance:
                min_distance = distance
                closest_color = color_name

        result.append({"class_name": pred.class_name, "color_name": closest_color})
            
            
        radius = 20
        ellipse_coords = (x - radius, y - radius, x + radius, y + radius)
            
        draw.ellipse(ellipse_coords, outline=(255, 255, 255))
            
    marked_image_path = os.path.join(temp_folder, "marked_image.png")
    marked_image.save(marked_image_path)
        
    return result


async def get_data_test():
    try:
        with open("resultado.json", 'r') as json_file:
            conteudo = json.load(json_file)
        return conteudo
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

    