'''
 
Estructura diccionario:
cubo = {
  left: {
    operador:{
      right: value
    }
  }
}

'''
cubo_semantico = {
  'int':{
    '+':{
      'int':'int',
      'float': 'float',
      'char':'error',
      'bool':'error'
    },
    '-':{
      'int':'int',
      'float': 'float',
      'char':'error',
      'bool':'error'
    },
    '*':{
      'int':'int',
      'float': 'float',
      'char':'error',
      'bool':'error'
    },
    '/':{
      'int':'float',
      'float':'float',
      'char':'error',
      'bool':'error'
    },
    '>':{
      'int':'bool',
      'float':'bool',
      'char':'error',
      'bool':'error'
    },
    '<':{
      'int':'bool',
      'float':'bool',
      'char':'error',
      'bool':'error'
    },
    '<>':{
      'int': 'bool',
      'float':'error',
      'char': 'error',
      'bool': 'error'
    },
    '==': {
      'int': 'bool',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    'and': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    'or': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    '=': {
      'int': 'int',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
  },
  'float':{
    '+':{
      'int':'float',
      'float': 'float',
      'char':'error',
      'bool':'error'
    },
    '-':{
      'int':'float',
      'float': 'float',
      'char':'error',
      'bool':'error'
    },
    '*':{
      'int':'float',
      'float': 'float',
      'char':'error',
      'bool':'error'
    },
    '/':{
      'int':'float',
      'float':'float',
      'char':'error',
      'bool':'error'
    },
    '>':{
      'int':'bool',
      'float':'bool',
      'char':'error',
      'bool':'error'
    },
    '<':{
      'int':'bool',
      'float':'bool',
      'char':'error',
      'bool':'error'
    },
    '<>':{
      'int': 'error',
      'float':'bool',
      'char': 'error',
      'bool': 'error'
    },
    '==': {
      'int': 'error',
      'float': 'bool',
      'char': 'error',
      'bool': 'error'
    },
    'and': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    'or': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    '=': {
      'int': 'error',
      'float': 'float',
      'char': 'error',
      'bool': 'error'
    }, 
  },
 'char':{
    '+':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '-':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '*':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '/':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '>':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '>':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '<>':{
      'int': 'error',
      'float':'error',
      'char': 'bool',
      'bool': 'error'
    },
    '==': {
      'int': 'error',
      'float': 'error',
      'char': 'bool',
      'bool': 'error'
    },
    'and': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    'or': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    },
    '=': {
      'int': 'error',
      'float': 'error',
      'char': 'char',
      'bool': 'error'
    }, 
  },
   'bool':{
    '+':{
      'int':'error',
      'float': 'error',
      'char':'error',
      'bool':'error'
    },
    '-':{
      'int':'error',
      'float': 'error',
      'char':'error',
      'bool':'error'
    },
    '*':{
      'int':'error',
      'float': 'error',
      'char':'error',
      'bool':'error'
    },
    '/':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '>':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '>':{
      'int':'error',
      'float':'error',
      'char':'error',
      'bool':'error'
    },
    '<>':{
      'int': 'error',
      'float':'error',
      'char': 'error',
      'bool': 'bool'
    },
    '==': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'bool'
    },
    'and': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'bool'
    },
    'or': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'bool'
    },
    '=': {
      'int': 'error',
      'float': 'error',
      'char': 'error',
      'bool': 'error'
    }, 
  },
}