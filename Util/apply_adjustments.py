def apply_adjustments(class_name, x, y):
    adjustments = {
        "Peru": (-7, -60),
        "Argentina": (-10, 0),
        "Mexico": (-9, 7),
        "Venezuela": (0, 3),
        "Suecia": (-7, 0),
        "Polonia": (5, -6),
        "Islandia": (7, 0),
        "Inglaterra": (7, 0),
        "Sudao": (-10, 0),
        "Madagascar": (-10, 0),
        "Dudinka": (8, 0),
        "india": (-10, 0),
        "Nova Guine": (-3, 0),
        "Groenlandia": (0, 0),
        "Moscou": (0, -10),
        "Vancouver": (10, 0),
        "Inglaterra": (10, 10),
        "Suecia": (-10, 10),
        "Egito": (20, -4),
        "Omsk": (5, 5),
        "Aral": (7, 0),
        "Borneo": (11, 7),
        "Nova Guine": (-11, -4)
    }
    
    adjustment = adjustments.get(class_name, (0, 0))
    x_adjusted, y_adjusted = x + adjustment[0], y + adjustment[1]
    
    return x_adjusted, y_adjusted
