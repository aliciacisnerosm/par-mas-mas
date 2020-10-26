import sys
import re

# from par_mas_mas.compilador.ply.lex import lex
# from par_mas_mas.compilador.ply.yacc import yacc

import par_mas_mas.compilador.ply.lex as lex
import par_mas_mas.compilador.ply.yacc as yacc
import par_mas_mas.compilador.semantic_var as semantic_var
from par_mas_mas.compilador.semantic_var import *
from par_mas_mas.compilador.quadruples import *
from par_mas_mas.compilador.memory import *
from par_mas_mas.compilador.types import *
from collections import deque
import os

error = False
semantic_var = None
memory = None
scope = 'global'
var_type = None # si tenemos tiempo, quitar global
arr_quadruples = []
cube = SemanticCube()

stack_operators = deque()
stack_operands = deque()
stack_type = deque()


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
'COMMA', 'EQUALS', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'GREATER_THAN', 'LESS_THAN', 'DIFFERENT', 'EQUAL', 'GREATER_EQUAL', 'LESS_EQUAL','STR', 
'CTE_I','CTE_CHAR', 'MORE', 'DOT',
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
t_EQUAL = r'\=='
t_GREATER_EQUAL = r'\>='
t_LESS_EQUAL = r'\<='
t_ignore = ' \t'
t_MORE = r'\&'
t_DOT = r'\.'

