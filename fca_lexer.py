# fca_lexer.py
import ply.lex as lex

class FCALexer:
    tokens = (
        "varid", "num", "plus", "minus", "times", "divide", "lparen", "rparen",
        "equals", "semicolon", "colon", "comma", "string", "programa", "const", 
        "var", "entrada", "aleatorio", "funcao", "escrever", "lbracket", "rbracket", 
        "concat", "map", "fold"
    )

    # Define literals (single-character tokens)
    literals = ["+", "-", "*", "/", "(", ")", "=", ";", ":", ",", "[", "]"]

    # Ignored characters (spaces and tabs)
    t_ignore = " \n"

    def __init__(self):
        self.lexer = None

    # Define tokens for keywords
    def t_programa(self, t):
        r"PROGRAMA"
        return t

    def t_const(self, t):
        r"CONST"
        return t

    def t_var(self, t):
        r"VAR"
        return t

    def t_entrada(self, t):
        r"ENTRADA"
        return t

    def t_aleatorio(self, t):
        r"ALEATORIO"
        return t

    def t_funcao(self, t):
        r"FUNCAO"
        return t

    def t_escrever(self, t):
        r"[Ee][Ss][Cc]([Rr][Ee][Vv][Ee][Rr])?"
        return t

    def t_map(self, t):
        r"MAP"
        return t

    def t_fold(self, t):
        r"FOLD"
        return t

    # Define token for string literals
    def t_string(self, t):
        r"\"([^\\\"]|\\.)*\""
        t.value = t.value[1:-1]  # Remove the quotation marks
        return t

    # Define token for identifiers
    def t_varid(self, t):
        r"[a-zA-Z_][a-zA-Z0-9_]*"
        return t

    # Define token for numbers
    def t_num(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    # Define token for concatenation operator
    def t_concat(self, t):
        r"<>"
        return t

    # Define token for comments (single line and multi-line)
    def t_comment_single_line(self, t):
        r"\-\-.*"
        pass  # No return value. Token discarded

    def t_comment_multi_line(self, t):
        r"\{\-.*?-\}"
        pass  # No return value. Token discarded

    # Define error handling rule
    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Input function to set the data for the lexer
    def input(self, string):
        self.lexer.input(string)

    # Token function to get the next token
    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type 
