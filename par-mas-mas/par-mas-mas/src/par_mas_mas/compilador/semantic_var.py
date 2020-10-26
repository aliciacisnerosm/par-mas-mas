class Semantics:
	def __init__(self):
		self._global = {
			'functions': {
				'func_names': set(), 
				'main': {
				'return_type': 'void',
					'variables': {
						'var_name': set(),
					},
				}
			},
	}
		

	def unique_function_names(self, name, return_type):
		if name in self._global.functions.func_names:
			return "error"
		else:
			self._global['functions']['func_names'].add(name)
			self._global['functions']['func_names'][name] = {
				'return_type': return_type,
				'variables': {
					'var_names': set()
				}
			}
	#declara variables 
	def declare_variables(self, return_type, scope, kind, name, value, memory_dir, dimension):
		if scope == 'global':
			if name not in self._global['global_var']['global_var_names']:
				self._global['global_var']['global_var_names'].add(name)
				self._global['global_var'][memory_dir] = {
					'name': name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension
				}

				return ("exitoso", name, return_type)
			else: 
				return ("Error: Variable ya declarada", name, return_type)
		else: 
			if name not in self._global['functions'][scope]['variables']['name_var']:
				self._global['functions'][scope]['variables']['name_var'].add(name)
				self._global['functions'][scope]['variables'][memory_dir] = {
					'name': name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension

				}
				return ("exitoso", name, return_type)
			else:
				return ("Error: Variable ya declarada", name, return_type)
	
	def get_memory_dir(self, name, scope):
		if scope == "global":
			list_keys = list(self._global['global_var'].keys())
			for i in list_keys:
				if i != 'global_var_names':
					if self._global['global_var'][i]['name'] == name and name != None:
						return self._global['global_var'][i]['memory_dir']
		else:
			list_keys = list(self._global['functions'][scope]['variables'].keys())
			for i in list_keys:
				if i != 'name_var':
					if self._global['functions'][scope]['variables'][i]['name'] == name and name != None:
						return self._global['functions'][scope]['variables'][i]['memory_dir']

	# agrega variables temporales
	def add_variables(self, return_type, scope, kind, name, value, memory_dir, dimension):
		if scope == 'global':
			self._global['global_var'][memory_dir] = {
					'name':name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension
				}
		else:
			self._global['functions'][scope]['variables'][memory_dir] = {
					'name': name,
					'return_type': return_type,
					'scope': scope,
					'kind': kind,
					'value': value,
					'memory_dir': memory_dir,
					'dimension': dimension
				}

	def get_variables_sets(self, scope):
		if scope == "global":
			return self._global['global_var']['global_var_names']
		else:
			return self._global['functions'][scope]['variables']['name_var']
	
	def get_return_type_variables(self, scope, memory_dir):
		if scope == "global":
			return self._global['global_var'][memory_dir]['return_type']

		return self._global['functions'][scope]['variables'][memory_dir]['return_type']

	def get_memory_dir_variable(self, scope, memory_dir):
		if scope == "global":
			return self._global['global_var'][memory_dir]['memory_dir']
		
		return self._global['functions'][scope]['variables'][memory_dir]['memory_dir']
	
	def get_name_variable(self, memory_dir, scope):
		print(memory_dir, scope, self._global)
		if scope == "global":
			return self._global['global_var'][memory_dir]['name']

		return self._global['functions'][scope]['variables'][memory_dir]['name']

	def get_value_variable(self, scope, memory_dir):
		print(scope, memory_dir)
		if scope == "global":
			return self._global['global_var'][memory_dir]['value']

		return self._global['functions'][scope]['variables'][memory_dir]['value']
	
	def set_value(self, scope, memory_dir, value):
		if scope == "global":
			self._global['global_var'][memory_dir]['value'] = value
		else:
			self._global['functions'][scope]['variables'][memory_dir]['value'] = value

	def add_variable_name(self, scope, memory_dir, name):
		if scope == "global":
			 self._global['global_var'][memory_dir]['name'] = name

		self._global['functions'][scope]['variables'][memory_dir]['name'] = name