class Predicao:
    
    x = 0
    y = 0
    width = 0
    height = 0
    confidence = 0
    class_name = ""
    image_path = ""
    predicao_type = ""
    
    def __init__(self, x, y, largura, altura, confianca, classe, caminhoImagem, predicao_tipo):
        self.x = x
        self.y = y
        self.width = largura
        self.height = altura
        self.confidence = confianca
        self.class_name = classe
        self.image_path = caminhoImagem
        self.predicao_type = predicao_tipo
        
    def __str__(self):
        return f"Predicao(class_name={self.class_name}, x={self.x}, y={self.y}, width={self.width}, height={self.height}, confidence={self.confidence}, image_path={self.image_path}, predicao_type={self.predicao_type})"
    