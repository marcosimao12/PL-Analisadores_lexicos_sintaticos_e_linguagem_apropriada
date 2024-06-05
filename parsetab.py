
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftCONCATleft+-left*/rightUMINUSALEATORIO COLON COMMA COMMENT COMMENT_MULTI_LINE COMMENT_SINGLE_LINE CONCAT CONST DIVIDE END ENTRADA EQUALS FOLD FUNC INTERPOLATION LBRACKET LPAREN MAP MINUS NUM PLUS PRINT PROGRAM RBRACKET RPAREN SEMICOLON STRING TIMES VAR VARIDlista_declaracoes : declaracao\n                             | lista_declaracoes declaracaodeclaracao : declaracao_atribuicao\n                      | declaracao_expressao\n                      | declaracao_funcao\n                      | declaracao_funcao_literal\n                      | declaracao_escrever\n                      | declaracao_comentario\n                      | declaracao_multiplas_atribuicoesdeclaracao_atribuicao : VARID '=' expressao ';'declaracao_expressao : expressao ';'declaracao_funcao : FUNC VARID '(' parametros ')' ':' lista_declaracoes END \n                             | FUNC VARID '(' parametros ')' ',' ':' expressao ';'declaracao_funcao_literal : FUNC VARID '(' NUM ')' ',' ':' expressao ';'declaracao_escrever : PRINT '(' expressao ')' ';'declaracao_comentario : COMMENT_SINGLE_LINE\n                                 | COMMENT_MULTI_LINEdeclaracao_multiplas_atribuicoes : lista_atribuicoes ';'lista_atribuicoes : atribuicao\n                             | lista_atribuicoes ',' atribuicaoatribuicao : VARID '=' expressaolista_expressoes : expressao\n                            | lista_expressoes ',' expressaoexpressao : expressao CONCAT expressaoexpressao : STRINGexpressao : expressao '+' expressaoexpressao : expressao '-' expressaoexpressao : expressao '*' expressaoexpressao : expressao '/' expressaoexpressao : '(' expressao ')'expressao : '-' expressao %prec UMINUSexpressao : VARIDexpressao : NUMexpressao : '[' ']' \n                     | '[' lista_expressoes ']'expressao : VARID '(' lista_expressoes ')'\n                     | ENTRADA '(' ')'\n                     | ALEATORIO '(' expressao ')'expressao : MAP '(' VARID ',' expressao ')'expressao : FOLD '(' VARID ',' expressao ',' expressao ')'parametros : VARID\n                      | parametros ',' VARID\n                      | '[' ']' parametros : VARID ':' VARID "
    
