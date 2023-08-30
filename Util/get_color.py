from Util.rgb_to_hex import rgb_to_hex
from Util.hex_to_rgb import hex_to_rgb
from Util.color_mapping import color_mapping

def get_color(pixel_color):
    rgb_color = hex_to_rgb(rgb_to_hex(pixel_color))
            
    closest_color = None
    min_distance = float('inf')
        
    for color_name, color_hex in color_mapping().items():
        color_rgb = hex_to_rgb(color_hex)
        distance = sum((a - b) ** 2 for a, b in zip(rgb_color, color_rgb))
                
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name
                
    return closest_color