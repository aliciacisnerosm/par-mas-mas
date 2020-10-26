'''
  * push al stack operadores
  * push al stack de operandos
  * push al stack de saltos 
  * push al stack de tipos 

  se genera el cuadruplo con el operador, 2 operandos

  pendientes: 
  * Integrar puntos neuralgicos & sus funciones
  * Crear las funciones en el codigo intermedio
  * Generar los cuadruplos 


'''


from queue import LifoQueue
import par_mas_mas.compilador.types as type

class IntermediateCode:
  def __init__(self):  
    self.stackOperators = LifoQueue()
    self.stackOperands = LifoQueue()
    self.stackJumps = LifoQueue()
    self.stackTypes = LifoQueue()
    self.listQuadruples = []
    
  def push_Operators(self, operator):
      self.stackOperators.push(operator)

  def push_Operands(self, operands):
      self.stackOperands.push(operands)

  def push_Jumps(self, jump):
      self.stackJumps.push(jumps)
	
	def push_Types(self,type):
			self.stackTypes.push(types)
  

  

