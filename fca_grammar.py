from fca_lexer import FCALexer
import ply.yacc as pyacc
 
 
class FCAGrammar:
    # Define a precedência dos operadores para resolver questões na gramatica
    precedence = (
        ('left', '+', '-'),  # Operadores de adição e subtração com associatividade à esquerda
        ('left', '*', '/'),  # Operadores de multiplicação e divisão com associatividade à esquerda
        ('right', 'UMINUS', 'UNARY_NEG'),  # Operadores unários como '-' (negativo) e 'NEG' têm associatividade à direita
    )
 
    # Constructor
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None
 
    # Construir o analisador sintatico, pega no lexer e configura-o
    def build(self, **kwargs):
        self.lexer = FCALexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)
 
    # Realiza a analise sintatica do Input fornecido
    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)
 
    # Regras Producao da Gramatica:
 
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
                      | declaracao_se
                      | declaracao_escrever
                      | declaracao_comentario"""
        p[0] = p[1]
 
    # Declaração com atribuição
    def p_declaracao_atribuicao(self, p):
        """declaracao_atribuicao : VAR_ID '=' lista_expressoes ';'"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}
        
    #daqui para baixo nao está correto 
    
    # Declaração com atribuição
    def p_declaracao_atribuicao(self, p):
        """declaracao_atribuicao : varid equals lista_expressoes semicolon"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    # Declaração de expressão
    def p_declaracao_expressao(self, p):
        """declaracao_expressao : lista_expressoes semicolon"""
        p[0] = {'op': 'expressao', 'args': p[1]}

    # Declaração de função
    def p_declaracao_funcao(self, p):
        """declaracao_funcao : funcao varid lparen parametros rparen colon lista_declaracoes fim"""
        p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[7]]}

    # Declaração condicional "se"
    def p_declaracao_se(self, p):
        """declaracao_se : SE lparen expressao rparen entao lista_declaracoes fim"""
        p[0] = {'op': 'se', 'args': [p[3], p[6]]}

    # Declaração de comando "escrever"
    def p_declaracao_escrever(self, p):
        """declaracao_escrever : escrever lparen varid rparen semicolon"""
        p[0] = {'op': 'escrever', 'args': [p[3]]}

    # Declaração de comentário, este está correto
    def p_declaracao_comentario(self, p):
        """declaracao_comentario : comment"""
        p[0] = {'op': 'comentario', 'args': [p[1]]}

    # Lista de expressões
    def p_lista_expressoes(self, p):
        """lista_expressoes : expressao
                            | lista_expressoes comma expressao"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[3])
            p[0] = p[1]

    # Expressão
    def p_expressao(self, p):
        """expressao : expressao plus expressao
                     | expressao minus expressao
                     | expressao times expressao
                     | expressao divide expressao
                     | lparen expressao rparen
                     | minus expressao %prec UMINUS
                     | varid
                     | num"""
        if len(p) == 4:
            if p[2] == '+':
                p[0] = {'op': '+', 'args': [p[1], p[3]]}
            elif p[2] == '-':
                p[0] = {'op': '-', 'args': [p[1], p[3]]}
            elif p[2] == '*':
                p[0] = {'op': '*', 'args': [p[1], p[3]]}
            elif p[2] == '/':
                p[0] = {'op': '/', 'args': [p[1], p[3]]}
            else:
                p[0] = p[2]
        elif len(p) == 3:
            p[0] = {'op': 'neg', 'args': [p[2]]}
        elif len(p) == 2:
            p[0] = p[1]

    # Parâmetros de função
    def p_parametros(self, p):
        """parametros : varid
                      | parametros comma varid"""
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