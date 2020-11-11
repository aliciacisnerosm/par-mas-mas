from collections import deque
class VirtualMachine:
	def __init__(self, arr_quadruples, general_dir):
		self.memory = MemoryMap(arr_quadruples, general_dir)
		self.arr_quadruples = arr_quadruples
		self.execution_stack = deque()


	def process_quadruples(self):
		pointer = 0
		while (pointer < len(self.arr_quadruples)):

			if self.arr_quadruples[pointer][0] == '+':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value + right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '-':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value - right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '=':
				left_value = self.memory.get_value(self.arr_quadruples[pointer][1])
				self.memory.set_value(self.arr_quadruples[pointer][3], left_value)
				print("valor asignacion", left_value)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '*':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value * right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '/':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value / right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == 'read':
				result = self.memory.get_value(self.arr_quadruples[pointer][3])
				print("este es el result de read",result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0]== 'write':
				result = self.memory.get_value(self.arr_quadruples[pointer][3])
				print(result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == 'and':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value and right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == 'or':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value or right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '>':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value > right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '<':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value < right_value
				print(left_value, right_value, result, "<<<<<<<<", self.arr_quadruples[pointer][3])
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1

			elif self.arr_quadruples[pointer][0] == '>=':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value >= right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '<=':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value <= right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '<>':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value != right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
				
			elif self.arr_quadruples[pointer][0] == '==':
				left_value =  self.memory.get_value(self.arr_quadruples[pointer][1])
				right_value = self.memory.get_value(self.arr_quadruples[pointer][2])
				result = left_value == right_value
				self.memory.set_value(self.arr_quadruples[pointer][3], result)
				pointer += 1
			elif self.arr_quadruples[pointer][0] == 'GOTO':
				print("este es pointer goto",pointer)
				next_quadruple = self.arr_quadruples[pointer][3]
				print(next_quadruple)
				pointer = next_quadruple
			elif self.arr_quadruples[pointer][0] == 'ERA':
				self.execution_stack.append(pointer)
				pointer +=1
			elif self.arr_quadruples[pointer][0] == 'ENDFUNC':
				pointer = self.execution_stack.pop()
				pointer +=1
			elif self.arr_quadruples[pointer][0] == 'GOTOF':
				left_value = self.memory.get_value(self.arr_quadruples[pointer][1])
				print(left_value, "left_value")
				if left_value == False:
					pointer = self.arr_quadruples[pointer][3]
					print(pointer)
				else:
					pointer += 1

			else:
				pointer += 1

	def execute(self): 
		print("entra a execute")
		self.memory.fill_memories()
		self.process_quadruples()



class MemoryMap:
		def __init__(self, arr_quadruples, general_dir):
				#int,float,char,bool
				self.global_memory = [dict(), dict(), dict(),dict()]
				#int,float,char,bool
				self.local_memory = [dict(), dict(), dict(), dict()]
				#int,float,char,string
				self.constant_memory = [dict(), dict(), dict(), dict()]
				self.execution_stack = deque()

				self.arr_quadruples = arr_quadruples
				self.general_dir = general_dir

				self.global_vars = dict()
				self.const_vars = dict()


		def separate_vars(self):
			list_keys = list(self.general_dir['global_var'].keys())
			for i in list_keys:
				if i != 'global_var_names':
					if self.general_dir['global_var'][i]['kind'] == 'variable_name':
						self.global_vars[i] = self.general_dir['global_var'][i]
					elif self.general_dir['global_var'][i]['kind'] == 'const_variable':
						self.const_vars[i] = self.general_dir['global_var'][i]

		def fill_global_memory(self):
				for var in self.global_vars:
						if var >= 1000 and var < 2000:
								self.global_memory[0][var] = {
										'memory_dir': var,
										'value': None # PENDIENTE
								}
						elif var >= 2000 and var < 3000:
								 self.global_memory[1][var] = {
										'memory_dir': var,
										'value': None # PENDIENTE
								}
						elif var >= 3000 and var < 4000:
								 self.global_memory[2][var] = {
										'memory_dir': var,
										'value': None # PENDIENTE
								}

		def fill_constant_memory(self):
			print(self.const_vars)
			for var in self.const_vars:
					if var >= 15000 and var < 16000:
							self.constant_memory[0][var] = {
									'memory_dir': var,
									'value': self.const_vars[var]['value']
							}

					elif var >= 16000 and var < 17000:
							self.constant_memory[1][var] = {
									'memory_dir': var,
									'value': self.const_vars[var]['value']
							}

					elif var >= 17000 and var < 18000:
							self.constant_memory[2][var] = {
									'memory_dir': var,
									'value': self.const_vars[var]['value']
							}
					elif var >= 18000 and var < 19000:
							self.constant_memory[3][var] = {
									'memory_dir': var,
									'value': self.const_vars[var]['value']
							}
		


		def get_value(self, memory_dir):
				print(self.local_memory, "local mem",  self.global_memory)
				if (memory_dir >= 15000 and memory_dir < 19000) or (memory_dir >= 1000 and memory_dir < 8000):
						return self.get_global_value(memory_dir)
				else:
						return self.get_local_value(memory_dir)

		def get_local_value(self, memory_dir):
				if (memory_dir >= 8000 and memory_dir < 9000) or (memory_dir >= 11000 and memory_dir < 12000):
						return self.local_memory[0][memory_dir]['value']

				elif (memory_dir >= 9000 and memory_dir < 10000) or (memory_dir >= 12000 and memory_dir < 13000):
						return self.local_memory[1][memory_dir]['value']
														
				elif (memory_dir >= 10000 and memory_dir < 11000) or (memory_dir >= 13000 and memory_dir < 14000):
						return self.local_memory[2][memory_dir]['value']
														
				elif memory_dir >= 14000 and memory_dir < 15000:
						return self.local_memory[3][memory_dir]['value']


		def get_global_value(self, memory_dir):
				if int(memory_dir) >= 15000 and int(memory_dir) < 16000:
						return self.constant_memory[0][memory_dir]['value']
				elif int(memory_dir) >= 16000 and int(memory_dir) < 17000:
						return self.constant_memory[1][memory_dir]['value']
				elif int(memory_dir) >= 17000 and int(memory_dir) < 18000:
						return self.constant_memory[2][memory_dir]['value']
				elif int(memory_dir) >= 18000 and int(memory_dir) < 19000:
						return self.constant_memory[3][memory_dir]['value']
				elif (memory_dir >= 1000 and memory_dir < 2000) or (memory_dir >= 4000 and memory_dir < 5000):
						return self.global_memory[0][memory_dir]['value']
				elif memory_dir >= 2000 and memory_dir < 3000 or (memory_dir >= 5000 and memory_dir < 6000):
						return self.global_memory[1][memory_dir]['value']
				elif memory_dir >= 3000 and memory_dir < 4000 or (memory_dir >= 6000 and memory_dir < 7000):
						return self.global_memory[2][memory_dir]['value']
				elif memory_dir >= 7000 and memory_dir < 8000:
						return self.global_memory[3][memory_dir]['value']
				

		def get_memory(self,value):
				#ERROR CORREGIR INDENTATION
			list_keys = list(self.general_dir['global_var'].keys())
			for i in list_keys:
				if i != 'global_var_names':
						if self.general_dir['global_var'][i]['name'] == value and value != None:
							return self.general_dir['global_var'][i]['memory_dir']
							
		def set_value(self, memory_dir, value):
				if(memory_dir >= 8000 and memory_dir < 9000) or (memory_dir >= 11000 and memory_dir < 12000):
						self.local_memory[0][memory_dir] = {
								'value': value 
						}

				elif (memory_dir >= 9000 and memory_dir < 10000) or (memory_dir >= 12000 and memory_dir < 13000):
						self.local_memory[1][memory_dir] = {
								'value': value 
						}
																
				elif (memory_dir >= 10000 and memory_dir < 11000) or (memory_dir >= 13000 and memory_dir < 14000):
						self.local_memory[2][memory_dir] = {
								'value': value 
						}
												
				elif memory_dir >= 14000 and memory_dir < 15000:
						 self.local_memory[3][memory_dir] = {
								'value': value 
						}
				elif memory_dir >= 7000 and memory_dir < 8000:
					self.global_memory[3][memory_dir] = {
						'value': value
					}
				elif( memory_dir >= 1000 and memory_dir < 2000) or (memory_dir >= 4000 and memory_dir < 5000):
						self.global_memory[0][memory_dir] = {
								'value': value # 
						}
				elif (memory_dir >= 2000 and memory_dir < 3000) or (memory_dir >= 4000 and memory_dir < 5000):
						self.global_memory[1][memory_dir] = {
								'value': value # PENDIENTE
						}
				elif (memory_dir >= 3000 and memory_dir < 4000) or (memory_dir >= 4000 and memory_dir < 5000):
					self.global_memory[2][memory_dir] = {
						'value': value 
					}
				elif memory_dir >= 18000 and memory_dir < 19000:
					self.local_memory[3][memory_dir] = {
						'value': value 
					}
		 

		def fill_memories(self):
				self.separate_vars()
				self.fill_constant_memory()
				self.fill_global_memory()