_lr_action_items = {'VARID':([0,1,2,3,4,5,6,7,8,9,12,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,41,47,48,49,57,63,68,75,78,79,80,82,85,90,95,96,97,98,100,104,105,],[10,10,-1,-3,-4,-5,-6,-7,-8,-9,36,38,-16,-17,38,38,-2,38,38,-11,38,38,38,38,38,38,-18,61,38,66,67,70,38,-10,38,38,38,89,92,-15,10,38,10,38,38,-12,-13,-14,]),'FUNC':([0,1,2,3,4,5,6,7,8,9,16,17,27,30,40,68,85,90,96,100,104,105,],[12,12,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,12,12,-12,-13,-14,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,16,17,27,30,40,68,85,90,96,100,104,105,],[15,15,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,15,15,-12,-13,-14,]),'COMMENT_SINGLE_LINE':([0,1,2,3,4,5,6,7,8,9,16,17,27,30,40,68,85,90,96,100,104,105,],[16,16,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,16,16,-12,-13,-14,]),'COMMENT_MULTI_LINE':([0,1,2,3,4,5,6,7,8,9,16,17,27,30,40,68,85,90,96,100,104,105,],[17,17,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,17,17,-12,-13,-14,]),'STRING':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[19,19,-1,-3,-4,-5,-6,-7,-8,-9,19,-16,-17,19,19,-2,19,19,-11,19,19,19,19,19,19,-18,19,19,-10,19,19,19,-15,19,19,19,19,19,-12,-13,-14,]),'(':([0,1,2,3,4,5,6,7,8,9,10,13,15,16,17,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,38,39,40,47,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[13,13,-1,-3,-4,-5,-6,-7,-8,-9,29,13,39,-16,-17,13,13,46,47,48,49,-2,13,13,-11,13,13,13,13,13,57,29,13,-18,13,13,-10,13,13,13,-15,13,13,13,13,13,-12,-13,-14,]),'-':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,16,17,19,20,21,27,28,29,30,31,32,33,34,35,37,38,39,40,42,43,45,47,50,52,53,54,55,56,58,59,62,63,64,65,68,69,75,76,77,78,79,85,86,87,88,90,94,95,96,97,98,99,100,101,102,103,104,105,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-32,33,20,-33,-16,-17,-25,20,20,-2,20,20,-11,20,20,20,20,20,33,-32,20,-18,-31,-34,33,20,33,33,-26,-27,-28,-29,-30,33,-35,20,-37,33,-10,-36,20,33,-38,20,20,-15,33,33,33,20,-39,20,20,20,20,33,-12,33,33,-40,-13,-14,]),'NUM':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,57,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[14,14,-1,-3,-4,-5,-6,-7,-8,-9,14,-16,-17,14,14,-2,14,14,-11,14,14,14,14,14,14,-18,14,72,14,-10,14,14,14,-15,14,14,14,14,14,-12,-13,-14,]),'[':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,57,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[21,21,-1,-3,-4,-5,-6,-7,-8,-9,21,-16,-17,21,21,-2,21,21,-11,21,21,21,21,21,21,-18,21,73,21,-10,21,21,21,-15,21,21,21,21,21,-12,-13,-14,]),'ENTRADA':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[22,22,-1,-3,-4,-5,-6,-7,-8,-9,22,-16,-17,22,22,-2,22,22,-11,22,22,22,22,22,22,-18,22,22,-10,22,22,22,-15,22,22,22,22,22,-12,-13,-14,]),'ALEATORIO':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,23,-16,-17,23,23,-2,23,23,-11,23,23,23,23,23,23,-18,23,23,-10,23,23,23,-15,23,23,23,23,23,-12,-13,-14,]),'MAP':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,24,-16,-17,24,24,-2,24,24,-11,24,24,24,24,24,24,-18,24,24,-10,24,24,24,-15,24,24,24,24,24,-12,-13,-14,]),'FOLD':([0,1,2,3,4,5,6,7,8,9,13,16,17,20,21,27,28,29,30,31,32,33,34,35,39,40,47,63,68,75,78,79,85,90,95,96,97,98,100,104,105,],[25,25,-1,-3,-4,-5,-6,-7,-8,-9,25,-16,-17,25,25,-2,25,25,-11,25,25,25,25,25,25,-18,25,25,-10,25,25,25,-15,25,25,25,25,25,-12,-13,-14,]),'$end':([1,2,3,4,5,6,7,8,9,16,17,27,30,40,68,85,100,104,105,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,-12,-13,-14,]),'END':([2,3,4,5,6,7,8,9,16,17,27,30,40,68,85,96,100,104,105,],[-1,-3,-4,-5,-6,-7,-8,-9,-16,-17,-2,-11,-18,-10,-15,100,-12,-13,-14,]),'=':([10,61,],[28,75,]),';':([10,11,14,18,19,26,38,42,43,50,52,53,54,55,56,58,60,62,64,69,74,77,86,94,101,102,103,],[-32,30,-33,40,-25,-19,-32,-31,-34,68,-24,-26,-27,-28,-29,-30,-20,-35,-37,-36,85,-38,-21,-39,104,105,-40,]),'CONCAT':([10,11,14,19,37,38,42,43,45,50,52,53,54,55,56,58,59,62,64,65,69,76,77,86,87,88,94,99,101,102,103,],[-32,31,-33,-25,31,-32,-31,-34,31,31,-24,-26,-27,-28,-29,-30,31,-35,-37,31,-36,31,-38,31,31,31,-39,31,31,31,-40,]),'+':([10,11,14,19,37,38,42,43,45,50,52,53,54,55,56,58,59,62,64,65,69,76,77,86,87,88,94,99,101,102,103,],[-32,32,-33,-25,32,-32,-31,-34,32,32,32,-26,-27,-28,-29,-30,32,-35,-37,32,-36,32,-38,32,32,32,-39,32,32,32,-40,]),'*':([10,11,14,19,37,38,42,43,45,50,52,53,54,55,56,58,59,62,64,65,69,76,77,86,87,88,94,99,101,102,103,],[-32,34,-33,-25,34,-32,-31,-34,34,34,34,34,34,-28,-29,-30,34,-35,-37,34,-36,34,-38,34,34,34,-39,34,34,34,-40,]),'/':([10,11,14,19,37,38,42,43,45,50,52,53,54,55,56,58,59,62,64,65,69,76,77,86,87,88,94,99,101,102,103,],[-32,35,-33,-25,35,-32,-31,-34,35,35,35,35,35,-28,-29,-30,35,-35,-37,35,-36,35,-38,35,35,35,-39,35,35,35,-40,]),')':([14,19,37,38,42,43,45,46,51,52,53,54,55,56,58,59,62,64,65,69,70,71,72,76,77,84,87,89,92,94,99,103,],[-33,-25,58,-32,-31,-34,-22,64,69,-24,-26,-27,-28,-29,-30,74,-35,-37,77,-36,-41,81,83,-23,-38,-43,94,-44,-42,-39,103,-40,]),']':([14,19,21,38,42,43,44,45,52,53,54,55,56,58,62,64,69,73,76,77,94,103,],[-33,-25,43,-32,-31,-34,62,-22,-24,-26,-27,-28,-29,-30,-35,-37,-36,84,-23,-38,-39,-40,]),',':([14,18,19,26,38,42,43,44,45,50,51,52,53,54,55,56,58,60,62,64,66,67,69,70,71,76,77,81,83,84,86,88,89,92,94,103,],[-33,41,-25,-19,-32,-31,-34,63,-22,-21,63,-24,-26,-27,-28,-29,-30,-20,-35,-37,78,79,-36,-41,82,-23,-38,91,93,-43,-21,95,-44,-42,-39,-40,]),':':([70,81,91,93,],[80,90,97,98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista_declaracoes':([0,90,],[1,96,]),'declaracao':([0,1,90,96,],[2,27,2,27,]),'declaracao_atribuicao':([0,1,90,96,],[3,3,3,3,]),'declaracao_expressao':([0,1,90,96,],[4,4,4,4,]),'declaracao_funcao':([0,1,90,96,],[5,5,5,5,]),'declaracao_funcao_literal':([0,1,90,96,],[6,6,6,6,]),'declaracao_escrever':([0,1,90,96,],[7,7,7,7,]),'declaracao_comentario':([0,1,90,96,],[8,8,8,8,]),'declaracao_multiplas_atribuicoes':([0,1,90,96,],[9,9,9,9,]),'expressao':([0,1,13,20,21,28,29,31,32,33,34,35,39,47,63,75,78,79,90,95,96,97,98,],[11,11,37,42,45,50,45,52,53,54,55,56,59,65,76,86,87,88,11,99,11,101,102,]),'lista_atribuicoes':([0,1,90,96,],[18,18,18,18,]),'atribuicao':([0,1,41,90,96,],[26,26,60,26,26,]),'lista_expressoes':([21,29,],[44,51,]),'parametros':([57,],[71,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista_declaracoes","S'",1,None,None,None),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','fca_grammar.py',53),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','fca_grammar.py',54),
  ('declaracao -> declaracao_atribuicao','declaracao',1,'p_declaracao','fca_grammar.py',62),
  ('declaracao -> declaracao_expressao','declaracao',1,'p_declaracao','fca_grammar.py',63),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','fca_grammar.py',64),
  ('declaracao -> declaracao_funcao_literal','declaracao',1,'p_declaracao','fca_grammar.py',65),
  ('declaracao -> declaracao_escrever','declaracao',1,'p_declaracao','fca_grammar.py',66),
  ('declaracao -> declaracao_comentario','declaracao',1,'p_declaracao','fca_grammar.py',67),
  ('declaracao -> declaracao_multiplas_atribuicoes','declaracao',1,'p_declaracao','fca_grammar.py',68),
  ('declaracao_atribuicao -> VARID = expressao ;','declaracao_atribuicao',4,'p_declaracao_atribuicao','fca_grammar.py',72),
  ('declaracao_expressao -> expressao ;','declaracao_expressao',2,'p_declaracao_expressao','fca_grammar.py',76),
  ('declaracao_funcao -> FUNC VARID ( parametros ) : lista_declaracoes END','declaracao_funcao',8,'p_declaracao_funcao','fca_grammar.py',80),
  ('declaracao_funcao -> FUNC VARID ( parametros ) , : expressao ;','declaracao_funcao',9,'p_declaracao_funcao','fca_grammar.py',81),
  ('declaracao_funcao_literal -> FUNC VARID ( NUM ) , : expressao ;','declaracao_funcao_literal',9,'p_declaracao_funcao_literal','fca_grammar.py',88),
  ('declaracao_escrever -> PRINT ( expressao ) ;','declaracao_escrever',5,'p_declaracao_escrever','fca_grammar.py',92),
  ('declaracao_comentario -> COMMENT_SINGLE_LINE','declaracao_comentario',1,'p_declaracao_comentario','fca_grammar.py',96),
  ('declaracao_comentario -> COMMENT_MULTI_LINE','declaracao_comentario',1,'p_declaracao_comentario','fca_grammar.py',97),
  ('declaracao_multiplas_atribuicoes -> lista_atribuicoes ;','declaracao_multiplas_atribuicoes',2,'p_declaracao_multiplas_atribuicoes','fca_grammar.py',105),
  ('lista_atribuicoes -> atribuicao','lista_atribuicoes',1,'p_lista_atribuicoes','fca_grammar.py',109),
  ('lista_atribuicoes -> lista_atribuicoes , atribuicao','lista_atribuicoes',3,'p_lista_atribuicoes','fca_grammar.py',110),
  ('atribuicao -> VARID = expressao','atribuicao',3,'p_atribuicao','fca_grammar.py',118),
  ('lista_expressoes -> expressao','lista_expressoes',1,'p_lista_expressoes','fca_grammar.py',122),
  ('lista_expressoes -> lista_expressoes , expressao','lista_expressoes',3,'p_lista_expressoes','fca_grammar.py',123),
  ('expressao -> expressao CONCAT expressao','expressao',3,'p_expressao_concat','fca_grammar.py',132),
  ('expressao -> STRING','expressao',1,'p_expressao_string','fca_grammar.py',136),
  ('expressao -> expressao + expressao','expressao',3,'p_expressao_plus','fca_grammar.py',144),
  ('expressao -> expressao - expressao','expressao',3,'p_expressao_minus','fca_grammar.py',148),
  ('expressao -> expressao * expressao','expressao',3,'p_expressao_times','fca_grammar.py',152),
  ('expressao -> expressao / expressao','expressao',3,'p_expressao_divide','fca_grammar.py',156),
  ('expressao -> ( expressao )','expressao',3,'p_expressao_group','fca_grammar.py',160),
  ('expressao -> - expressao','expressao',2,'p_expressao_uminus','fca_grammar.py',164),
  ('expressao -> VARID','expressao',1,'p_expressao_var_id','fca_grammar.py',168),
  ('expressao -> NUM','expressao',1,'p_expressao_num','fca_grammar.py',172),
  ('expressao -> [ ]','expressao',2,'p_expressao_list','fca_grammar.py',176),
  ('expressao -> [ lista_expressoes ]','expressao',3,'p_expressao_list','fca_grammar.py',177),
  ('expressao -> VARID ( lista_expressoes )','expressao',4,'p_expressao_chamada_funcao','fca_grammar.py',184),
  ('expressao -> ENTRADA ( )','expressao',3,'p_expressao_chamada_funcao','fca_grammar.py',185),
  ('expressao -> ALEATORIO ( expressao )','expressao',4,'p_expressao_chamada_funcao','fca_grammar.py',186),
  ('expressao -> MAP ( VARID , expressao )','expressao',6,'p_expressao_map','fca_grammar.py',195),
  ('expressao -> FOLD ( VARID , expressao , expressao )','expressao',8,'p_expressao_fold','fca_grammar.py',199),
  ('parametros -> VARID','parametros',1,'p_parametros','fca_grammar.py',203),
  ('parametros -> parametros , VARID','parametros',3,'p_parametros','fca_grammar.py',204),
  ('parametros -> [ ]','parametros',2,'p_parametros','fca_grammar.py',205),
  ('parametros -> VARID : VARID','parametros',3,'p_parametro_id_array','fca_grammar.py',215),
]
