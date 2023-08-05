from typing import Union
from fastapi import FastAPI
from roboflow import Roboflow
import uvicorn

rf = Roboflow(api_key="VaFSU2CW1skuZYeidgCM")
app = FastAPI()
project = rf.workspace().project("project_demo-jlcme")
model = project.version(3).model

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


@app.get("/predict/")
def predict_image(image_path: str):
    confidence = 40
    overlap = 30
    data = model.predict(image_path, confidence=confidence, overlap=overlap).json()
    return data

@app.get("/predict-countries/")
def predict_image(image_path: str):
    confidence = 40
    overlap = 30
    data = model.predict(image_path, confidence=confidence, overlap=overlap).json()
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
