class Predicao:
    
    x = 0
    y = 0
    width = 0
    height = 0
    confidence = 0
    class_name = ""
    
    def __init__(self, x, y, largura, altura, confianca, classe):
        self.x = x
        self.y = y
        self.width = largura
        self.height = altura
        self.confidence = confianca
        self.class_name = classe