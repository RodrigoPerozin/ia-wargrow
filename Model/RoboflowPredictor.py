from roboflow import Roboflow

class RoboflowPredictor:
    def __init__(self):
        self.rf = Roboflow(api_key="81gG6yXrCsPPzbHBRCuK")
        self.project = self.rf.workspace().project("war-ia")
        self.model = self.project.version(1).model
        self.confidence = 7
        self.overlap = 1

    async def predict_json(self, image_path):
        return self.model.predict(image_path, confidence=self.confidence, overlap=self.overlap).json()

    async def predict_view(self, image_path):
        return self.model.predict(image_path, confidence=self.confidence, overlap=self.overlap)