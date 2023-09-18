import os
from google.cloud import vision
from google.cloud.vision_v1 import types

client = vision.ImageAnnotatorClient()

def extract_troop_info(cropped_image_path):
     with open(cropped_image_path, 'rb') as image_file:
        content = image_file.read()

        vision_image = types.Image(content=content)
        
        response = client.text_detection(image=vision_image, max_results=1, image_context={"language_hints": ["pt"]})
        texts = response.text_annotations
        description = ""
        if texts:
            description = texts[0].description
        return description