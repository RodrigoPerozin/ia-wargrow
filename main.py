import uvicorn
import os

<<<<<<< Updated upstream
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
=======
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nicolas/studyspace/projects-senai/ia-wargrow/key.json"
>>>>>>> Stashed changes
    
if __name__ == "__main__":
    uvicorn.run("Controller.ImagePredictionController:app", host="localhost", port=8000, reload=True)
