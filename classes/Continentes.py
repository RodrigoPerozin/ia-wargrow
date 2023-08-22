class Continentes:
  
  def __init__(self, continente, paises):
    self.continente = continente
    self.paises = paises
    
  def __str__(self):
    return f"Continentes(continente={self.continente}, paises={self.paises})"