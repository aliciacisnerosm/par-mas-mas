
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND CHAR COLON COMMA CTE_CHAR CTE_I DIFFERENT DIVIDE DO DOT ELSE EQUAL EQUALS FLOAT FOR FUNC GREATER_EQUAL GREATER_THAN ID IF INT LEFT_BR LEFT_CURL LEFT_PAR LESS_EQUAL LESS_THAN MAIN MINUS MORE MULTIPLY OR PLUS PROGRAM READ RETURN RIGHT_BR RIGHT_CURL RIGHT_PAR SEMICOLON STR THEN TO VAR VD VOID WHILE WRITE\n\tcte_f : CTE_I DOT CTE_I\n\t\n\t\n\tprogram : PROGRAM ID punto_program COLON main\n\t\t\t\t\t| PROGRAM ID punto_program COLON variables main\n\t\t\t\t\t| PROGRAM ID punto_program COLON variables funciones main\n\t\t\t\t\t| PROGRAM ID punto_program COLON funciones main  \n\t\n\tpunto_program : \n\t\n\tmain : MAIN LEFT_PAR RIGHT_PAR LEFT_CURL main_aux RIGHT_CURL\n\n\t\n\tmain_aux : estatutos_main_multiple\n\t\t\t\t\t | empty\n\t\n\tvariables : VAR punto_variables_1 SEMICOLON\n\t\t\t\t\t\t| VAR punto_variables_1 variables_aux SEMICOLON\n\t\n\tpunto_variables_1 :\n\t\n\tvariables_aux : tipo COLON declaracion_inicial\n\t\t\t\t\t\t\t\t| tipo COLON declaracion_inicial MORE variables_aux\n\t\n\ttipo : INT\n\t\t\t| FLOAT\n\t\t\t| CHAR\n\t\n\tdeclaracion_inicial : dec_varaux punto_dec_var_1 COMMA declaracion_inicial\n\t\t\t\t\t\t\t\t\t\t\t| dec_varaux punto_dec_var_1\n\t\n\tpunto_dec_var_1 :\n\t\n\tdec_varaux : ID \n\t\t\t\t\t\t\t| ID LEFT_BR CTE_I RIGHT_BR \n\t\t\t\t\t\t\t| ID LEFT_BR CTE_I RIGHT_BR LEFT_BR CTE_I RIGHT_BR\n\t\n\tpunto_dec_varaux_1 :\n\n\t\n\tdec_var : dec_varaux COMMA dec_var\n\t\t\t\t\t| dec_varaux\n\t\n\tdec_var_llamada : m_exp punto_verify_dec_param COMMA punto_mas_k dec_var_llamada\n\t\t\t\t\t| m_exp punto_verify_dec_param\n\t\n\tpunto_mas_k :\n\n\t\n\tpunto_verify_dec_param : \n\t\n\tfunciones : funciones_aux\n\t\t\t\t\t\t| funciones_aux funciones\n\t\n\t\n\t\tfunciones_aux : tipo FUNC ID punto_id_func punto_return_value LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables estatutos RIGHT_CURL punto_end_function_return\n\t\t\t\t\t\t\t\t | VOID FUNC ID punto_id_func LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables count_vars estatutos RIGHT_CURL end_func\n\t\n\tpunto_return_value :\n\n\t\n\tnot_variables : variables count_vars\n\t\t\t\t\t\t\t\t| empty\n\t\n\tnot_params : parametros count_params\n\t\t\t\t\t\t | empty\n\t\n\t\tpunto_end_function_return :\n\t\n\tpunto_id_func :\n\t\n\tparametros : dec_var_param COMMA parametros\n\t\t\t\t\t\t\t| dec_var_param\n\n\t\n\tdec_var_param : tipo ID punto_push_param\n\t\n\tpunto_push_param :\n\t\n\tcount_params :\n\t\n\tcount_vars :\n\t\n\tend_func :\n\t\n\t\texp_or : t_exp punto_pop_or t_exp_or_aux\n\t\t\t\t\t| t_exp punto_pop_or\n\t\n\t\tpunto_pop_or :\n\t\n\t\n\tt_exp_or_aux : OR punto_push_or exp_or\n\t\n\tpunto_push_or :\n\t\n\tt_exp : g_exp pop_and t_exp_aux\n\t\t\t\t| g_exp pop_and\n\n\t\n\tpop_and :\n\t\n\t\n\tt_exp_aux : AND punto_push_and t_exp\n\n\t\n\tpunto_push_and :\n\t\n\t\tg_exp : m_exp\n\t\t\t\t\t| m_exp relacionales punto_relacionales m_exp punto_pop_relacional\n\t\n\tpunto_relacionales :\n\t\n\tpunto_pop_relacional :\n\t\n\tm_exp : termino punto_mexp_pop\n\t\t\t\t| termino punto_mexp_pop m_exp_aux\n\t\n\tpunto_mexp_pop :\n\t\n\tm_exp_aux : PLUS punto_m_exp_push m_exp\n\t\t\t\t\t\t| MINUS punto_m_exp_push m_exp\n\n\t\n\tpunto_m_exp_push :\n\t\n\ttermino : factor punto_termino_pop\n\t\t\t\t\t| factor punto_termino_pop termino_aux\n\t\n\tpunto_termino_pop :\n\t\n  termino_aux : MULTIPLY punto_termino_aux termino\n              | DIVIDE punto_termino_aux termino\n  \n\tpunto_termino_aux :\n\t\n\tfactor : cte\n\t\t\t\t\t| ID LEFT_PAR dec_var RIGHT_PAR\n\t\t\t\t\t| ID LEFT_PAR RIGHT_PAR\n\t\t\t\t\t| LEFT_PAR exp_or RIGHT_PAR\n\t\n\trelacionales : LESS_THAN\n\t\t\t\t\t\t\t\t\t| GREATER_THAN\n\t\t\t\t\t\t\t\t\t| DIFFERENT\n\t\t\t\t\t\t\t\t\t| EQUAL\n\t\t\t\t\t\t\t\t\t| GREATER_EQUAL\n\t\t\t\t\t\t\t\t\t| LESS_EQUAL\n\t\n\testatutos : estatutos_main_aux \n\t\t\t\t\t\t| retorno SEMICOLON \n\n\t\n\testatutos_main : asignacion SEMICOLON\n\t\t\t\t\t\t\t\t\t| llamada SEMICOLON\n\t\t\t\t\t\t\t\t\t| lectura SEMICOLON\n\t\t\t\t\t\t\t\t\t| escritura SEMICOLON\n\t\t\t\t\t\t\t\t\t| decision SEMICOLON\n\t\t\t\t\t\t\t\t\t| repeticion SEMICOLON\n\t\n\testatutos_main_multiple : estatutos_main estatutos_main_multiple\n\t\t\t\t\t\t\t\t\t\t| estatutos_main\n\t\n\testatutos_main_aux : estatutos_main estatutos\n\t\t\t\t\t\t\t\t\t\t\t| estatutos_main\n\n\t\n\tasignacion : dec_varaux punto_asignacion_var EQUALS punto_igual m_exp punto_asignacion\n\n\t\n\tpunto_asignacion_var : \n\t\n\tpunto_igual :\n\t\n\tpunto_asignacion : \n\n\t\n\t\tllamada : ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada\n\t\t\t\t\t\t| ID punto_verify_id LEFT_PAR punto_era dec_var_llamada RIGHT_PAR punto_verify_total_params punto_end_llamada\n\t\t\t\t\t\t\n\t\n\tpunto_verify_id :\n\t\n\tpunto_verify_total_params :\n\t\n\tpunto_end_llamada :\n\t\n\tpunto_era :\n\t\n\t\tretorno : RETURN LEFT_PAR m_exp RIGHT_PAR punto_return\n\t\n\tpunto_return :\n\t\n\t\n\tpunto_read_stack : \n\t\n\tlectura : READ LEFT_PAR lectura_var RIGHT_PAR\n\t\n\tlectura_var : punto_read_stack dec_varaux punto_push_dec_var punto_add_read_operand COMMA lectura_var\n\t\t\t\t\t| punto_read_stack dec_varaux punto_push_dec_var punto_add_read_operand\n\t\n\tpunto_push_dec_var :\n\t\n\t\tpunto_add_read_operand : \n\t\n\tescritura : WRITE LEFT_PAR escritura_aux RIGHT_PAR\n\t\n\tescritura_aux : punto_write_stack STR punto_escritura_push punto_add_write_operand\n\t\t\t\t\t\t\t\t| punto_write_stack m_exp punto_escritura_push punto_add_write_operand\n\t\t\t\t\t\t\t\t| punto_write_stack STR punto_escritura_push punto_add_write_operand COMMA escritura_aux \n\t\t\t\t\t\t\t\t| punto_write_stack m_exp punto_escritura_push punto_add_write_operand COMMA escritura_aux\n\t\n\tpunto_escritura_push : \n\n\t\n\tpunto_write_stack :\n\t\n\tpunto_add_write_operand : \n\t\n\tdecision : IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp THEN LEFT_CURL estatutos RIGHT_CURL punto_end_if \n\t\t\t\t\t\t| IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp THEN LEFT_CURL estatutos RIGHT_CURL ELSE punto_else LEFT_CURL estatutos RIGHT_CURL punto_end_if\n\t\n\tpunto_if_exp :\n\t\n\tpunto_else :\n\t\n\tpunto_end_if :\n\t\n\trepeticion : condicional\n\t\t\t\t\t\t\t| no_condicional\n\t\n\tno_condicional : FOR LEFT_PAR dec_varaux punto_for EQUALS m_exp punto_exp_for_inf TO m_exp punto_exp_for_sup RIGHT_PAR LEFT_CURL estatutos RIGHT_CURL punto_end_for\n\t\n\tpunto_for :\n\t\n\tpunto_exp_for_inf :\n\t\n\tpunto_exp_for_sup :\n\t\n\tpunto_end_for :\n\t\n\tcondicional : WHILE punto_while LEFT_PAR exp_or RIGHT_PAR punto_validar_exp LEFT_CURL estatutos RIGHT_CURL punto_end_while\n\t\n\tpunto_while :\n\t\n\tpunto_validar_exp :\n\t\n\tpunto_end_while :\n\t\n\tcte : ID factor_push_operand\n\t\t\t| CTE_I factor_int_push\n\t\t\t| cte_f factor_float_push\n\t\t\t| CTE_CHAR factor_char_push\n\t\n\tfactor_push_operand :\n\t\n\tfactor_float_push :\n\t\n\tfactor_int_push :\n\t\n\tfactor_char_push :\n\t\n\tempty : \n\t'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,6,17,19,25,61,],[0,-2,-3,-5,-4,-7,]),'ID':([2,14,15,16,23,24,27,32,33,34,40,63,64,65,66,67,68,72,73,74,76,84,85,86,89,91,92,104,107,113,114,125,126,127,128,129,130,131,134,144,158,160,161,163,164,166,167,173,174,175,176,177,187,188,190,191,192,193,195,198,199,200,202,204,205,206,207,216,221,225,231,235,252,253,],[3,-15,-16,-17,30,31,-10,48,-11,58,48,-87,-88,-89,-90,-91,-92,-109,-121,100,58,112,-99,-106,58,100,100,100,58,100,100,-61,-79,-80,-81,-82,-83,-84,58,-147,-53,-58,100,-68,-68,-74,-74,100,-147,-47,-47,-37,100,100,100,100,100,100,58,48,48,-36,-29,-109,-121,-121,48,48,48,100,100,100,48,48,]),'COLON':([3,4,14,15,16,29,],[-6,5,-15,-16,-17,34,]),'MAIN':([5,7,8,11,18,22,27,33,232,236,241,243,],[9,9,9,-31,9,-32,-10,-11,-40,-48,-33,-34,]),'VAR':([5,144,174,],[10,10,10,]),'VOID':([5,7,11,27,33,232,236,241,243,],[13,13,13,-10,-11,-40,-48,-33,-34,]),'INT':([5,7,10,11,21,27,33,60,77,79,111,232,236,241,243,],[14,14,-12,14,14,-10,-11,14,14,14,14,-40,-48,-33,-34,]),'FLOAT':([5,7,10,11,21,27,33,60,77,79,111,232,236,241,243,],[15,15,-12,15,15,-10,-11,15,15,15,15,-40,-48,-33,-34,]),'CHAR':([5,7,10,11,21,27,33,60,77,79,111,232,236,241,243,],[16,16,-12,16,16,-10,-11,16,16,16,16,-40,-48,-33,-34,]),'LEFT_PAR':([9,30,31,35,36,48,49,50,51,54,55,59,70,73,74,75,85,86,91,92,100,104,113,114,125,126,127,128,129,130,131,158,160,161,163,164,166,167,173,187,188,190,191,192,193,202,205,206,222,225,231,235,],[20,-41,-41,-35,60,-103,72,73,74,-136,76,79,86,-121,92,104,-99,-106,92,92,134,92,92,92,-61,-79,-80,-81,-82,-83,-84,-53,-58,92,-68,-68,-74,-74,92,92,92,92,92,92,92,-29,-121,-121,235,92,92,92,]),'SEMICOLON':([10,21,28,41,42,43,44,45,46,52,53,56,57,58,78,97,98,99,100,101,102,103,106,115,116,118,132,133,135,136,138,139,142,147,148,155,162,165,169,171,178,179,180,194,201,203,211,212,213,214,220,224,238,239,244,246,248,251,256,257,258,259,],[-12,27,33,63,64,65,66,67,68,-128,-129,-13,-20,-21,-19,-65,-71,-75,-143,-145,-144,-146,-14,-22,-110,-115,-63,-69,-139,-140,-141,-142,-18,-100,-105,-78,-64,-70,-77,-1,-97,-101,-104,-76,-105,-23,-66,-67,-72,-73,233,-102,-127,-138,-123,-135,-108,-107,-127,-134,-124,-130,]),'FUNC':([12,13,14,15,16,],[23,24,-15,-16,-17,]),'RIGHT_PAR':([20,58,60,79,80,81,82,83,86,88,90,93,94,95,96,97,98,99,100,101,102,103,108,110,112,114,115,117,119,120,121,123,124,132,133,134,135,136,138,139,140,145,146,149,150,152,153,154,155,157,159,162,165,168,169,170,171,181,183,184,185,189,194,203,208,209,210,211,212,213,214,215,226,227,228,237,240,242,247,],[26,-21,-147,-147,109,-46,-39,-43,-106,116,118,122,-51,-56,-59,-65,-71,-75,-143,-145,-144,-146,143,-38,-45,148,-22,-113,-120,-120,155,-50,-55,-63,-69,169,-139,-140,-141,-142,172,-42,-44,180,-30,-114,-122,-122,-78,-49,-54,-64,-70,194,-77,-26,-1,-28,-112,-116,-117,-62,-76,-23,-52,-57,-60,-66,-67,-72,-73,-25,-111,-118,-119,-27,-133,248,250,]),'LEFT_CURL':([26,109,143,172,186,196,245,249,250,],[32,144,174,-137,207,216,-126,252,253,]),'RETURN':([27,33,63,64,65,66,67,68,144,174,175,176,177,198,199,200,207,216,221,252,253,],[-10,-11,-87,-88,-89,-90,-91,-92,-147,-147,-47,-47,-37,222,222,-36,222,222,222,222,222,]),'READ':([27,32,33,40,63,64,65,66,67,68,144,174,175,176,177,198,199,200,207,216,221,252,253,],[-10,49,-11,49,-87,-88,-89,-90,-91,-92,-147,-147,-47,-47,-37,49,49,-36,49,49,49,49,49,]),'WRITE':([27,32,33,40,63,64,65,66,67,68,144,174,175,176,177,198,199,200,207,216,221,252,253,],[-10,50,-11,50,-87,-88,-89,-90,-91,-92,-147,-147,-47,-47,-37,50,50,-36,50,50,50,50,50,]),'IF':([27,32,33,40,63,64,65,66,67,68,144,174,175,176,177,198,199,200,207,216,221,252,253,],[-10,51,-11,51,-87,-88,-89,-90,-91,-92,-147,-147,-47,-47,-37,51,51,-36,51,51,51,51,51,]),'WHILE':([27,32,33,40,63,64,65,66,67,68,144,174,175,176,177,198,199,200,207,216,221,252,253,],[-10,54,-11,54,-87,-88,-89,-90,-91,-92,-147,-147,-47,-47,-37,54,54,-36,54,54,54,54,54,]),'FOR':([27,32,33,40,63,64,65,66,67,68,144,174,175,176,177,198,199,200,207,216,221,252,253,],[-10,55,-11,55,-87,-88,-89,-90,-91,-92,-147,-147,-47,-47,-37,55,55,-36,55,55,55,55,55,]),'RIGHT_CURL':([32,37,38,39,40,62,63,64,65,66,67,68,218,219,221,223,229,230,233,234,254,255,],[-147,61,-8,-9,-94,-93,-87,-88,-89,-90,-91,-92,232,-85,-96,236,238,239,-86,-95,256,257,]),'EQUALS':([47,48,58,69,105,115,141,203,],[-98,-21,-21,85,-131,-22,173,-23,]),'LEFT_BR':([48,58,115,],[71,71,151,]),'MORE':([56,57,58,78,115,142,203,],[77,-20,-21,-19,-22,-18,-23,]),'COMMA':([57,58,78,83,97,98,99,100,101,102,103,112,115,117,119,120,132,133,135,136,138,139,146,150,152,153,154,155,162,165,169,170,171,181,183,184,185,194,203,211,212,213,214,],[-20,-21,107,111,-65,-71,-75,-143,-145,-144,-146,-45,-22,-113,-120,-120,-63,-69,-139,-140,-141,-142,-44,-30,-114,-122,-122,-78,-64,-70,-77,195,-1,202,204,205,206,-76,-23,-66,-67,-72,-73,]),'CTE_I':([71,73,74,85,86,91,92,104,113,114,125,126,127,128,129,130,131,137,151,158,160,161,163,164,166,167,173,187,188,190,191,192,193,202,205,206,225,231,235,],[87,-121,101,-99,-106,101,101,101,101,101,-61,-79,-80,-81,-82,-83,-84,171,182,-53,-58,101,-68,-68,-74,-74,101,101,101,101,101,101,101,-29,-121,-121,101,101,101,]),'STR':([73,91,205,206,],[-121,119,-121,-121,]),'CTE_CHAR':([73,74,85,86,91,92,104,113,114,125,126,127,128,129,130,131,158,160,161,163,164,166,167,173,187,188,190,191,192,193,202,205,206,225,231,235,],[-121,103,-99,-106,103,103,103,103,103,-61,-79,-80,-81,-82,-83,-84,-53,-58,103,-68,-68,-74,-74,103,103,103,103,103,103,103,-29,-121,-121,103,103,103,]),'RIGHT_BR':([87,182,],[115,203,]),'OR':([94,95,96,97,98,99,100,101,102,103,123,124,132,133,135,136,138,139,155,159,162,165,169,171,189,194,209,210,211,212,213,214,],[-51,-56,-59,-65,-71,-75,-143,-145,-144,-146,158,-55,-63,-69,-139,-140,-141,-142,-78,-54,-64,-70,-77,-1,-62,-76,-57,-60,-66,-67,-72,-73,]),'AND':([95,96,97,98,99,100,101,102,103,124,132,133,135,136,138,139,155,162,165,169,171,189,194,210,211,212,213,214,],[-56,-59,-65,-71,-75,-143,-145,-144,-146,160,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-62,-76,-60,-66,-67,-72,-73,]),'LESS_THAN':([96,97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,211,212,213,214,],[126,-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-66,-67,-72,-73,]),'GREATER_THAN':([96,97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,211,212,213,214,],[127,-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-66,-67,-72,-73,]),'DIFFERENT':([96,97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,211,212,213,214,],[128,-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-66,-67,-72,-73,]),'EQUAL':([96,97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,211,212,213,214,],[129,-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-66,-67,-72,-73,]),'GREATER_EQUAL':([96,97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,211,212,213,214,],[130,-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-66,-67,-72,-73,]),'LESS_EQUAL':([96,97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,211,212,213,214,],[131,-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-66,-67,-72,-73,]),'PLUS':([97,98,99,100,101,102,103,132,133,135,136,138,139,155,165,169,171,194,213,214,],[-65,-71,-75,-143,-145,-144,-146,163,-69,-139,-140,-141,-142,-78,-70,-77,-1,-76,-72,-73,]),'MINUS':([97,98,99,100,101,102,103,132,133,135,136,138,139,155,165,169,171,194,213,214,],[-65,-71,-75,-143,-145,-144,-146,164,-69,-139,-140,-141,-142,-78,-70,-77,-1,-76,-72,-73,]),'TO':([97,98,99,100,101,102,103,132,133,135,136,138,139,155,162,165,169,171,194,197,211,212,213,214,217,],[-65,-71,-75,-143,-145,-144,-146,-63,-69,-139,-140,-141,-142,-78,-64,-70,-77,-1,-76,-132,-66,-67,-72,-73,231,]),'MULTIPLY':([98,99,100,101,102,103,133,135,136,138,139,155,169,171,194,],[-71,-75,-143,-145,-144,-146,166,-139,-140,-141,-142,-78,-77,-1,-76,]),'DIVIDE':([98,99,100,101,102,103,133,135,136,138,139,155,169,171,194,],[-71,-75,-143,-145,-144,-146,167,-139,-140,-141,-142,-78,-77,-1,-76,]),'DOT':([101,],[137,]),'THEN':([122,156,],[-125,186,]),'ELSE':([238,],[245,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'punto_program':([3,],[4,]),'main':([5,7,8,18,],[6,17,19,25,]),'variables':([5,144,174,],[7,176,176,]),'funciones':([5,7,11,],[8,18,22,]),'funciones_aux':([5,7,11,],[11,11,11,]),'tipo':([5,7,11,21,60,77,79,111,],[12,12,12,29,84,29,84,84,]),'punto_variables_1':([10,],[21,]),'variables_aux':([21,77,],[28,106,]),'punto_id_func':([30,31,],[35,36,]),'main_aux':([32,],[37,]),'estatutos_main_multiple':([32,40,],[38,62,]),'empty':([32,60,79,144,174,],[39,82,82,177,177,]),'estatutos_main':([32,40,198,199,207,216,221,252,253,],[40,40,221,221,221,221,221,221,221,]),'asignacion':([32,40,198,199,207,216,221,252,253,],[41,41,41,41,41,41,41,41,41,]),'llamada':([32,40,198,199,207,216,221,252,253,],[42,42,42,42,42,42,42,42,42,]),'lectura':([32,40,198,199,207,216,221,252,253,],[43,43,43,43,43,43,43,43,43,]),'escritura':([32,40,198,199,207,216,221,252,253,],[44,44,44,44,44,44,44,44,44,]),'decision':([32,40,198,199,207,216,221,252,253,],[45,45,45,45,45,45,45,45,45,]),'repeticion':([32,40,198,199,207,216,221,252,253,],[46,46,46,46,46,46,46,46,46,]),'dec_varaux':([32,34,40,76,89,107,134,195,198,199,207,216,221,252,253,],[47,57,47,105,117,57,170,170,47,47,47,47,47,47,47,]),'condicional':([32,40,198,199,207,216,221,252,253,],[52,52,52,52,52,52,52,52,52,]),'no_condicional':([32,40,198,199,207,216,221,252,253,],[53,53,53,53,53,53,53,53,53,]),'declaracion_inicial':([34,107,],[56,142,]),'punto_return_value':([35,],[59,]),'punto_asignacion_var':([47,],[69,]),'punto_verify_id':([48,],[70,]),'punto_while':([54,],[75,]),'punto_dec_var_1':([57,],[78,]),'not_params':([60,79,],[80,108,]),'parametros':([60,79,111,],[81,81,145,]),'dec_var_param':([60,79,111,],[83,83,83,]),'lectura_var':([72,204,],[88,226,]),'punto_read_stack':([72,204,],[89,89,]),'escritura_aux':([73,205,206,],[90,227,228,]),'punto_write_stack':([73,205,206,],[91,91,91,]),'exp_or':([74,92,104,187,],[93,121,140,208,]),'t_exp':([74,92,104,187,188,],[94,94,94,94,209,]),'g_exp':([74,92,104,187,188,],[95,95,95,95,95,]),'m_exp':([74,91,92,104,113,114,161,173,187,188,190,191,225,231,235,],[96,120,96,96,147,150,189,197,96,96,211,212,150,240,242,]),'termino':([74,91,92,104,113,114,161,173,187,188,190,191,192,193,225,231,235,],[97,97,97,97,97,97,97,97,97,97,97,97,213,214,97,97,97,]),'factor':([74,91,92,104,113,114,161,173,187,188,190,191,192,193,225,231,235,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'cte':([74,91,92,104,113,114,161,173,187,188,190,191,192,193,225,231,235,],[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'cte_f':([74,91,92,104,113,114,161,173,187,188,190,191,192,193,225,231,235,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'count_params':([81,],[110,]),'punto_igual':([85,],[113,]),'punto_era':([86,],[114,]),'punto_pop_or':([94,],[123,]),'pop_and':([95,],[124,]),'relacionales':([96,],[125,]),'punto_mexp_pop':([97,],[132,]),'punto_termino_pop':([98,],[133,]),'factor_push_operand':([100,],[135,]),'factor_int_push':([101,],[136,]),'factor_float_push':([102,],[138,]),'factor_char_push':([103,],[139,]),'punto_for':([105,],[141,]),'punto_push_param':([112,],[146,]),'dec_var_llamada':([114,225,],[149,237,]),'punto_push_dec_var':([117,],[152,]),'punto_escritura_push':([119,120,],[153,154,]),'punto_if_exp':([122,],[156,]),'t_exp_or_aux':([123,],[157,]),'t_exp_aux':([124,],[159,]),'punto_relacionales':([125,],[161,]),'m_exp_aux':([132,],[162,]),'termino_aux':([133,],[165,]),'dec_var':([134,195,],[168,215,]),'not_variables':([144,174,],[175,198,]),'punto_asignacion':([147,],[178,]),'punto_end_llamada':([148,201,],[179,224,]),'punto_verify_dec_param':([150,],[181,]),'punto_add_read_operand':([152,],[183,]),'punto_add_write_operand':([153,154,],[184,185,]),'punto_push_or':([158,],[187,]),'punto_push_and':([160,],[188,]),'punto_m_exp_push':([163,164,],[190,191,]),'punto_termino_aux':([166,167,],[192,193,]),'punto_validar_exp':([172,],[196,]),'count_vars':([175,176,],[199,200,]),'punto_verify_total_params':([180,],[201,]),'punto_pop_relacional':([189,],[210,]),'punto_exp_for_inf':([197,],[217,]),'estatutos':([198,199,207,216,221,252,253,],[218,223,229,230,234,254,255,]),'estatutos_main_aux':([198,199,207,216,221,252,253,],[219,219,219,219,219,219,219,]),'retorno':([198,199,207,216,221,252,253,],[220,220,220,220,220,220,220,]),'punto_mas_k':([202,],[225,]),'punto_end_function_return':([232,],[241,]),'end_func':([236,],[243,]),'punto_end_if':([238,256,],[244,258,]),'punto_end_while':([239,],[246,]),'punto_exp_for_sup':([240,],[247,]),'punto_else':([245,],[249,]),'punto_return':([248,],[251,]),'punto_end_for':([257,],[259,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('cte_f -> CTE_I DOT CTE_I','cte_f',3,'p_cte_f','lexer.py',120),
  ('program -> PROGRAM ID punto_program COLON main','program',5,'p_program','lexer.py',132),
  ('program -> PROGRAM ID punto_program COLON variables main','program',6,'p_program','lexer.py',133),
  ('program -> PROGRAM ID punto_program COLON variables funciones main','program',7,'p_program','lexer.py',134),
  ('program -> PROGRAM ID punto_program COLON funciones main','program',6,'p_program','lexer.py',135),
  ('punto_program -> <empty>','punto_program',0,'p_punto_program','lexer.py',140),
  ('main -> MAIN LEFT_PAR RIGHT_PAR LEFT_CURL main_aux RIGHT_CURL','main',6,'p_main','lexer.py',154),
  ('main_aux -> estatutos_main_multiple','main_aux',1,'p_main_aux','lexer.py',160),
  ('main_aux -> empty','main_aux',1,'p_main_aux','lexer.py',161),
  ('variables -> VAR punto_variables_1 SEMICOLON','variables',3,'p_variables','lexer.py',166),
  ('variables -> VAR punto_variables_1 variables_aux SEMICOLON','variables',4,'p_variables','lexer.py',167),
  ('punto_variables_1 -> <empty>','punto_variables_1',0,'p_punto_variables_1','lexer.py',172),
  ('variables_aux -> tipo COLON declaracion_inicial','variables_aux',3,'p_variables_aux','lexer.py',178),
  ('variables_aux -> tipo COLON declaracion_inicial MORE variables_aux','variables_aux',5,'p_variables_aux','lexer.py',179),
  ('tipo -> INT','tipo',1,'p_tipo','lexer.py',184),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lexer.py',185),
  ('tipo -> CHAR','tipo',1,'p_tipo','lexer.py',186),
  ('declaracion_inicial -> dec_varaux punto_dec_var_1 COMMA declaracion_inicial','declaracion_inicial',4,'p_declaracion_inicial','lexer.py',201),
  ('declaracion_inicial -> dec_varaux punto_dec_var_1','declaracion_inicial',2,'p_declaracion_inicial','lexer.py',202),
  ('punto_dec_var_1 -> <empty>','punto_dec_var_1',0,'p_punto_dec_var_1','lexer.py',207),
  ('dec_varaux -> ID','dec_varaux',1,'p_dec_varaux','lexer.py',217),
  ('dec_varaux -> ID LEFT_BR CTE_I RIGHT_BR','dec_varaux',4,'p_dec_varaux','lexer.py',218),
  ('dec_varaux -> ID LEFT_BR CTE_I RIGHT_BR LEFT_BR CTE_I RIGHT_BR','dec_varaux',7,'p_dec_varaux','lexer.py',219),
  ('punto_dec_varaux_1 -> <empty>','punto_dec_varaux_1',0,'p_punto_dec_varaux_1','lexer.py',228),
  ('dec_var -> dec_varaux COMMA dec_var','dec_var',3,'p_dec_var','lexer.py',234),
  ('dec_var -> dec_varaux','dec_var',1,'p_dec_var','lexer.py',235),
  ('dec_var_llamada -> m_exp punto_verify_dec_param COMMA punto_mas_k dec_var_llamada','dec_var_llamada',5,'p_dec_var_llamada','lexer.py',240),
  ('dec_var_llamada -> m_exp punto_verify_dec_param','dec_var_llamada',2,'p_dec_var_llamada','lexer.py',241),
  ('punto_mas_k -> <empty>','punto_mas_k',0,'p_punto_mas_k','lexer.py',245),
  ('punto_verify_dec_param -> <empty>','punto_verify_dec_param',0,'p_punto_verify_dec_param','lexer.py',253),
  ('funciones -> funciones_aux','funciones',1,'p_funciones','lexer.py',267),
  ('funciones -> funciones_aux funciones','funciones',2,'p_funciones','lexer.py',268),
  ('funciones_aux -> tipo FUNC ID punto_id_func punto_return_value LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables estatutos RIGHT_CURL punto_end_function_return','funciones_aux',13,'p_funciones_aux','lexer.py',275),
  ('funciones_aux -> VOID FUNC ID punto_id_func LEFT_PAR not_params RIGHT_PAR LEFT_CURL not_variables count_vars estatutos RIGHT_CURL end_func','funciones_aux',13,'p_funciones_aux','lexer.py',276),
  ('punto_return_value -> <empty>','punto_return_value',0,'p_punto_return_value','lexer.py',280),
  ('not_variables -> variables count_vars','not_variables',2,'p_not_variables','lexer.py',288),
  ('not_variables -> empty','not_variables',1,'p_not_variables','lexer.py',289),
  ('not_params -> parametros count_params','not_params',2,'p_not_params','lexer.py',294),
  ('not_params -> empty','not_params',1,'p_not_params','lexer.py',295),
  ('punto_end_function_return -> <empty>','punto_end_function_return',0,'p_punto_end_function_return','lexer.py',300),
  ('punto_id_func -> <empty>','punto_id_func',0,'p_punto_id_func','lexer.py',315),
  ('parametros -> dec_var_param COMMA parametros','parametros',3,'p_parametros','lexer.py',332),
  ('parametros -> dec_var_param','parametros',1,'p_parametros','lexer.py',333),
  ('dec_var_param -> tipo ID punto_push_param','dec_var_param',3,'p_dec_var_param','lexer.py',339),
  ('punto_push_param -> <empty>','punto_push_param',0,'p_punto_push_param','lexer.py',344),
  ('count_params -> <empty>','count_params',0,'p_count_params','lexer.py',364),
  ('count_vars -> <empty>','count_vars',0,'p_count_vars','lexer.py',371),
  ('end_func -> <empty>','end_func',0,'p_end_func','lexer.py',379),
  ('exp_or -> t_exp punto_pop_or t_exp_or_aux','exp_or',3,'p_exp_or','lexer.py',392),
  ('exp_or -> t_exp punto_pop_or','exp_or',2,'p_exp_or','lexer.py',393),
  ('punto_pop_or -> <empty>','punto_pop_or',0,'p_punto_pop_or','lexer.py',397),
  ('t_exp_or_aux -> OR punto_push_or exp_or','t_exp_or_aux',3,'p_t_exp_or_aux','lexer.py',440),
  ('punto_push_or -> <empty>','punto_push_or',0,'p_punto_push_or','lexer.py',445),
  ('t_exp -> g_exp pop_and t_exp_aux','t_exp',3,'p_t_exp','lexer.py',453),
  ('t_exp -> g_exp pop_and','t_exp',2,'p_t_exp','lexer.py',454),
  ('pop_and -> <empty>','pop_and',0,'p_pop_and','lexer.py',459),
  ('t_exp_aux -> AND punto_push_and t_exp','t_exp_aux',3,'p_t_exp_aux','lexer.py',502),
  ('punto_push_and -> <empty>','punto_push_and',0,'p_punto_push_and','lexer.py',507),
  ('g_exp -> m_exp','g_exp',1,'p_g_exp','lexer.py',514),
  ('g_exp -> m_exp relacionales punto_relacionales m_exp punto_pop_relacional','g_exp',5,'p_g_exp','lexer.py',515),
  ('punto_relacionales -> <empty>','punto_relacionales',0,'p_punto_relacionales','lexer.py',519),
  ('punto_pop_relacional -> <empty>','punto_pop_relacional',0,'p_punto_pop_relacional','lexer.py',528),
  ('m_exp -> termino punto_mexp_pop','m_exp',2,'p_m_exp','lexer.py',571),
  ('m_exp -> termino punto_mexp_pop m_exp_aux','m_exp',3,'p_m_exp','lexer.py',572),
  ('punto_mexp_pop -> <empty>','punto_mexp_pop',0,'p_punto_mexp_pop','lexer.py',579),
  ('m_exp_aux -> PLUS punto_m_exp_push m_exp','m_exp_aux',3,'p_m_exp_aux','lexer.py',625),
  ('m_exp_aux -> MINUS punto_m_exp_push m_exp','m_exp_aux',3,'p_m_exp_aux','lexer.py',626),
  ('punto_m_exp_push -> <empty>','punto_m_exp_push',0,'p_punto_m_exp_push','lexer.py',631),
  ('termino -> factor punto_termino_pop','termino',2,'p_termino','lexer.py',641),
  ('termino -> factor punto_termino_pop termino_aux','termino',3,'p_termino','lexer.py',642),
  ('punto_termino_pop -> <empty>','punto_termino_pop',0,'p_punto_termino_pop','lexer.py',648),
  ('termino_aux -> MULTIPLY punto_termino_aux termino','termino_aux',3,'p_termino_aux','lexer.py',693),
  ('termino_aux -> DIVIDE punto_termino_aux termino','termino_aux',3,'p_termino_aux','lexer.py',694),
  ('punto_termino_aux -> <empty>','punto_termino_aux',0,'p_punto_termino_aux','lexer.py',699),
  ('factor -> cte','factor',1,'p_factor','lexer.py',708),
  ('factor -> ID LEFT_PAR dec_var RIGHT_PAR','factor',4,'p_factor','lexer.py',709),
  ('factor -> ID LEFT_PAR RIGHT_PAR','factor',3,'p_factor','lexer.py',710),
  ('factor -> LEFT_PAR exp_or RIGHT_PAR','factor',3,'p_factor','lexer.py',711),
  ('relacionales -> LESS_THAN','relacionales',1,'p_relacionales','lexer.py',718),
  ('relacionales -> GREATER_THAN','relacionales',1,'p_relacionales','lexer.py',719),
  ('relacionales -> DIFFERENT','relacionales',1,'p_relacionales','lexer.py',720),
  ('relacionales -> EQUAL','relacionales',1,'p_relacionales','lexer.py',721),
  ('relacionales -> GREATER_EQUAL','relacionales',1,'p_relacionales','lexer.py',722),
  ('relacionales -> LESS_EQUAL','relacionales',1,'p_relacionales','lexer.py',723),
  ('estatutos -> estatutos_main_aux','estatutos',1,'p_estatutos','lexer.py',730),
  ('estatutos -> retorno SEMICOLON','estatutos',2,'p_estatutos','lexer.py',731),
  ('estatutos_main -> asignacion SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',737),
  ('estatutos_main -> llamada SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',738),
  ('estatutos_main -> lectura SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',739),
  ('estatutos_main -> escritura SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',740),
  ('estatutos_main -> decision SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',741),
  ('estatutos_main -> repeticion SEMICOLON','estatutos_main',2,'p_estatutos_main','lexer.py',742),
  ('estatutos_main_multiple -> estatutos_main estatutos_main_multiple','estatutos_main_multiple',2,'p_estatutos_main_multiple','lexer.py',747),
  ('estatutos_main_multiple -> estatutos_main','estatutos_main_multiple',1,'p_estatutos_main_multiple','lexer.py',748),
  ('estatutos_main_aux -> estatutos_main estatutos','estatutos_main_aux',2,'p_estatutos_main_aux','lexer.py',753),
  ('estatutos_main_aux -> estatutos_main','estatutos_main_aux',1,'p_estatutos_main_aux','lexer.py',754),
  ('asignacion -> dec_varaux punto_asignacion_var EQUALS punto_igual m_exp punto_asignacion','asignacion',6,'p_asignacion','lexer.py',760),
  ('punto_asignacion_var -> <empty>','punto_asignacion_var',0,'p_punto_asignacion_var','lexer.py',766),
  ('punto_igual -> <empty>','punto_igual',0,'p_punto_igual','lexer.py',781),
  ('punto_asignacion -> <empty>','punto_asignacion',0,'p_punto_asignacion','lexer.py',788),
  ('llamada -> ID punto_verify_id LEFT_PAR punto_era RIGHT_PAR punto_end_llamada','llamada',6,'p_llamada','lexer.py',815),
  ('llamada -> ID punto_verify_id LEFT_PAR punto_era dec_var_llamada RIGHT_PAR punto_verify_total_params punto_end_llamada','llamada',8,'p_llamada','lexer.py',816),
  ('punto_verify_id -> <empty>','punto_verify_id',0,'p_punto_verify_id','lexer.py',821),
  ('punto_verify_total_params -> <empty>','punto_verify_total_params',0,'p_punto_verify_total_params','lexer.py',829),
  ('punto_end_llamada -> <empty>','punto_end_llamada',0,'p_punto_end_llamada','lexer.py',838),
  ('punto_era -> <empty>','punto_era',0,'p_punto_era','lexer.py',846),
  ('retorno -> RETURN LEFT_PAR m_exp RIGHT_PAR punto_return','retorno',5,'p_retorno','lexer.py',857),
  ('punto_return -> <empty>','punto_return',0,'p_punto_return','lexer.py',861),
  ('punto_read_stack -> <empty>','punto_read_stack',0,'p_punto_read_stack','lexer.py',873),
  ('lectura -> READ LEFT_PAR lectura_var RIGHT_PAR','lectura',4,'p_lectura','lexer.py',882),
  ('lectura_var -> punto_read_stack dec_varaux punto_push_dec_var punto_add_read_operand COMMA lectura_var','lectura_var',6,'p_lectura_var','lexer.py',887),
  ('lectura_var -> punto_read_stack dec_varaux punto_push_dec_var punto_add_read_operand','lectura_var',4,'p_lectura_var','lexer.py',888),
  ('punto_push_dec_var -> <empty>','punto_push_dec_var',0,'p_punto_push_dec_var','lexer.py',894),
  ('punto_add_read_operand -> <empty>','punto_add_read_operand',0,'p_punto_add_read_operand','lexer.py',911),
  ('escritura -> WRITE LEFT_PAR escritura_aux RIGHT_PAR','escritura',4,'p_escritura','lexer.py',927),
  ('escritura_aux -> punto_write_stack STR punto_escritura_push punto_add_write_operand','escritura_aux',4,'p_escritura_aux','lexer.py',932),
  ('escritura_aux -> punto_write_stack m_exp punto_escritura_push punto_add_write_operand','escritura_aux',4,'p_escritura_aux','lexer.py',933),
  ('escritura_aux -> punto_write_stack STR punto_escritura_push punto_add_write_operand COMMA escritura_aux','escritura_aux',6,'p_escritura_aux','lexer.py',934),
  ('escritura_aux -> punto_write_stack m_exp punto_escritura_push punto_add_write_operand COMMA escritura_aux','escritura_aux',6,'p_escritura_aux','lexer.py',935),
  ('punto_escritura_push -> <empty>','punto_escritura_push',0,'p_punto_escritura_push','lexer.py',939),
  ('punto_write_stack -> <empty>','punto_write_stack',0,'p_punto_write_stack','lexer.py',952),
  ('punto_add_write_operand -> <empty>','punto_add_write_operand',0,'p_punto_add_write_operand','lexer.py',959),
  ('decision -> IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp THEN LEFT_CURL estatutos RIGHT_CURL punto_end_if','decision',10,'p_decision','lexer.py',971),
  ('decision -> IF LEFT_PAR exp_or RIGHT_PAR punto_if_exp THEN LEFT_CURL estatutos RIGHT_CURL ELSE punto_else LEFT_CURL estatutos RIGHT_CURL punto_end_if','decision',15,'p_decision','lexer.py',972),
  ('punto_if_exp -> <empty>','punto_if_exp',0,'p_punto_if_exp','lexer.py',976),
  ('punto_else -> <empty>','punto_else',0,'p_punto_else','lexer.py',993),
  ('punto_end_if -> <empty>','punto_end_if',0,'p_punto_end_if','lexer.py',1006),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','lexer.py',1014),
  ('repeticion -> no_condicional','repeticion',1,'p_repeticion','lexer.py',1015),
  ('no_condicional -> FOR LEFT_PAR dec_varaux punto_for EQUALS m_exp punto_exp_for_inf TO m_exp punto_exp_for_sup RIGHT_PAR LEFT_CURL estatutos RIGHT_CURL punto_end_for','no_condicional',15,'p_no_condicional','lexer.py',1020),
  ('punto_for -> <empty>','punto_for',0,'p_punto_for','lexer.py',1025),
  ('punto_exp_for_inf -> <empty>','punto_exp_for_inf',0,'p_punto_exp_for_inf','lexer.py',1040),
  ('punto_exp_for_sup -> <empty>','punto_exp_for_sup',0,'p_punto_exp_for_sup','lexer.py',1060),
  ('punto_end_for -> <empty>','punto_end_for',0,'p_punto_end_for','lexer.py',1085),
  ('condicional -> WHILE punto_while LEFT_PAR exp_or RIGHT_PAR punto_validar_exp LEFT_CURL estatutos RIGHT_CURL punto_end_while','condicional',10,'p_condicional','lexer.py',1105),
  ('punto_while -> <empty>','punto_while',0,'p_punto_while','lexer.py',1110),
  ('punto_validar_exp -> <empty>','punto_validar_exp',0,'p_punto_validar_exp','lexer.py',1118),
  ('punto_end_while -> <empty>','punto_end_while',0,'p_punto_end_while','lexer.py',1135),
  ('cte -> ID factor_push_operand','cte',2,'p_cte','lexer.py',1151),
  ('cte -> CTE_I factor_int_push','cte',2,'p_cte','lexer.py',1152),
  ('cte -> cte_f factor_float_push','cte',2,'p_cte','lexer.py',1153),
  ('cte -> CTE_CHAR factor_char_push','cte',2,'p_cte','lexer.py',1154),
  ('factor_push_operand -> <empty>','factor_push_operand',0,'p_factor_push_operand','lexer.py',1160),
  ('factor_float_push -> <empty>','factor_float_push',0,'p_factor_float_push','lexer.py',1179),
  ('factor_int_push -> <empty>','factor_int_push',0,'p_factor_int_push','lexer.py',1192),
  ('factor_char_push -> <empty>','factor_char_push',0,'p_factor_char_push','lexer.py',1207),
  ('empty -> <empty>','empty',0,'p_empty','lexer.py',1226),
]