#EXPRESIONES REGULARES COMPLEJAS
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_CTE_I(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_CTE_CHAR(t):
	r'[a-zA-Z]'
	t.value=str(t.value)
	return t


def t_error(t):
	print("Illegal characters", t)
	t.lexer.skip(1)

def t_newline(t):
		r'\n+'
		t.lexer.lineno += t.value.count("\n")

lexer = lex.lex()
start = 'program'

def p_cte_f(p):
	'''
	cte_f : CTE_I DOT CTE_I
	
	'''
	if p[1] == None:
		global error
		error = True
	
	float_var = str(p[1]) + p[2] + str(p[3])
	p[0] = float(float_var)

def p_program(p):
	'''
	program : PROGRAM ID punto_program COLON main
					| PROGRAM ID punto_program COLON variables main
					| PROGRAM ID punto_program COLON variables funciones main
					| PROGRAM ID punto_program COLON funciones main  
	''' 

def p_punto_program(p):
	'''
	punto_program : 
	'''
	global semantic_var, memory, quadruples
	semantic_var = Semantics()
	memory = Memory()

	global_var = {
		'global_var_names': set(),
	}

	semantic_var._global['global_var'] = global_var

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
	variables : VAR punto_variables_1 SEMICOLON
						| VAR punto_variables_1 variables_aux SEMICOLON
	'''

def p_punto_variables_1(p):
	'''
	punto_variables_1 :
	'''


def p_variables_aux(p):
	'''
	variables_aux : tipo COLON declaracion_inicial
								| tipo COLON declaracion_inicial MORE variables_aux
	'''

def p_tipo(p):
	'''
	tipo : INT
			| FLOAT
			| CHAR
	'''
	p[0] = p[1]

	global var_type
	if p[1] == 'int':
		var_type = 1
	elif p[1] == 'float':
		var_type = 2
	elif p[1] == 'char':
		var_type = 3
	

def p_declaracion_inicial(p):
	'''
	declaracion_inicial : dec_varaux punto_dec_var_1 COMMA declaracion_inicial
											| dec_varaux punto_dec_var_1
	'''
	
def p_punto_dec_var_1(p):
	'''
	punto_dec_var_1 :
	'''
	global semantic_var, scope, var_type
	
	#TO DO AVANCE 4: Memory_dir ya asignada al declarar variables
	memory_dir_aux = memory.get_value_memory(var_type, scope, False)
	semantic_var.declare_variables(var_type, scope, 'variable_name', p[-1], None, memory_dir_aux, 0)
	
def p_dec_varaux(p):
	'''
	dec_varaux : ID 
							| ID LEFT_BR CTE_I RIGHT_BR 
							| ID LEFT_BR CTE_I RIGHT_BR LEFT_BR CTE_I RIGHT_BR
	'''
	p[0] = p[1]



#todo: agregar punto para las dimensiones (:
def p_punto_dec_varaux_1(p):
	'''
	punto_dec_varaux_1 :

	'''

def p_dec_var(p):
	'''
	dec_var : dec_varaux COMMA dec_var
					| dec_varaux
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

def p_exp_or(p):
	'''
		exp_or : t_exp punto_pop_or t_exp_or_aux
					| t_exp punto_pop_or
	'''
def p_punto_pop_or(p):
	'''
		punto_pop_or :
	
	'''
	global stack_operators, arr_quadruples, stack_operands, semantic_var
	
	if len(stack_operators) != 0:
		top = stack_operators.pop()

		if top == 'or':
			op1 = stack_operands.pop() # memory dir
			op2 = stack_operands.pop()

			aux_1 = semantic_var.get_value_variable(scope,op1) # value
			aux_2 = semantic_var.get_value_variable(scope,op2)
			
			#todo: checar tipos
			if semantic_var.get_return_type_variables(scope,op1) == 4 and semantic_var.get_return_type_variables(scope, op2) == 4:
				# 1 memory dir : scope, 'bool', temp
				dir_memory_aux = memory.get_value_memory(4, scope, True)
				value = False

				# 2 hacer la operacion para sacar value
				# true or false value = true
				value = aux_2 or aux_1

				# 3 agregar esa direccion de memoria a _global variables temp 
				semantic_var.add_variables(4, scope, 'temp_variable', None, value, dir_memory_aux, 0)
				
				# 4 crear cuadruplo = (or false true memory_dir)

				q = Quadruple(top, op2, op1, dir_memory_aux)
				arr_quadruples.append(q.get_quadruple())
			else:
				print("error en or")
		else:
			stack_operators.append(top)


def p_t_exp_or_aux(p):
	'''
	t_exp_or_aux : OR punto_push_or exp_or
	'''

def p_punto_push_or(p):
	'''
	punto_push_or :
	'''
	global stack_operators
	stack_operators.append('OR')


def p_t_exp(p):
	'''
	t_exp : g_exp pop_and t_exp_aux
				| g_exp pop_and

	'''
def p_pop_and(p):
	'''
	pop_and :
	
	'''
	global stack_operators, arr_quadruples, stack_operands
	if len(stack_operators) != 0:
		top = stack_operators.pop()

		if top == 'and':
			op1 = stack_operands.pop() # memory dir
			op2 = stack_operands.pop()

			aux_1 = semantic_var.get_value_variable(scope,op1) # value
			aux_2 = semantic_var.get_value_variable(scope,op2)
			
			#todo: checar tipos
			if semantic_var.get_return_type_variables(scope, op1) == 4 and semantic_var.get_return_type_variables(scope, op2) == 4:
				# 1 memory dir : scope, 'bool', temp
				dir_memory_aux = memory.get_value_memory(4, scope, True)
				value = False

				# 2 hacer la operacion para sacar value
				# true and false value = true
				value = aux_2 and aux_1

				# 3 agregar esa direccion de memoria a _global variables temp 
				semantic_var.add_variables(4, scope, 'temp_variable', None, value, dir_memory_aux, 0)
				
				# 4 crear cuadruplo = (and false true memory_dir)

				q = Quadruple(top, op2, op1, dir_memory_aux)
				arr_quadruples.append(q.get_quadruple())
			else:
				print("error en and")
		else:
			stack_operators.append(top)

def p_t_exp_aux(p):
	'''
	t_exp_aux : AND punto_push_and t_exp

	'''
def p_punto_push_and(p):
	'''
	punto_push_and :
	'''
	global stack_operators
	stack_operators.append('and')
	
def p_g_exp(p):
	'''
		g_exp : m_exp
					| m_exp relacionales punto_relacionales m_exp punto_pop_relacional
	'''
def p_punto_relacionales(p):
	'''
	punto_relacionales :
	'''
	global stack_operators
	if p[-1] != None:
		stack_operators.append(p[-1])
	

def p_punto_pop_relacional(p):
	'''
	punto_pop_relacional :
	'''
	global stack_operators, arr_quadruples
	
	if len(stack_operators) != 0:
		top = stack_operators.pop()

		op1 = stack_operands.pop()
		op2 = stack_operands.pop()

		aux_1 = semantic_var.get_value_variable(scope,op1) # value
		aux_2 = semantic_var.get_value_variable(scope,op2)


		dir_memory_aux = memory.get_value_memory(4, scope, True)
		value = False
		if (top is '=='):
			value = aux_2 == aux_1
		elif top is '>':
			value = aux_2 > aux_1		
		elif top is '<':
			value = aux_2 < aux_1
		elif top is '<=':
			value = aux_2 <= aux_1
		elif top is '>=':
			value = aux_2 >= aux_1
		elif top is '<>':
			value = aux_2 != aux_1
		else:
			value = None
			
		
		semantic_var.add_variables(4, scope, 'temp_variable', None,  value, dir_memory_aux, 0)
			

		q = Quadruple(top, op2, op1, dir_memory_aux)
		arr_quadruples.append(q.get_quadruple())
		
def p_m_exp(p):
	'''
	m_exp : termino punto_mexp_pop
				| termino punto_mexp_pop m_exp_aux
	'''
	global stack_operands, stack_operators
	p[0] = p[1]

def p_punto_mexp_pop(p):
	'''
	punto_mexp_pop :
	'''
	global stack_operators, arr_quadruples, cube

	if len(stack_operators) != 0:
		top = stack_operators.pop()

		if top == '+' or top == '-':
			value = None
			value_type = None
			
			op1 = stack_operands.pop()
			op2 = stack_operands.pop()
			
			aux_1 = semantic_var.get_value_variable(scope, op1) # value
			aux_2 = semantic_var.get_value_variable(scope,op2)

			type_aux_1 = semantic_var.get_return_type_variables(scope,op1)
			type_aux_2 = semantic_var.get_return_type_variables(scope, op2)
			
			value_type = cube.get_type(type_aux_1, type_aux_2, top)

			if value_type == 5:
				#todo: error
				print("error en tipo de suma & resta")
			else:
				dir_memory_aux = memory.get_value_memory(value_type, scope, True)
			
				if top == '+':
					value = aux_2 + aux_1
				else:
					value = aux_2 - aux_1
				
				semantic_var.add_variables(value_type, scope, 'variable', None, value, dir_memory_aux, 0)

				q = Quadruple(top, op2, op1, dir_memory_aux )
				arr_quadruples.append(q.get_quadruple())

		else:
			stack_operators.append(top)


def p_m_exp_aux(p):
	'''
	m_exp_aux : PLUS punto_termino_push m_exp
						| MINUS punto_termino_push m_exp

	'''
def p_punto_termino_push(p):
	'''
	punto_termino_push :
	'''
	global stack_operators
	if p[-1] != None:
		stack_operators.append(p[-1])
		print(p[-1])


def p_termino(p):
	'''
	termino : factor punto_termino_pop
					| factor punto_termino_pop termino_aux
	'''   
	p[0] = p[1]
	global stack_operators
	if p[-1] != None:
		stack_operators.append(p[-1])
		print(p[-1])

def p_punto_termino_pop(p):
	'''
	punto_termino_pop :

	'''
	global stack_operators, arr_quadruples, cube
	top = None	
	if len(stack_operators) != 0:
		top = stack_operators.pop()


	if top == '*' or top == '/':
		value = None
		value_type = None
		
		op1 = stack_operands.pop()
		op2 = stack_operands.pop()
		
		aux_1 = semantic_var.get_value_variable(scope,op1) # value
		aux_2 = semantic_var.get_value_variable(scope,op2)
		print(aux_1, aux_2)
		type_aux_1 = semantic_var.get_return_type_variables(scope,op1)
		type_aux_2 = semantic_var.get_return_type_variables(scope, op2)
		
		value_type = cube.get_type(type_aux_1, type_aux_2, top)

		if value_type == 5:
			#todo: error
			print("error tipo de * / ")
		else:
			dir_memory_aux = memory.get_value_memory(value_type, scope, True)
		
			if top == '*':
				value = aux_2 * aux_1
			else:
				value = aux_2 / aux_1
			
			semantic_var.add_variables(value_type, scope, 'variable', None, value, dir_memory_aux, 0)

			q = Quadruple(top, op2, op1, dir_memory_aux )
			arr_quadruples.append(q.get_quadruple())

	else:
		stack_operators.append(top)

def p_termino_aux(p):
  '''
  termino_aux : MULTIPLY termino
              | DIVIDE termino
  '''

def p_factor(p):
	'''
	factor : cte
					| ID LEFT_PAR dec_var RIGHT_PAR
					| ID LEFT_PAR RIGHT_PAR
					| LEFT_PAR exp_or RIGHT_PAR
	'''
	p[0] = p[1]


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
	asignacion : dec_varaux punto_asignacion_var EQUALS punto_igual m_exp punto_asignacion
	'''
def p_punto_asignacion_var(p):
	'''
	punto_asignacion_var : 
	'''
	global stack_operands
	var_id = semantic_var.get_memory_dir(p[-1], scope)
	stack_operands.append(var_id)
	p[0] = var_id

def p_punto_igual(p):
	'''
	punto_igual :
	'''
	global stack_operators
	stack_operators.append('=')
	
def p_punto_asignacion(p):
	'''
	punto_asignacion : 

	'''
	global stack_operators, stack_operands, arr_quadruples, scope
	if p[-5] not in semantic_var.get_variables_sets(scope):
		print("error en punto de asignacion")
	else:
		elem = stack_operands.pop()
		izq= stack_operands.pop()
		op = stack_operators.pop()
		
		value_aux = semantic_var.get_value_variable(scope, izq)
		## checar el tipo de variable antes de asignar
		semantic_var.set_value(scope, elem, value_aux)
		
		q = Quadruple(op, izq, None, elem)
		arr_quadruples.append(q.get_quadruple())

def p_llamada(p):
	'''
		llamada : VD ID LEFT_PAR RIGHT_PAR
						| VD ID LEFT_PAR dec_var RIGHT_PAR
	'''

def p_retorno(p):
	'''
		retorno : RETURN LEFT_PAR m_exp RIGHT_PAR
	'''

def p_punto_read_stack(p):
	'''
	punto_read_stack : 
	'''
	global stack_operators
	stack_operators.append("read")
	


def p_lectura(p):
	'''
	lectura : READ LEFT_PAR lectura_var RIGHT_PAR
	'''

def p_lectura_var(p):
	'''
	lectura_var : punto_read_stack dec_varaux punto_push_dec_var punto_add_read_operand COMMA lectura_var
					| punto_read_stack dec_varaux punto_push_dec_var punto_add_read_operand
	'''
	p[0] = p[1]

def p_punto_push_dec_var(p):
	'''
	punto_push_dec_var :
	'''
	global stack_operands, stack_operators

	var_id = semantic_var.get_memory_dir(p[-1], scope)
	stack_operands.append(var_id)
	p[0] = var_id
	


def p_punto_add_read_operand(p):
	'''
		punto_add_read_operand : 
	'''
	global arr_quadruples
	global stack_operators
	global stack_operands

	if p[-2] not in semantic_var.get_variables_sets(scope):
		print(p[-2])
		print("error punto de read")
	else:
		q = Quadruple(stack_operators.pop(), None, None, p[-1])
		arr_quadruples.append(q.get_quadruple())

#TO DO: ARREGLAR ESCRITURA MULTIPLES STRINGS
def p_escritura(p):
	'''
	escritura : WRITE LEFT_PAR escritura_aux RIGHT_PAR
	'''

def p_escritura_aux(p):
	'''
	escritura_aux : punto_write_stack STR punto_escritura_push punto_add_write_operand
								| punto_write_stack m_exp punto_escritura_push punto_add_write_operand
								| punto_write_stack STR punto_escritura_push punto_add_write_operand COMMA escritura_aux 
								| punto_write_stack m_exp punto_escritura_push punto_add_write_operand COMMA escritura_aux
	'''
def p_punto_escritura_push(p):
	'''
	punto_escritura_push : 

	'''
	global stack_operands, semantic_var, stack_operators
	if type(p[-1]) == str:
		stack_operands.append(p[-1])
	else:
		var_id = semantic_var.get_memory_dir(p[-1], scope)
		stack_operands.append(var_id)
		
def p_punto_write_stack(p):
	'''
	punto_write_stack :
	'''
	global stack_operators
	stack_operators.append("write")

def p_punto_add_write_operand(p):
	'''
	punto_add_write_operand : 
	'''
	global arr_quadruples
	global stack_operators
	global stack_operands
	global semantic_var
	
	# checar q este ok 

	elemento = stack_operands.pop()
	q = Quadruple(stack_operators.pop(), None, None, elemento)
	arr_quadruples.append(q.get_quadruple())

def p_decision(p):
	'''
	decision : IF LEFT_PAR exp_or RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL 
						| IF LEFT_PAR exp_or RIGHT_PAR THEN LEFT_CURL estatutos RIGHT_CURL ELSE LEFT_CURL estatutos RIGHT_CURL
	'''

def p_repeticion(p):
	'''
	repeticion : condicional
							| no_condicional
	'''

def p_no_condicional(p):
	'''
	no_condicional : FOR LEFT_PAR dec_varaux EQUALS m_exp TO m_exp RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL
	'''
		
def p_condicional(p):
	'''
	condicional : WHILE LEFT_PAR exp_or RIGHT_PAR DO LEFT_CURL estatutos RIGHT_CURL
	'''

def p_cte(p):
	'''
	cte : ID factor_push_operand
			| CTE_I factor_int_push
			| cte_f factor_float_push
			| CTE_CHAR factor_char_push
	'''
	p[0] = p[1]
	
def p_factor_push_operand(p):
	'''
	factor_push_operand :
	'''
	global stack_operators
	if p[-1] not in semantic_var.get_variables_sets(scope):
		print("error en factor")
	else:
    # TO DO: CHECAR TIPOS PARA MANIPULAR MEMORIA Y TEMPORALES
		global stack_type, stack_operands
		memory_dir_p1 = semantic_var.get_memory_dir(p[-1], scope)
		type_aux_p1 = semantic_var.get_return_type_variables(scope,memory_dir_p1)

		stack_operands.append(memory_dir_p1)
		stack_type.append(type_aux_p1)

def p_factor_float_push(p):
	'''
	factor_float_push :
	'''
	global stack_operands, stack_type
	if p[-1] != None:
		memory_dir_p1 = memory.get_value_memory(2, scope, True)
		semantic_var.add_variables(2, scope, 'temp_variable', None, p[-1], memory_dir_p1, 0)
		stack_operands.append(memory_dir_p1)
		stack_type.append(2)

def p_factor_int_push(p):
	'''
	factor_int_push :
	'''
	global stack_operands, scope
	if p[-1] != None:
		memory_dir_p1 = memory.get_value_memory(1, scope, True)
		semantic_var.add_variables(1, scope, 'temp_variable', None, p[-1], memory_dir_p1, 0)
		stack_operands.append(memory_dir_p1)
		stack_type.append(1)

def p_factor_char_push(p):
	'''
	factor_char_push :
	'''
	global stack_operands, stack_type
	if p[-1] != None:
		memory_dir_p1 = memory.get_value_memory(3, scope, True)
		semantic_var.add_variables(3, scope, 'temp_variable', None, p[-1], memory_dir_p1, 0)
		stack_operands.append(memory_dir_p1)
		stack_type.append(3)

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


def parser():
	try:
		arch_name = 'prueba-1.txt'
		this_folder = os.path.dirname(os.path.abspath(__file__))
		my_file = os.path.join(this_folder, arch_name)
		print(my_file)
		arch = open(my_file,'r')
		print("Nombre de archivo " + arch_name)
		archivo = arch.read()
		arch.close()
		yacc.parse(archivo)

		if error: 
			return "hay errores de sintaxis"
		else:
			global arr_quadruples, stack_operands
			print(arr_quadruples, stack_operands, len(arr_quadruples))
			print(semantic_var._global)
			return "apropiado"


	except EOFError:
		print(EOFError)

if __name__ == '__main__':
	parser()