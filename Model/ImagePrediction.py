class ImagePrediction:
    def __init__(self, predictions, image_width, image_height):
        self.predictions = predictions
        self.image_width = image_width
        self.image_height = image_height

    def __str__(self):
        return f"ImagePrediction(predictions={self.predictions}, image_width={self.image_width}, image_height={self.image_height})"
