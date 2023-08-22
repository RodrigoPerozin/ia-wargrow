class Fronteiras:
    def __init__(self, pais, fronteiras):
        self.pais = pais
        self.fronteiras = fronteiras
        
    def __str__(self):
        return f"Fronteiras(pais={self.pais}, fronteiras={self.fronteiras})"