from fca_lexer import FCALexer
import ply.yacc as yacc

class FCAGrammar:
    precedence = (
        ('left', 'CONCAT'),  # Adiciona concatenação como operador de maior precedência
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )
    #--------------------------------#
          # Inicializa o parser
    #--------------------------------#
    def __init__(self): 
        self.yacc = None
        self.lexer = None
        self.tokens = None

    #--------------------------------#
          # Constrói o parser
    #--------------------------------#

    def build(self, **kwargs):
        self.lexer = FCALexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = yacc.yacc(module=self, **kwargs)

    #------------------------------------------------#
        # Função para fazer o parsing de uma string
    #------------------------------------------------#
    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)
    
    #------------------------------------------------#
            # Regras de produção da gramática
    #------------------------------------------------#
    def p_lista_declaracoes(self, p):                                                   # Regra para lista de declarações
        """lista_declaracoes : declaracao                                                                          
                             | lista_declaracoes declaracao"""
        if len(p) == 2:                                                                 # Se houver apenas uma declaração
            p[0] = {'op': 'seq', 'args': [p[1]]}                                        # Retorna a declaração
        else:
            p[1]['args'].append(p[2])                                                   # Adiciona a declaração à lista de declarações
            p[0] = p[1]                                                                 # Retorna a lista de declarações

    #------------------------------------------------#
        # Regras de produção para declarações
    #------------------------------------------------#
    def p_declaracao(self, p):                                                          # Regra para declaração
        """declaracao : declaracao_atribuicao
                      | declaracao_expressao
                      | declaracao_funcao
                      | declaracao_funcao_literal
                      | declaracao_escrever
                      | declaracao_comentario
                      | declaracao_multiplas_atribuicoes"""
        p[0] = p[1]                                                                     # Retorna a declaração

    def p_declaracao_atribuicao(self, p):                                               # Regra para declaração de atribuição
        """declaracao_atribuicao : VARID '=' expressao ';'"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}                               # Retorna a declaração de atribuição

    def p_declaracao_expressao(self, p):                                                # Regra para declaração de expressão
        """declaracao_expressao : expressao ';'"""
        p[0] = p[1]                                                                     # Retorna a expressão

    def p_declaracao_funcao(self, p):                                                   # Regra para declaração de função
        """declaracao_funcao : FUNC VARID '(' parametros ')' ':' lista_declaracoes FIM 
                             | FUNC VARID '(' parametros ')' ',' ':' expressao ';'"""
        if len(p) == 9:                                                                 # Se a função tiver corpo
            p[0] = {'op': 'funcao', 'args': [p[2]], 'parametros': p[4], 'corpo': p[7]}  # Retorna a declaração de função
        else:
            p[0] = {'op': 'funcao', 'args': [p[2]], 'parametros': p[4], 'corpo': p[8]}  # Retorna a declaração de função

    def p_declaracao_funcao_literal(self, p):                                          # Regra para declaração de função com parâmetro literal
        """declaracao_funcao_literal : FUNC VARID '(' NUM ')' ',' ':' expressao ';'""" 
        p[0] = {'op': 'funcao', 'args': [p[2]], 'parametros': [{'op': 'literal', 'args': [p[4]]}], 'corpo': p[8]} 

    def p_declaracao_escrever(self, p):                                                # Regra para declaração de escrita
        """declaracao_escrever : PRINT '(' expressao ')' ';'"""
        p[0] = {'op': 'escrever', 'args': [p[3]]}                                      # Retorna a declaração de escrita

    def p_declaracao_comentario(self, p):                                              # Regra para declaração de comentário
        """declaracao_comentario : COMMENT_SINGLE_LINE
                                 | COMMENT_MULTI_LINE"""
        # Remove os delimitadores de comentário 
        if p.slice[1].type == 'COMMENT_SINGLE_LINE':
            p[0] = {'op': 'comentario', 'args': p[1][2:].strip()}                      # Retorna o comentário
        else:
            p[0] = {'op': 'comentario', 'args': p[1][2:-2].strip()} 

    def p_declaracao_multiplas_atribuicoes(self, p):                                   # Regra para declaração de múltiplas atribuições
        """declaracao_multiplas_atribuicoes : lista_atribuicoes ';'"""
        p[0] = {'op': 'seq', 'args': p[1]}                                             # Retorna a lista de atribuições

    #------------------------------------------------#
    # Regras de produção para interpolação de strings
    #------------------------------------------------#

    def processar_interpolacao(self, text):                                             # Função para processar interpolação de strings
        result = []                                                                     # Lista de partes da string
        i = 0                                                                           # Índice do caractere atual
        while i < len(text):                                                            # Percorre o texto caractere a caractere
            if text[i:i+2] == '#{':                                                     # Encontrou um '#{'
                j = i + 2                                                               # Avança para o próximo caractere
                while j < len(text) and text[j] != '}':                                 # Enquanto não encontrar um '}'
                    j += 1                                                              # Avança para o próximo caractere
                if j < len(text):                                                       # Encontrou um '}' correspondente
                    var_name = text[i+2:j]                                              # Extrai o nome da variável
                    result.append({'var': var_name})                                    # Adiciona a variável à lista de partes
                    i = j + 1                                                           # Avança para o próximo caractere
                else:                                                                   # Não encontrou um '}' correspondente
                    result.append({'op': 'literal', 'args': [text[i:]]})                # Adiciona o restante da string à lista de partes
                    break                                                               # Encerra o loop
            else:
                j = i
                while j < len(text) and text[j:j+2] != '#{':                            # Enquanto não encontrar um '#{'
                    j += 1                                                              # Avança para o próximo caractere
                result.append({'op': 'literal', 'args': [text[i:j]]})                   # Adiciona a parte da string à lista de partes
                i = j                                                                   # Avança para o próximo caractere
        return result                                                                   # Retorna a lista de partes da string    
    #------------------------------------------------#
         # Regras de produção para expressões
    #------------------------------------------------#
    def p_lista_atribuicoes(self, p):                                                   # Regra para lista de atribuições
        """lista_atribuicoes : atribuicao
                             | lista_atribuicoes ',' atribuicao"""
        if len(p) == 2:                                                                # Se houver apenas uma atribuição
            p[0] = [p[1]]                                                              # Retorna a atribuição
        else:                                                                          # Se houver mais de uma atribuição 
            p[1].append(p[3])                                                          # Adiciona a atribuição à lista de atribuições
            p[0] = p[1]                                                                # Retorna a lista de atribuições

    def p_atribuicao(self, p):                                                         # Regra para atribuição
        """atribuicao : VARID '=' expressao"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}                              # Retorna a atribuição

    def p_lista_expressoes(self, p):                                                  # Regra para lista de expressões
        """lista_expressoes : expressao
                            | lista_expressoes ',' expressao"""
        if len(p) == 2:                                                               # Se houver apenas uma expressão
            p[0] = [p[1]]                                                             # Retorna a expressão
        else:
            p[1].append(p[3])                                                        # Adiciona a expressão à lista de expressões
            p[0] = p[1]                                                              # Retorna a lista de expressões

    def p_expressao_concat(self, p):                                                 # Regra para expressão de concatenação
        """expressao : expressao CONCAT expressao"""
        p[0] = {'op': 'concat', 'args': [p[1], p[3]]}                                # Retorna a expressão de concatenação

    def p_expressao_string(self, p):                                                 # Regra para expressão de string
        """expressao : STRING"""
        partes = self.processar_interpolacao(p[1])                                   # Processa a interpolação de strings
        if len(partes) == 1:                                                         # Se houver apenas uma parte
            p[0] = partes[0]                                                         # Retorna a parte
        else:
            p[0] = {'op': 'interpolacao', 'args': partes}                            # Retorna a interpolação de strings

    def p_expressao_plus(self, p):                                                   # Regra para expressão de adição
        """expressao : expressao '+' expressao"""
        p[0] = {'op': '+', 'args': [p[1], p[3]]}                                     # Retorna a expressão de adição

    def p_expressao_minus(self, p):                                                  # Regra para expressão de subtração
        """expressao : expressao '-' expressao"""
        p[0] = {'op': '-', 'args': [p[1], p[3]]}                                     # Retorna a expressão de subtração

    def p_expressao_times(self, p):                                                  # Regra para expressão de multiplicação
        """expressao : expressao '*' expressao"""
        p[0] = {'op': '*', 'args': [p[1], p[3]]}                                     # Retorna a expressão de multiplicação

    def p_expressao_divide(self, p):                                                 # Regra para expressão de divisão
        """expressao : expressao '/' expressao"""
        p[0] = {'op': '/', 'args': [p[1], p[3]]}                                     # Retorna a expressão de divisão

    def p_expressao_group(self, p):                                                  # Regra para expressão de agrupamento
        """expressao : '(' expressao ')'"""
        p[0] = p[2]                                                                  # Retorna a expressão agrupada

    def p_expressao_uminus(self, p):                                                 # Regra para expressão de negação
        """expressao : '-' expressao %prec UMINUS""" 
        p[0] = {'op': 'uminus', 'args': [p[2]]}                                      # Retorna a expressão de negação

    def p_expressao_var_id(self, p):                                                 # Regra para expressão de variável
        """expressao : VARID"""
        p[0] = {'var': p[1]}                                                         # Retorna a variável

    def p_expressao_num(self, p):                                                    # Regra para expressão de número
        """expressao : NUM"""
        p[0] = {'op': 'literal', 'args': [p[1]]}                                     # Retorna o número

    def p_expressao_list(self, p):                                                   # Regra para expressão de lista
        """expressao : '[' ']' 
                     | '[' lista_expressoes ']'"""
        if len(p) == 3:                                                              # Se a lista estiver vazia
            p[0] = {'op': 'list', 'args': []}                                        # Retorna a lista vazia
        else:                                                                        # Se a lista não estiver vazia
            p[0] = {'op': 'list', 'args': p[2]}                                      # Retorna a lista

    #-----------------------------------------------------------------------#
     # Regras de produção para chamadas de funções, entrada e aleatório
    #----------------------------------------------------------------------#
    def p_expressao_chamada_funcao(self, p):                                         # Regra para chamada de função
        """expressao : VARID '(' lista_expressoes ')'
                     | ENTRADA '(' ')'
                     | ALEATORIO '(' expressao ')'"""
        if p.slice[1].type == 'VARID':                                               # Se for uma chamada de função
            p[0] = {'op': 'call_func', 'args': [p[1], p[3]]}                         # Retorna a chamada de função
        elif p.slice[1].type == 'ENTRADA':                                           # Se for uma chamada de entrada
            p[0] = {'op': 'entrada', 'args': []}                                     # Retorna a chamada de entrada
        elif p.slice[1].type == 'ALEATORIO':                                         # Se for uma chamada de aleatório
            p[0] = {'op': 'aleatorio', 'args': [p[3]]}                               # Retorna a chamada de aleatório

    #------------------------------------------------#
     # Regras de produção para funções MAP e FOLD
    #------------------------------------------------#

    def p_expressao_map(self, p):                                                  # Regra para expressão de mapeamento
        """expressao : MAP '(' VARID ',' expressao ')'"""
        p[0] = {'op': 'map', 'args': [p[3], p[5]]}                                 # Retorna a expressão de mapeamento

    def p_expressao_fold(self, p):                                                 # Regra para expressão de redução
        """expressao : FOLD '(' VARID ',' expressao ',' expressao ')'"""
        p[0] = {'op': 'fold', 'args': [p[3], p[5], p[7]]}                          # Retorna a expressão de redução

    #---------------------------------------------------#    
       # Regras de produção para parâmetros de funções
    #---------------------------------------------------#
    def p_parametros(self, p):                                                     # Regra para parâmetros
        """parametros : VARID
                      | parametros ',' VARID
                      | '[' ']' """
        if len(p) == 2:                                                            # Se houver apenas um parâmetro
            p[0] = [{'var': p[1]}]                                                 # Retorna o parâmetro
        elif len(p) == 3:                                                          # Se a lista de parâmetros estiver vazia
            p[0] = [{'op': 'array_vazio', 'args': []}]                             # Retorna a lista de parâmetros vazia
        else:
            p[1].append({'var': p[3]})                                             # Adiciona o parâmetro à lista de parâmetros
            p[0] = p[1]                                                            # Retorna a lista de parâmetros
            
    def p_parametro_id_array(self, p):                                             # Regra para parâmetro de array
        """parametros : VARID ':' VARID """
        p[0] = [{'op': 'var_array', 'args': [p[1], p[3]]}]                         # Retorna o parâmetro de array


    def p_error(self, p):                                                         # Função para tratamento de erros
        if p:
            print(f"Syntax error at '{p.value}'")                                 # Exibe a mensagem de erro
        else:
            print("Syntax error at EOF")
