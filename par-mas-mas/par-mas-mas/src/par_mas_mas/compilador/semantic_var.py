'''

cada vez que se haga add 
  primero se 

nuevo  = {
  a: {
    alsdañls: true
  }
}

s = {
  variables globales: se((nombre, type, valor), )
  funciones : set((nombre, type), nuevo, nuevo2)
  
  funcion1: {
    
  }

    # variables globales 
  #funciones: {
    #set con  nombre de variable, type 
    #key: {
      #variables 
   # }
  # }
}
'''
_global = {
  'global_var_names': set(),
  'functions': {
    'func_names': set('main'), 
    'main': {
    'return_type': 'void',
      'variables': {
        'var_name': set(),
        # 'name_var': {
        #   'kind':
        #   'return_type':
        #   'value':
        # }
      }
    }
  },
  'global_var': {
    'var_name': set(),
    # 'name_var': {
    #   'kind':
    #   'return_type':
    #   'value':
    #   'scope':
    # }
  }
}

def unique_function_names(name, return_type):

  if name in _global.functions.func_names:
    return "error"
  else:
    _global['functions']['func_names'].add(name)
    _global['functions']['func_names'][name] = {
      'return_type': return_type,
      'variables': {
        var_names: set()
      }
    }

def add_variable(return_type, scope, kind, name, value):
  if scope == 'global':
    if name not in _global.global_var_names:
      _global['global_var_names'].add(name)
      _global['global_var'][name] = {
        'return_type': return_type,
        'scope': scope,
        'kind': kind,
        'value': value 
      }
    else: 
      return "Error: Variable ya declarada"
  else: 
    if name not in _global['functions'][name]['variables']['name_var']:
      _global['functions'][scope]['variables']['name_var'].add(name)
      _global['functions'][scope]['variables'][name] = {
        'return_type': return_type,
        'scope': scope,
        'kind': kind,
        'value': value 
      }
    else:
      return "Error: Variable ya declarada"
  return _global
  
