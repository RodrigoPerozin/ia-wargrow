import uvicorn
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\projetos\ia-war\ia-wargrow\key.json"
    
if __name__ == "__main__":
    uvicorn.run("Controller.ImagePredictionController:app", host="0.0.0.0", port=8000, reload=True)
