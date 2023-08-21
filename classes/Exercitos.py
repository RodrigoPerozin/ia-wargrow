class Exercitos:
  
  def __init__(self, cor, exercitos):
    self.cor = cor
    self.exercitos = exercitos
      
  def __str__(self):
    return f"Exercitos(cor={self.cor}, exercitos={self.exercitos})"