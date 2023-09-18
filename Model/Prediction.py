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
