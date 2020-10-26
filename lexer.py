import sys
from ply import lex
from ply import yacc

error = False
reserved = {
  'if': 'IF',
  'else': 'ELSE',
  'program': 'PROGRAM',
  'main': 'MAIN',
  'var': 'VAR',
  'int': 'INT',
  'char':'CHAR',
  'float': 'FLOAT',
  'write': 'WRITE',
  'while': 'WHILE',
  'do': 'DO',
  'for': 'FOR',
  'then': 'THEN',
  'read': 'READ',
  'vd': 'VD',
  'and': 'AND',
  'or': 'OR',
  'void': 'VOID',
  'func': 'FUNC',
  'to': 'TO',
  'return': 'RETURN'
}


tokens = [ 'ID', 'COLON','SEMICOLON', 'LEFT_PAR', 'RIGHT_PAR', 'LEFT_BR', 'RIGHT_BR', 'LEFT_CURL', 'RIGHT_CURL',
'COMMA', 'EQUALS', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'GREATER_THAN', 'LESS_THAN', 'DIFFERENT', 'EQUAL', 'STR', 
'CTE_I','CTE_F', 'MORE'
] + list(reserved.values())

#EXPRESIONES REGULARES SIMPLES
t_STR = r'\".*\"'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'
t_LEFT_BR = r'\['
t_RIGHT_BR = r'\]'
t_LEFT_CURL = r'\{'
t_RIGHT_CURL = r'\}'
t_COMMA = r'\,'
t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_DIFFERENT = r'\<>'
t_GREATER_EQUAL = r'\>='
t_LESS_EQUAL = r'\<='
t_EQUAL = r'\=='
t_ignore = ' \t'
t_MORE = r'\&'

#EXPRESIONES REGULARES COMPLEJAS
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')
  return t

