from fastapi import FastAPI
import uvicorn
from Controller.ImagePredictionController import app 
    
if __name__ == "__main__":
    uvicorn.run("Controller.ImagePredictionController:app", host="0.0.0.0", port=8000, reload=True)
