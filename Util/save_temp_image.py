import os


async def save_temp_image(pil_image):
    temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    image_path = os.path.join(temp_folder, "temp_image.png")
    pil_image.save(image_path)
    return image_path