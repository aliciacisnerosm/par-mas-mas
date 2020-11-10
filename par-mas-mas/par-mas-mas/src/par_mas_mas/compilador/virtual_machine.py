from collections import deque
class VirtualMachine:
    def __init__(self, arr_quadruples, general_dir):
        self.memory = MemoryMap(arr_quadruples, general_dir)
        self.arr_quadruples = arr_quadruples
    # def generate_obj(self):
    #     if self.arr_quadruples == None or self.general_dir == None:
    #         return "error"
    #     #else :
    #         #print("este es el arr_quadruples",self.arr_quadruples)
    #         #print("este es el general_dir", self.general_dir)

    def process_quadruples(self):
      pointer = 0
      print(self.arr_quadruples[pointer][0])
      while(pointer<len(self.arr_quadruples)):
        if self.arr_quadruples[pointer][0]== '+':
            left_value=self.memory.get_value(self.arr_quadruples[pointer][1])
            right_value=self.memory.get_value(self.arr_quadruples[pointer][2])
            result = left_value + right_value
            self.memory.set_value(self.arr_quadruples[pointer][3], result)
            pointer+=1

        elif self.arr_quadruples[pointer][0]== '-':
            left_value=self.memory.get_value(self.arr_quadruples[pointer][1])
            right_value=self.memory.get_value(self.arr_quadruples[pointer][2])
            result = left_value - right_value
            self.memory.set_value(self.arr_quadruples[pointer][3], result)
            pointer+=1

        elif self.arr_quadruples[pointer][0]== '*':
            left_value=self.memory.get_value(self.arr_quadruples[pointer][1])
            right_value=self.memory.get_value(self.arr_quadruples[pointer][2])
            result = left_value * right_value
            self.memory.set_value(self.arr_quadruples[pointer][3], result)
            pointer+=1

        elif self.arr_quadruples[pointer][0]== '/':
            left_value=self.memory.get_value(self.arr_quadruples[pointer][1])
            right_value=self.memory.get_value(self.arr_quadruples[pointer][2])
            result = left_value /right_value
            self.memory.set_value(self.arr_quadruples[pointer][3], result)
            pointer+=1
        elif self.arr_quadruples[pointer][0]== 'write':
            result = self.memory.get_memory(self.arr_quadruples[pointer][3])
            direction = self.memory.get_memory(result)
            value=self.memory.get_value(direction)
            print("este es el resultado", value)
            pointer+=1
        else:
            pointer+=1

    def execute(self):
        self.memory.fill_memories()
        self.process_quadruples()



class MemoryMap:
    def __init__(self, arr_quadruples, general_dir):
        self.global_memory = [dict(), dict(), dict()]
        self.local_memory = [dict(), dict(), dict(), dict()]
        self.constant_memory = [dict(), dict(), dict()]
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
            print(self.global_memory)

    def fill_constant_memory(self):
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
            print(self.constant_memory)

    def get_value(self, memory_dir):
        print(memory_dir)
        if int(memory_dir) >= 15000 and int(memory_dir) < 16000:
            return self.constant_memory[0][memory_dir]['value']
        elif int(memory_dir) >= 16000 and int(memory_dir) < 17000:
            return self.constant_memory[1][memory_dir]['value']
        elif int(memory_dir) >= 17000 and int(memory_dir) < 18000:
            return self.constant_memory[2][memory_dir]['value']
        elif int(memory_dir) >= 1000 and int(memory_dir)< 2000:
            return self.global_memory[0]['value']
        elif int(memory_dir) >= 2000 and int(memory_dir) < 3000:
            return self.global_memory[1]['value']
        elif int(memory_dir) >= 3000 and int(memory_dir) < 4000:
            return self.global_memory[2]['value']

    def get_memory(self,value):
      print(value)
        #ERROR CORREGIR INDENTATION
      list_keys = list(self.general_dir['global_var'].keys())
      for i in list_keys:
        if i != 'global_var_names':
            if self.general_dir['global_var'][i]['name'] == value and value != None:
              return self.general_dir['global_var'][i]['memory_dir']
              print(self.general_dir['global_var'][i]['memory_dir'])

    def set_value(self, memory_dir, value):
        print(memory_dir)
        if memory_dir >= 15000 and memory_dir < 16000:
            self.constant_memory[0][memory_dir]['value'] = value
        elif memory_dir >= 16000 and memory_dir < 17000:
            self.constant_memory[1][memory_dir]['value'] = value
        elif memory_dir >= 17000 and memory_dir < 18000:
            self.constant_memory[2][memory_dir]['value'] = value
        elif memory_dir >= 1000 and memory_dir < 2000:
            self.global_memory[0]['value'] = value
        elif memory_dir >= 2000 and memory_dir < 3000:
            self.global_memory[1]['value'] = value
        elif memory_dir >= 3000 and memory_dir < 4000:
            self.global_memory[2]['value'] = value

    def fill_memories(self):
        self.separate_vars()
        self.fill_constant_memory()
        self.fill_global_memory()






