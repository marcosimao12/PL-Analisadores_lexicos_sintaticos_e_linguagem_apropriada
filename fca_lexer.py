import ply.lex as lex

class FCALexer:
    tokens = (
        "varid", "num", "plus", "minus", "times", "divide", "lparen", "rparen",
        "equals", "semicolon", "colon", "comma", "string", "programa", "entrada", 
        "aleatorio", "funcao", "escrever", "lbracket", "rbracket", "concat", "map", "fold",
        "comment", "fim"
    )

    # Define literals (single-character tokens)
    literals = ["+", "-", "*", "/", "(", ")", "=", ";", ":", ",", "[", "]"]

    # Ignored characters (spaces and tabs)
    t_ignore = " \t"

    # Define token for single line comments
    def t_comment_single_line(self, t):
        r"--.*"
        t.type = "comment"
        t.value = t.value[2:]  # Remove the comment marker
        return t

    # Define token for multi-line comments
    def t_comment_multi_line(self, t):
        r"\{-.*?-\}"
        t.type = "comment"
        t.value = t.value[2:-2]  # Remove the comment markers
        return t

    # Define tokens for keywords
    def t_programa(self, t):
        r"[Pp][Rr][Oo][Gg][Rr][Aa][Mm][Aa]"
        return t

    def t_entrada(self, t):
        r"[Ee][Nn][Tt][Rr][Aa][Dd][Aa]"
        return t

    def t_aleatorio(self, t):
        r"[Aa][Ll][Ee][Aa][Tt][Oo][Rr][Ii][Oo]"
        return t

    def t_funcao(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]"
        return t

    def t_escrever(self, t):
        r"[Ee][Ss][Cc][Rr][Ee][Vv][Ee][Rr]"
        return t

    def t_map(self, t):
        r"[Mm][Aa][Pp]"
        return t

    def t_fold(self, t):
        r"[Ff][Oo][Ll][Dd]"
        return t

    def t_fim(self, t):
        r"[Ff][Ii][Mm]"
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

    # Define tokens for function definitions
    def t_funcao_def(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*,:"
        t.type = "funcao"
        return t

    def t_funcao_def_multiline(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*:"
        t.type = "funcao"
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Define error handling rule
    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        t.lexer.skip(1)  # Skip the token and continue

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Input function to set the data for the lexer
    def input(self, string):
        self.lexer.input(string)

    # Token function to get the next token
    def token(self):
        token = self.lexer.token()
        return token.type if token else None
