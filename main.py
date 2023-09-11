import uvicorn
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
    
if __name__ == "__main__":
    uvicorn.run("Controller.ImagePredictionController:app", host="localhost", port=8000, reload=True)
