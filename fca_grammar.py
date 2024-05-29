from fca_lexer import FCALexer
import ply.yacc as yacc

class FCAGrammar:
    # Define a precedência dos operadores para resolver questões na gramática
    precedence = (
        ('left', '+', '-'),  # Operadores de adição e subtração com associatividade à esquerda
        ('left', '*', '/'),  # Operadores de multiplicação e divisão com associatividade à esquerda
        ('right', 'UMINUS'),  # Operador unário de negação
    )

    # Constructor
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    # Construir o analisador sintático, pega no lexer e configura-o
    def build(self, **kwargs):
        self.lexer = FCALexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = yacc.yacc(module=self, **kwargs)

    # Realiza a análise sintática do input fornecido
    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # Regras de produção da gramática

    # Lista de declarações, que pode ser uma única declaração ou várias declarações
    def p_lista_declaracoes(self, p):
        """lista_declaracoes : declaracao
                             | lista_declaracoes declaracao"""
        if len(p) == 2:
            p[0] = {'op': 'seq', 'args': [p[1]]}  # uma única declaração
        else:
            p[1]['args'].append(p[2])  # Adiciona a declaração à lista existente
            p[0] = p[1]

    # Declarações gerais dentro do programa
    def p_declaracao(self, p):
        """declaracao : declaracao_atribuicao
                      | declaracao_expressao
                      | declaracao_funcao
                      | declaracao_funcao_literal
                      | declaracao_escrever
                      | declaracao_comentario
                      | declaracao_multiplas_atribuicoes"""
        p[0] = p[1]

    # Declaração com atribuição
    def p_declaracao_atribuicao(self, p):
        """declaracao_atribuicao : varid '=' expressao ';'"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    # Declaração de expressão
    def p_declaracao_expressao(self, p):
        """declaracao_expressao : expressao ';'"""
        p[0] = p[1]

    # Declaração de função
    def p_declaracao_funcao(self, p):
        """declaracao_funcao : funcao varid '(' parametros ')' ':' lista_declaracoes fim
                             | funcao varid '(' parametros ')' ',' ':' expressao ';'"""
        if len(p) == 9:
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[7]]}
        else:
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], [p[8]]]}

    # Declaração de função com parâmetro literal
    def p_declaracao_funcao_literal(self, p):
        """declaracao_funcao_literal : funcao varid '(' num ')' ',' ':' expressao ';'"""
        p[0] = {'op': 'funcao', 'args': [p[2], [p[4]], p[8]]}

    # Declaração de comando "escrever"
    def p_declaracao_escrever(self, p):
        """declaracao_escrever : escrever '(' expressao ')' ';'"""
        p[0] = {'op': 'escrever', 'args': [p[3]]}

    # Declaração de comentário
    def p_declaracao_comentario(self, p):
        """declaracao_comentario : comment"""
        p[0] = {'op': 'comentario', 'args': [p[1]]}

    # Declaração de múltiplas atribuições
    def p_declaracao_multiplas_atribuicoes(self, p):
        """declaracao_multiplas_atribuicoes : lista_atribuicoes ';'"""
        p[0] = {'op': 'seq', 'args': p[1]}

    # Lista de atribuições
    def p_lista_atribuicoes(self, p):
        """lista_atribuicoes : atribuicao
                             | lista_atribuicoes ',' atribuicao"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[3])
            p[0] = p[1]

    # Atribuição
    def p_atribuicao(self, p):
        """atribuicao : varid '=' expressao"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    # Lista de expressões
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
        """expressao : expressao concat expressao"""
        p[0] = {'op': 'concat', 'args': [p[1], p[3]]}

    # Expressões específicas
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
        """expressao : varid"""
        p[0] = {'var': p[1]}

    def p_expressao_num(self, p):
        """expressao : num"""
        p[0] = {'op': 'literal', 'args': [p[1]]}

    def p_expressao_string(self, p):
        """expressao : string"""
        p[0] = {'op': 'literal', 'args': [p[1]]}

    def p_expressao_list(self, p):
        """expressao : '[' ']' 
                     | '[' lista_expressoes ']'"""
        if len(p) == 3:
            p[0] = {'op': 'list', 'args': []}
        else:
            p[0] = {'op': 'list', 'args': p[2]}

    # Adição da regra para chamada de função dentro de expressões
    def p_expressao_chamada_funcao(self, p):
        """expressao : varid '(' lista_expressoes ')'"""
        p[0] = {'op': 'call_func', 'args': [p[1], p[3]]}

    # Adição da regra para map e fold dentro de expressões
    def p_expressao_map(self, p):
        """expressao : map '(' varid ',' expressao ')'"""
        p[0] = {'op': 'map', 'args': [{'var': p[3]}, p[5]]}

    def p_expressao_fold(self, p):
        """expressao : fold '(' varid ',' expressao ',' expressao ')'"""
        p[0] = {'op': 'fold', 'args': [{'var': p[3]}, p[5], p[7]]}

    # Parâmetros de função
    def p_parametros(self, p):
        """parametros : varid
                      | parametros ',' varid"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[3])
            p[0] = p[1]

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}'")
        else:
            print("Syntax error at EOF")
