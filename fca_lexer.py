import ply.lex as lex

class FCALexer:
    tokens = (
        'ID', 'NUMBER', 'PLUS', 'TIMES', 'LPAREN', 'RPAREN', 'EQUALS', 'SEMICOLON',
        'STRING', 'PROGRAMA', 'CONST', 'VAR', 'INTEIRO', 'SLASH', 'DOT', 'COLON',
        'MINUS', 'DIVIDE', 'ESCREVER'
    )
    literals = ['+', '-', '*', '(', ')', '=', ';', ':', '.']

    t_ignore = ' \t'

    def t_PROGRAMA(self, t):
        r'PROGRAMA'
        return t

    def t_CONST(self, t):
        r'CONST'
        return t

    def t_VAR(self, t):
        r'VAR'
        return t

    def t_INTEIRO(self, t):
        r'INTEIRO'
        return t

    def t_STRING(self, t):
        r'\"[^"]*\"'
        t.value = t.value[1:-1]  # Remove the quotation marks
        return t

    def t_SLASH(self, t):
        r'/'
        return t

    def t_DOT(self, t):
        r'\.'
        return t

    def t_COLON(self, t):
        r':'
        return t

    def t_MINUS(self, t):
        r'-'
        return t

    def t_DIVIDE(self, t):
        r'/'
        return t

    def t_ESCREVER(self, t):
        r'ESCREVER'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*[?!]?'
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()
