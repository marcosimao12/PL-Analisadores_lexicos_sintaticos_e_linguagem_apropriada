from fca_lexer import FCALexer
import ply.yacc as yacc
 
class FCAGrammar:
    # Define a precedência dos operadores para resolver questões na gramática
    precedence = (
        ('left', 'plus', 'minus'),  # Operadores de adição e subtração com associatividade à esquerda
        ('left', 'times', 'divide'),  # Operadores de multiplicação e divisão com associatividade à esquerda
        ('right', 'UMINUS'),  # Operador unário '-' (negativo) tem associatividade à direita
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
                      | declaracao_escrever
                      | declaracao_comentario"""
        p[0] = p[1]

    # Declaração com atribuição
    def p_declaracao_atribuicao(self, p):
        """declaracao_atribuicao : varid equals expressao ';'"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    # Declaração de expressão
    def p_declaracao_expressao(self, p):
        """declaracao_expressao : expressao ';'"""
        p[0] = {'op': 'expressao', 'args': [p[1]]}

    # Declaração de função
    def p_declaracao_funcao(self, p):
        """declaracao_funcao : funcao varid '(' parametros ')' ',' ':' lista_declaracoes fim
                             | funcao varid '(' parametros ')' ',' ':' expressao ';'"""
        if len(p) == 10:  # Regra com múltiplas declarações e FIM
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[8]]}
        else:  # Regra com expressão única e ponto e vírgula
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[8]]}

    # Declaração de comando "escrever"
    def p_declaracao_escrever(self, p):
        """declaracao_escrever : escrever '(' expressao ')' ';'"""
        p[0] = {'op': 'escrever', 'args': [p[3]]}

    # Declaração de comentário
    def p_declaracao_comentario(self, p):
        """declaracao_comentario : comment"""
        p[0] = {'op': 'comentario', 'args': [p[1]]}

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

    # Expressão geral
    def p_expressao(self, p):
        """expressao : expressao '+' expressao
                     | expressao '-' expressao
                     | expressao '*' expressao
                     | expressao '/' expressao
                     | '(' expressao ')'
                     | '-' expressao %prec UMINUS
                     | varid
                     | num
                     | string
                     | '[' lista_expressoes ']'"""
        if len(p) == 4:
            if p[2] == '+':
                p[0] = {'op': '+', 'args': [p[1], p[3]]}
            elif p[2] == '-':
                p[0] = {'op': '-', 'args': [p[1], p[3]]}
            elif p[2] == '*':
                p[0] = {'op': '*', 'args': [p[1], p[3]]}
            elif p[2] == '/':
                p[0] = {'op': '/', 'args': [p[1], p[3]]}
        elif len(p) == 3:
            p[0] = {'op': 'neg', 'args': [p[2]]}
        elif len(p) == 2:
            if isinstance(p[1], int):
                p[0] = {'op': 'literal', 'args': [p[1]]}
            elif isinstance(p[1], str):
                if p[1].startswith('"') and p[1].endswith('"'):
                    p[0] = {'op': 'literal', 'args': [p[1][1:-1]]}
                else:
                    p[0] = {'op': 'literal', 'args': [p[1]]}
            else:
                p[0] = p[1]
        elif isinstance(p[1], str):
             p[0] = {'op': 'var', 'args': [p[1]]}

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