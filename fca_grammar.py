from fca_lexer import FCALexer
import ply.yacc as yacc

class FCAGrammar:
    precedence = (
        ('left', 'CONCAT'),  # Adiciona concatenação como operador de maior precedência
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None 

    def build(self, **kwargs): # Função para criar o analisador sintático
        self.lexer = FCALexer() # Cria o analisador léxico
        self.lexer.build(**kwargs) # Cria o analisador léxico
        self.tokens = self.lexer.tokens # Obtém a lista de tokens do analisador léxico
        self.yacc = yacc.yacc(module=self, **kwargs) # Cria o analisador sintático
 
    def parse(self, string):  # Função para analisar a string
        self.lexer.input(string)  # Define a string de entrada
        return self.yacc.parse(lexer=self.lexer.lexer)  # Chama o analisador sintático

    def processar_interpolacao(self, text): # Função para processar a interpolação de strings
        result = [] # Inicializa a lista de partes da string
        i = 0 # Inicializa o índice
        while i < len(text): # Enquanto não chegar ao fim do texto
            if text[i:i+2] == '#{': # Encontrou uma variável
                j = i + 2
                while j < len(text) and text[j] != '}': # Enquanto não encontrar um '}'
                    j += 1
                if j < len(text):  # Encontrou um '}' correspondente
                    var_name = text[i+2:j] # Extrai o nome da variável
                    result.append({'var': var_name}) # Adiciona a variável
                    i = j + 1
                else:  # Não encontrou um '}' correspondente
                    result.append({'op': 'literal', 'args': [text[i:]]}) # Adiciona o restante do texto
                    break
            else:
                j = i
                while j < len(text) and text[j:j+2] != '#{': # Enquanto não encontrar uma variável
                    j += 1  # Avança
                result.append({'op': 'literal', 'args': [text[i:j]]}) # Adiciona a parte literal
                i = j
        return result

    # Regras de produção da gramática

    def p_lista_declaracoes(self, p):
        """lista_declaracoes : declaracao
                             | lista_declaracoes declaracao"""
        if len(p) == 2:
            p[0] = {'op': 'seq', 'args': [p[1]]}
        else:
            p[1]['args'].append(p[2])
            p[0] = p[1]

    def p_declaracao(self, p):
        """declaracao : declaracao_atribuicao
                      | declaracao_expressao
                      | declaracao_funcao
                      | declaracao_funcao_literal
                      | declaracao_escrever
                      | declaracao_comentario
                      | declaracao_multiplas_atribuicoes"""
        p[0] = p[1]

    def p_declaracao_atribuicao(self, p): 
        """declaracao_atribuicao : VARID '=' expressao ';'""" # Regra de atribuição
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]} # Cria um nó de atribuição

    def p_declaracao_expressao(self, p):
        """declaracao_expressao : expressao ';'"""
        p[0] = p[1]

    def p_declaracao_funcao(self, p):
        """declaracao_funcao : FUNC VARID '(' parametros ')' ':' lista_declaracoes END
                             | FUNC VARID '(' parametros ')' ',' ':' expressao ';'"""
        if len(p) == 9:
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[7]]}
        else:
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], [p[8]]]}

    def p_declaracao_funcao_literal(self, p):
        """declaracao_funcao_literal : FUNC VARID '(' NUM ')' ',' ':' expressao ';'"""
        p[0] = {'op': 'funcao', 'args': [p[2], [p[4]], p[8]]}

    def p_declaracao_escrever(self, p):
        """declaracao_escrever : PRINT '(' expressao ')' ';'"""
        p[0] = {'op': 'escrever', 'args': [p[3]]}

    def p_declaracao_comentario(self, p):
        """declaracao_comentario : COMMENT_SINGLE_LINE
                                 | COMMENT_MULTI_LINE"""
        # Remove os delimitadores de comentário
        if p.slice[1].type == 'COMMENT_SINGLE_LINE':
            p[0] = {'op': 'comentario', 'args': p[1][2:].strip()}
        else:
            p[0] = {'op': 'comentario', 'args': p[1][2:-2].strip()}

    def p_declaracao_multiplas_atribuicoes(self, p):
        """declaracao_multiplas_atribuicoes : lista_atribuicoes ';'"""
        p[0] = {'op': 'seq', 'args': p[1]}

    def p_lista_atribuicoes(self, p):
        """lista_atribuicoes : atribuicao
                             | lista_atribuicoes ',' atribuicao"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[3])
            p[0] = p[1]

    def p_atribuicao(self, p):
        """atribuicao : VARID '=' expressao"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    def p_lista_expressoes(self, p):
        """lista_expressoes : expressao
                            | lista_expressoes ',' expressao"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[3])
            p[0] = p[1]

    # Expressão de concatenação
    def p_expressao_concat(self, p):
        """expressao : expressao CONCAT expressao"""
        p[0] = {'op': 'concat', 'args': [p[1], p[3]]}

    def p_expressao_string(self, p):
        """expressao : STRING"""
        partes = self.processar_interpolacao(p[1])
        if len(partes) == 1:
            p[0] = partes[0]
        else:
            p[0] = {'op': 'interpolacao', 'args': partes}

    def p_expressao_plus(self, p):
        """expressao : expressao '+' expressao"""
        p[0] = {'op': '+', 'args': [p[1], p[3]]}

    def p_expressao_minus(self, p):
        """expressao : expressao '-' expressao"""
        p[0] = {'op': '-', 'args': [p[1], p[3]]}

    def p_expressao_times(self, p):
        """expressao : expressao '*' expressao"""
        p[0] = {'op': '*', 'args': [p[1], p[3]]}

    def p_expressao_divide(self, p):
        """expressao : expressao '/' expressao"""
        p[0] = {'op': '/', 'args': [p[1], p[3]]}

    def p_expressao_group(self, p):
        """expressao : '(' expressao ')'"""
        p[0] = p[2]

    def p_expressao_uminus(self, p):
        """expressao : '-' expressao %prec UMINUS"""
        p[0] = {'op': 'uminus', 'args': [p[2]]}

    def p_expressao_var_id(self, p):
        """expressao : VARID"""
        p[0] = {'var': p[1]}

    def p_expressao_num(self, p):
        """expressao : NUM"""
        p[0] = {'op': 'literal', 'args': [p[1]]}

    def p_expressao_list(self, p):
        """expressao : '[' ']' 
                     | '[' lista_expressoes ']'"""
        if len(p) == 3:
            p[0] = {'op': 'list', 'args': []}
        else:
            p[0] = {'op': 'list', 'args': p[2]}

    def p_expressao_chamada_funcao(self, p):
        """expressao : VARID '(' lista_expressoes ')'
                     | ENTRADA '(' ')'
                     | ALEATORIO '(' expressao ')'"""
        if p.slice[1].type == 'VARID':
            p[0] = {'op': 'call_func', 'args': [p[1], p[3]]}
        elif p.slice[1].type == 'ENTRADA':
            p[0] = {'op': 'entrada', 'args': []}
        elif p.slice[1].type == 'ALEATORIO':
            p[0] = {'op': 'aleatorio', 'args': [p[3]]}

    def p_expressao_map(self, p):
        """expressao : MAP '(' VARID ',' expressao ')'"""
        p[0] = {'op': 'map', 'args': [{'var': p[3]}, p[5]]}

    def p_expressao_fold(self, p):
        """expressao : FOLD '(' VARID ',' expressao ',' expressao ')'"""
        p[0] = {'op': 'fold', 'args': [{'var': p[3]}, p[5], p[7]]}

    def p_parametros(self, p):
        """parametros : VARID
                      | parametros ',' VARID
                      | '[' ']'
                      | VARID ':' VARID '[' ']'"""
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 3:
            p[0] = [[]]
        elif len(p) == 6:
            p[0] = [{'op': 'var_array', 'args': [p[1], p[3]]}]
        else:
            p[1].append(p[3])
            p[0] = p[1]

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}'")
        else:
            print("Syntax error at EOF")
