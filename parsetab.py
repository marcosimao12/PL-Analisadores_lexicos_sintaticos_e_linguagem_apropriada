
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftCONCATleft+-left*/rightUMINUSCOLON COMMA COMMENT COMMENT_MULTI_LINE COMMENT_SINGLE_LINE CONCAT CONST DIVIDE END EQUALS FOLD FUNC INPUT INTERPOLATION LBRACKET LPAREN MAP MINUS NUM PLUS PRINT PROGRAM RANDOM RBRACKET RPAREN SEMICOLON STRING TIMES VAR VARIDlista_declaracoes : declaracao\n                             | lista_declaracoes declaracaodeclaracao : declaracao_atribuicao\n                      | declaracao_expressao\n                      | declaracao_funcao\n                      | declaracao_funcao_literal\n                      | declaracao_escrever\n                      | declaracao_comentario\n                      | declaracao_multiplas_atribuicoesdeclaracao_atribuicao : VARID '=' expressao ';'declaracao_expressao : expressao ';'declaracao_funcao : FUNC VARID '(' parametros ')' ':' lista_declaracoes END\n                             | FUNC VARID '(' parametros ')' ',' ':' expressao ';'declaracao_funcao_literal : FUNC VARID '(' NUM ')' ',' ':' expressao ';'declaracao_escrever : PRINT '(' expressao ')' ';'declaracao_comentario : COMMENT_SINGLE_LINE\n                                 | COMMENT_MULTI_LINEdeclaracao_multiplas_atribuicoes : lista_atribuicoes ';'lista_atribuicoes : atribuicao\n                             | lista_atribuicoes ',' atribuicaoatribuicao : VARID '=' expressaolista_expressoes : expressao\n                            | lista_expressoes ',' expressaoexpressao : expressao CONCAT expressaoexpressao : interpolacao_partesinterpolacao_partes : interpolacao_partes interpolacao_part\n                               | interpolacao_partinterpolacao_part : STRING\n                             | INTERPOLATIONexpressao : expressao '+' expressaoexpressao : expressao '-' expressaoexpressao : expressao '*' expressaoexpressao : expressao '/' expressaoexpressao : '(' expressao ')'expressao : '-' expressao %prec UMINUSexpressao : VARIDexpressao : NUMexpressao : STRINGexpressao : '[' ']' \n                     | '[' lista_expressoes ']'expressao : VARID '(' lista_expressoes ')'expressao : MAP '(' VARID ',' expressao ')'expressao : FOLD '(' VARID ',' expressao ',' expressao ')'parametros : VARID\n                      | parametros ',' VARID\n                      | '[' ']'\n                      | VARID ':' VARID '[' ']'"
    
