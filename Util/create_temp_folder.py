import os

def create_temp_folder():
    temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    return temp_folder