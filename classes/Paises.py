class Paises:

  def __init__(self, pais=None, cor=None, exercitos=0):
    self.pais = pais
    self.cor = cor
    self.exercitos = exercitos
      
  def __str__(self):
    return f"Paises(pais={self.pais}, cor={self.cor}, exercitos={self.exercitos})"