_lr_action_items = {'VARID':([0,1,2,3,4,5,6,7,8,9,12,13,16,17,20,22,28,29,30,31,32,33,34,35,36,40,41,42,49,50,58,64,67,74,76,77,78,80,83,88,93,95,96,97,100,104,105,],[10,10,-1,-3,-4,-5,-6,-7,-8,-9,37,39,-16,-17,39,39,-2,39,39,-11,39,39,39,39,39,39,-18,62,65,66,69,39,-10,39,39,39,87,90,-15,10,39,10,39,39,-12,-13,-14,]),'FUNC':([0,1,2,3,4,5,6,7,8,9,16,17,28,31,41,67,83,88,95,100,104,105,],[12,12,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,12,12,-12,-13,-14,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,16,17,28,31,41,67,83,88,95,100,104,105,],[15,15,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,15,15,-12,-13,-14,]),'COMMENT_SINGLE_LINE':([0,1,2,3,4,5,6,7,8,9,16,17,28,31,41,67,83,88,95,100,104,105,],[16,16,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,16,16,-12,-13,-14,]),'COMMENT_MULTI_LINE':([0,1,2,3,4,5,6,7,8,9,16,17,28,31,41,67,83,88,95,100,104,105,],[17,17,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,17,17,-12,-13,-14,]),'(':([0,1,2,3,4,5,6,7,8,9,10,13,15,16,17,20,22,23,24,28,29,30,31,32,33,34,35,36,37,39,40,41,64,67,74,76,77,83,88,93,95,96,97,100,104,105,],[13,13,-1,-3,-4,-5,-6,-7,-8,-9,30,13,40,-16,-17,13,13,49,50,-2,13,13,-11,13,13,13,13,13,58,30,13,-18,13,-10,13,13,13,-15,13,13,13,13,13,-12,-13,-14,]),'-':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,16,17,19,20,21,22,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,43,44,45,46,48,51,53,54,55,56,57,59,60,63,64,67,68,74,75,76,77,83,84,85,86,88,92,93,95,96,97,98,100,101,102,103,104,105,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-36,34,20,-37,-16,-17,-25,20,-28,20,-27,-29,-2,20,20,-11,20,20,20,20,20,34,-36,20,-18,-26,-28,-35,-39,34,34,34,-30,-31,-32,-33,-34,34,-40,20,-10,-41,20,34,20,20,-15,34,34,34,20,-42,20,20,20,20,34,-12,34,34,-43,-13,-14,]),'NUM':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,22,28,29,30,31,32,33,34,35,36,40,41,58,64,67,74,76,77,83,88,93,95,96,97,100,104,105,],[14,14,-1,-3,-4,-5,-6,-7,-8,-9,14,-16,-17,14,14,-2,14,14,-11,14,14,14,14,14,14,-18,71,14,-10,14,14,14,-15,14,14,14,14,14,-12,-13,-14,]),'STRING':([0,1,2,3,4,5,6,7,8,9,13,16,17,19,20,21,22,26,27,28,29,30,31,32,33,34,35,36,40,41,43,44,64,67,74,76,77,83,88,93,95,96,97,100,104,105,],[21,21,-1,-3,-4,-5,-6,-7,-8,-9,21,-16,-17,44,21,-28,21,-27,-29,-2,21,21,-11,21,21,21,21,21,21,-18,-26,-28,21,-10,21,21,21,-15,21,21,21,21,21,-12,-13,-14,]),'[':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,22,28,29,30,31,32,33,34,35,36,40,41,58,64,67,74,76,77,83,87,88,93,95,96,97,100,104,105,],[22,22,-1,-3,-4,-5,-6,-7,-8,-9,22,-16,-17,22,22,-2,22,22,-11,22,22,22,22,22,22,-18,72,22,-10,22,22,22,-15,94,22,22,22,22,22,-12,-13,-14,]),'MAP':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,22,28,29,30,31,32,33,34,35,36,40,41,64,67,74,76,77,83,88,93,95,96,97,100,104,105,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,23,-16,-17,23,23,-2,23,23,-11,23,23,23,23,23,23,-18,23,-10,23,23,23,-15,23,23,23,23,23,-12,-13,-14,]),'FOLD':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,22,28,29,30,31,32,33,34,35,36,40,41,64,67,74,76,77,83,88,93,95,96,97,100,104,105,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,24,-16,-17,24,24,-2,24,24,-11,24,24,24,24,24,24,-18,24,-10,24,24,24,-15,24,24,24,24,24,-12,-13,-14,]),'INTERPOLATION':([0,1,2,3,4,5,6,7,8,9,13,16,17,19,20,21,22,26,27,28,29,30,31,32,33,34,35,36,40,41,43,44,64,67,74,76,77,83,88,93,95,96,97,100,104,105,],[27,27,-1,-3,-4,-5,-6,-7,-8,-9,27,-16,-17,27,27,-28,27,-27,-29,-2,27,27,-11,27,27,27,27,27,27,-18,-26,-28,27,-10,27,27,27,-15,27,27,27,27,27,-12,-13,-14,]),'$end':([1,2,3,4,5,6,7,8,9,16,17,28,31,41,67,83,100,104,105,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,-12,-13,-14,]),'END':([2,3,4,5,6,7,8,9,16,17,28,31,41,67,83,95,100,104,105,],[-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,100,-12,-13,-14,]),'=':([10,62,],[29,74,]),';':([10,11,14,18,19,21,25,26,27,39,43,44,45,46,51,53,54,55,56,57,59,61,63,68,73,84,92,101,102,103,],[-36,31,-37,41,-25,-28,-19,-27,-29,-36,-26,-28,-35,-39,67,-24,-30,-31,-32,-33,-34,-20,-40,-41,83,-21,-42,104,105,-43,]),'CONCAT':([10,11,14,19,21,26,27,38,39,43,44,45,46,48,51,53,54,55,56,57,59,60,63,68,75,84,85,86,92,98,101,102,103,],[-36,32,-37,-25,-28,-27,-29,32,-36,-26,-28,-35,-39,32,32,-24,-30,-31,-32,-33,-34,32,-40,-41,32,32,32,32,-42,32,32,32,-43,]),'+':([10,11,14,19,21,26,27,38,39,43,44,45,46,48,51,53,54,55,56,57,59,60,63,68,75,84,85,86,92,98,101,102,103,],[-36,33,-37,-25,-28,-27,-29,33,-36,-26,-28,-35,-39,33,33,33,-30,-31,-32,-33,-34,33,-40,-41,33,33,33,33,-42,33,33,33,-43,]),'*':([10,11,14,19,21,26,27,38,39,43,44,45,46,48,51,53,54,55,56,57,59,60,63,68,75,84,85,86,92,98,101,102,103,],[-36,35,-37,-25,-28,-27,-29,35,-36,-26,-28,-35,-39,35,35,35,35,35,-32,-33,-34,35,-40,-41,35,35,35,35,-42,35,35,35,-43,]),'/':([10,11,14,19,21,26,27,38,39,43,44,45,46,48,51,53,54,55,56,57,59,60,63,68,75,84,85,86,92,98,101,102,103,],[-36,36,-37,-25,-28,-27,-29,36,-36,-26,-28,-35,-39,36,36,36,36,36,-32,-33,-34,36,-40,-41,36,36,36,36,-42,36,36,36,-43,]),')':([14,19,21,26,27,38,39,43,44,45,46,48,52,53,54,55,56,57,59,60,63,68,69,70,71,75,82,85,90,92,98,99,103,],[-37,-25,-28,-27,-29,59,-36,-26,-28,-35,-39,-22,68,-24,-30,-31,-32,-33,-34,73,-40,-41,-44,79,81,-23,-46,92,-45,-42,103,-47,-43,]),']':([14,19,21,22,26,27,39,43,44,45,46,47,48,53,54,55,56,57,59,63,68,72,75,92,94,103,],[-37,-25,-28,46,-27,-29,-36,-26,-28,-35,-39,63,-22,-24,-30,-31,-32,-33,-34,-40,-41,82,-23,-42,99,-43,]),',':([14,18,19,21,25,26,27,39,43,44,45,46,47,48,51,52,53,54,55,56,57,59,61,63,65,66,68,69,70,75,79,81,82,84,86,90,92,99,103,],[-37,42,-25,-28,-19,-27,-29,-36,-26,-28,-35,-39,64,-22,-21,64,-24,-30,-31,-32,-33,-34,-20,-40,76,77,-41,-44,80,-23,89,91,-46,-21,93,-45,-42,-47,-43,]),':':([69,79,89,91,],[78,88,96,97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista_declaracoes':([0,88,],[1,95,]),'declaracao':([0,1,88,95,],[2,28,2,28,]),'declaracao_atribuicao':([0,1,88,95,],[3,3,3,3,]),'declaracao_expressao':([0,1,88,95,],[4,4,4,4,]),'declaracao_funcao':([0,1,88,95,],[5,5,5,5,]),'declaracao_funcao_literal':([0,1,88,95,],[6,6,6,6,]),'declaracao_escrever':([0,1,88,95,],[7,7,7,7,]),'declaracao_comentario':([0,1,88,95,],[8,8,8,8,]),'declaracao_multiplas_atribuicoes':([0,1,88,95,],[9,9,9,9,]),'expressao':([0,1,13,20,22,29,30,32,33,34,35,36,40,64,74,76,77,88,93,95,96,97,],[11,11,38,45,48,51,48,53,54,55,56,57,60,75,84,85,86,11,98,11,101,102,]),'lista_atribuicoes':([0,1,88,95,],[18,18,18,18,]),'interpolacao_partes':([0,1,13,20,22,29,30,32,33,34,35,36,40,64,74,76,77,88,93,95,96,97,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'atribuicao':([0,1,42,88,95,],[25,25,61,25,25,]),'interpolacao_part':([0,1,13,19,20,22,29,30,32,33,34,35,36,40,64,74,76,77,88,93,95,96,97,],[26,26,26,43,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'lista_expressoes':([22,30,],[47,52,]),'parametros':([58,],[70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista_declaracoes","S'",1,None,None,None),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','fca_grammar.py',30),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','fca_grammar.py',31),
  ('declaracao -> declaracao_atribuicao','declaracao',1,'p_declaracao','fca_grammar.py',39),
  ('declaracao -> declaracao_expressao','declaracao',1,'p_declaracao','fca_grammar.py',40),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','fca_grammar.py',41),
  ('declaracao -> declaracao_funcao_literal','declaracao',1,'p_declaracao','fca_grammar.py',42),
  ('declaracao -> declaracao_escrever','declaracao',1,'p_declaracao','fca_grammar.py',43),
  ('declaracao -> declaracao_comentario','declaracao',1,'p_declaracao','fca_grammar.py',44),
  ('declaracao -> declaracao_multiplas_atribuicoes','declaracao',1,'p_declaracao','fca_grammar.py',45),
  ('declaracao_atribuicao -> VARID = expressao ;','declaracao_atribuicao',4,'p_declaracao_atribuicao','fca_grammar.py',49),
  ('declaracao_expressao -> expressao ;','declaracao_expressao',2,'p_declaracao_expressao','fca_grammar.py',53),
  ('declaracao_funcao -> FUNC VARID ( parametros ) : lista_declaracoes END','declaracao_funcao',8,'p_declaracao_funcao','fca_grammar.py',57),
  ('declaracao_funcao -> FUNC VARID ( parametros ) , : expressao ;','declaracao_funcao',9,'p_declaracao_funcao','fca_grammar.py',58),
  ('declaracao_funcao_literal -> FUNC VARID ( NUM ) , : expressao ;','declaracao_funcao_literal',9,'p_declaracao_funcao_literal','fca_grammar.py',65),
  ('declaracao_escrever -> PRINT ( expressao ) ;','declaracao_escrever',5,'p_declaracao_escrever','fca_grammar.py',69),
  ('declaracao_comentario -> COMMENT_SINGLE_LINE','declaracao_comentario',1,'p_declaracao_comentario','fca_grammar.py',73),
  ('declaracao_comentario -> COMMENT_MULTI_LINE','declaracao_comentario',1,'p_declaracao_comentario','fca_grammar.py',74),
  ('declaracao_multiplas_atribuicoes -> lista_atribuicoes ;','declaracao_multiplas_atribuicoes',2,'p_declaracao_multiplas_atribuicoes','fca_grammar.py',82),
  ('lista_atribuicoes -> atribuicao','lista_atribuicoes',1,'p_lista_atribuicoes','fca_grammar.py',86),
  ('lista_atribuicoes -> lista_atribuicoes , atribuicao','lista_atribuicoes',3,'p_lista_atribuicoes','fca_grammar.py',87),
  ('atribuicao -> VARID = expressao','atribuicao',3,'p_atribuicao','fca_grammar.py',95),
  ('lista_expressoes -> expressao','lista_expressoes',1,'p_lista_expressoes','fca_grammar.py',99),
  ('lista_expressoes -> lista_expressoes , expressao','lista_expressoes',3,'p_lista_expressoes','fca_grammar.py',100),
  ('expressao -> expressao CONCAT expressao','expressao',3,'p_expressao_concat','fca_grammar.py',109),
  ('expressao -> interpolacao_partes','expressao',1,'p_expressao_interpolacao','fca_grammar.py',114),
  ('interpolacao_partes -> interpolacao_partes interpolacao_part','interpolacao_partes',2,'p_interpolacao_partes','fca_grammar.py',121),
  ('interpolacao_partes -> interpolacao_part','interpolacao_partes',1,'p_interpolacao_partes','fca_grammar.py',122),
  ('interpolacao_part -> STRING','interpolacao_part',1,'p_interpolacao_part','fca_grammar.py',129),
  ('interpolacao_part -> INTERPOLATION','interpolacao_part',1,'p_interpolacao_part','fca_grammar.py',130),
  ('expressao -> expressao + expressao','expressao',3,'p_expressao_plus','fca_grammar.py',137),
  ('expressao -> expressao - expressao','expressao',3,'p_expressao_minus','fca_grammar.py',141),
  ('expressao -> expressao * expressao','expressao',3,'p_expressao_times','fca_grammar.py',145),
  ('expressao -> expressao / expressao','expressao',3,'p_expressao_divide','fca_grammar.py',149),
  ('expressao -> ( expressao )','expressao',3,'p_expressao_group','fca_grammar.py',153),
  ('expressao -> - expressao','expressao',2,'p_expressao_uminus','fca_grammar.py',157),
  ('expressao -> VARID','expressao',1,'p_expressao_var_id','fca_grammar.py',161),
  ('expressao -> NUM','expressao',1,'p_expressao_num','fca_grammar.py',165),
  ('expressao -> STRING','expressao',1,'p_expressao_string','fca_grammar.py',169),
  ('expressao -> [ ]','expressao',2,'p_expressao_list','fca_grammar.py',173),
  ('expressao -> [ lista_expressoes ]','expressao',3,'p_expressao_list','fca_grammar.py',174),
  ('expressao -> VARID ( lista_expressoes )','expressao',4,'p_expressao_chamada_funcao','fca_grammar.py',181),
  ('expressao -> MAP ( VARID , expressao )','expressao',6,'p_expressao_map','fca_grammar.py',185),
  ('expressao -> FOLD ( VARID , expressao , expressao )','expressao',8,'p_expressao_fold','fca_grammar.py',189),
  ('parametros -> VARID','parametros',1,'p_parametros','fca_grammar.py',193),
  ('parametros -> parametros , VARID','parametros',3,'p_parametros','fca_grammar.py',194),
  ('parametros -> [ ]','parametros',2,'p_parametros','fca_grammar.py',195),
  ('parametros -> VARID : VARID [ ]','parametros',5,'p_parametros','fca_grammar.py',196),
]
