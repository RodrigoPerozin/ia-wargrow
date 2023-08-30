def apply_class_adjustments(class_name, x, y, x_radius, y_radius):
        if class_name == "Brasil":
            x = x + 15
        elif class_name == "Argentina":
            y_radius = y_radius - 10
            x_radius = x_radius - 10
            
        elif class_name == "Peru":
            x = x + 20
            y = y - 30
            y_radius = y_radius - 50
            x_radius = x_radius + 20
            
        elif class_name == "Venezuela":
            x_radius = x_radius - 10
            
        elif class_name == "Mexico":
            y_radius = y_radius - 20
            
        elif class_name == "California":
            x_radius = x_radius - 10
            
        elif class_name == "Labrador":
            y_radius = y_radius - 20
            
        elif class_name == "Vancouver":
            x_radius = x_radius - 20
            
        elif class_name == "Mackenzie":
            x_radius = x_radius - 20
            y = y + 10
            
        elif class_name == "Alaska":
            x = x + 30
        
        elif class_name == "Vladvostok":
            x = x + 50
            y_radius = y_radius - 30
            
        elif class_name == "Groenlandia":
            y = y + 25
        
        elif class_name == "Africa do Sul":
            x = x + 10
            y = y + 10
            x_radius = x_radius - 20
        
        elif class_name == "Madagascar":
            y_radius = y_radius - 10
            x_radius = x_radius + 20
            x = x + 10
        
        elif class_name == "Congo":
            x = x + 10
            x_radius = x_radius - 20
            
        elif class_name == "Sudao":
            y = y + 10
            y_radius = y_radius - 20
            x = x + 10
            
        elif class_name == "Franca":
            x = x - 10
            x_radius = x_radius - 20
            y_radius = y_radius - 10
            y = y + 10
            
        elif class_name == "Suecia":
            y_radius = y_radius - 20
            
        elif class_name == "Oriente Medio":
            y_radius = y_radius - 20
            
        elif class_name =="Omsk":
            x_radius = x_radius - 40
            y_radius = y_radius + 10
        
        elif class_name == "india":
            x_radius = x_radius - 20
            x = x + 10
            
        elif class_name == "China":
            x_radius = x_radius - 10
            x = x + 15
            y = y + 10
            
        elif class_name == "Vietna":
            y_radius = y_radius - 10
            
        elif class_name == "Japao":
            x_radius = x_radius - 10
            y = y + 20
            
        return x, y, x_radius, y_radius
    