def t_CTE_I(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_CTE_F(t):
  r'[-+]?(\d*\.\d*)'
  t.value = float(t.value)
  return t

def t_error(t):
  print("Illegal characters", t)
  t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()
start = 'program'

def p_program(p):
  '''
  program : PROGRAM ID COLON main
          | PROGRAM ID COLON variables main
          | PROGRAM ID COLON variables funciones main
          | PROGRAM ID COLON funciones main  
  ''' 


def p_main(p):
  '''
  main : MAIN LEFT_PAR RIGHT_PAR LEFT_CURL main_aux RIGHT_CURL

  '''   

def p_main_aux(p):
  '''
  main_aux : estatutos_main_multiple
           | empty
  '''      

def p_variables(p):
  '''
  variables : VAR SEMICOLON
            | VAR variables_aux SEMICOLON
  '''

def p_variables_aux(p):
  '''
  variables_aux : tipo COLON dec_var
                | tipo COLON dec_var MORE variables_aux
  '''

def p_tipo(p):
  '''
  tipo : INT
      | FLOAT
      | CHAR
  '''

def p_dec_var(p):
  '''
  dec_var : dec_varaux COMMA dec_var
          | dec_varaux
  '''

def p_dec_varaux(p):
  '''
  dec_varaux : ID
              | ID LEFT_BR CTE_I RIGHT_BR
              | ID LEFT_BR CTE_I RIGHT_BR LEFT_BR CTE_I RIGHT_BR
  '''
	
def p_funciones(p):
  '''
  funciones : funciones_aux
            | funciones_aux funciones
  
  '''

def p_funciones_aux(p):
  '''
    funciones_aux : tipo FUNC ID LEFT_PAR parametros RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL
             | tipo FUNC ID LEFT_PAR RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL
             | VOID FUNC ID LEFT_PAR RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL
             | VOID FUNC ID LEFT_PAR parametros RIGHT_PAR LEFT_CURL variables estatutos RIGHT_CURL
  '''

def p_parametros(p):
  '''
  parametros : dec_var_param COMMA parametros
              | dec_var_param

  '''

def p_dec_var_param(p): 
	'''
	dec_var_param : tipo ID
	'''


def p_expresion(p):
  '''
  expresion : exp
              | exp relacionales expresion
							| exp logicos expresion
              | LEFT_PAR expresion RIGHT_PAR 
              | LEFT_PAR expresion RIGHT_PAR relacionales expresion
              | LEFT_PAR expresion RIGHT_PAR logicos expresion

  '''

def p_logicos(p):
  '''
  logicos : AND 
          | OR
  ''' 


def p_relacionales(p):
  '''
  relacionales : LESS_THAN
                  | GREATER_THAN
                  | DIFFERENT
                  | EQUAL
                  | GREATER_EQUAL 
                  | LESS_EQUAL
  '''

def p_estatutos(p):
  '''
  estatutos : estatutos_main_aux 
            | retorno SEMICOLON 

  '''

def p_estatutos_main(p):
  '''
  estatutos_main : asignacion SEMICOLON
                  | llamada SEMICOLON
                  | lectura SEMICOLON
                  | escritura SEMICOLON
                  | decision SEMICOLON
                  | repeticion SEMICOLON
  ''' 
  
def p_estatutos_main_multiple(p):
  '''
  estatutos_main_multiple : estatutos_main estatutos_main_multiple
                    | estatutos_main
  '''

def p_estatutos_main_aux(p):
  '''
  estatutos_main_aux : estatutos_main estatutos
                      | estatutos_main

  '''

def p_asignacion(p):
  '''
  asignacion : dec_varaux EQUALS exp
  '''


def p_exp(p):
  '''
  exp : termino exp_aux 
      | termino
  '''

def p_exp_aux(p):
  '''
  exp_aux : PLUS exp
          | MINUS exp
  '''

def p_termino(p):
  '''
  termino : factor
          | factor termino_aux
  '''   

def p_termino_aux(p):
  '''
  termino_aux : MULTIPLY termino
              | DIVIDE termino
  '''

def p_factor(p):
  '''
  factor : cte
          | LEFT_PAR exp RIGHT_PAR
          | ID LEFT_PAR dec_var RIGHT_PAR
          | ID LEFT_PAR RIGHT_PAR
  '''

def p_llamada(p):
  '''
    llamada : VD ID LEFT_PAR RIGHT_PAR
            | VD ID LEFT_PAR dec_var RIGHT_PAR
  '''

def p_retorno(p):
  '''
    retorno : RETURN LEFT_PAR exp RIGHT_PAR
  '''

def p_lectura(p):
  '''
  lectura : READ LEFT_PAR dec_var RIGHT_PAR
  '''

def p_escritura(p):
  '''
  escritura : WRITE LEFT_PAR escritura_aux RIGHT_PAR
  '''

def p_escritura_aux(p):
  '''
  escritura_aux : STR
                | exp
                | STR COMMA escritura_aux
                | exp COMMA escritura_aux
  '''

def p_decision(p):
  '''
  decision : IF LEFT_PAR expresion RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL 
            | IF LEFT_PAR expresion RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL ELSE LEFT_CURL estatutos RIGHT_CURL
  '''

def p_repeticion(p):
  '''
  repeticion : condicional
              | no_condicional
  '''

def p_no_condicional(p):
	'''
  no_condicional : FOR LEFT_PAR dec_varaux EQUALS exp TO exp RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL
  '''
    
def p_condicional(p):
  '''
  condicional : WHILE LEFT_PAR expresion RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL
  '''
def p_cte(p):
  '''
  cte : ID 
      | CTE_I
      | CTE_F 
  '''
def p_error(p): 
  global error
  error = True
  print("ERROR {}".format(p))

def p_empty(p):
  '''
  empty : 
  '''
  p[0] = None

parser = yacc.yacc()


if __name__ == '__main__':
  try:
    arch_name = 'prueba-1.txt'
    arch = open(arch_name,'r')
    print("Nombre de archivo " + arch_name)
    archivo = arch.read()
    arch.close()
    yacc.parse(archivo)

    if error: 
      print("hay errores de sintaxis")
    else:
      print("apropiado")  


  except EOFError:
    print(EOFError)