import ply.lex as lex

class FCALexer:
    tokens = (
        "VARID",                            # Identifiers
        "NUM",                              # Numbers 
        "STRING",                           # Strings
        "PROGRAM",                          # Program
        "ENTRADA",                          # Input
        "ALEATORIO",                        # Random
        "FUNC",                             # Function
        "PRINT",                            # ESCREVER
        "CONCAT",                           # Concatenation operator
        "VAR",                              # Variable
        "CONST",                            # Constant
        "MAP",                              # Map function
        "FOLD",                             # Fold function
        "COMMENT",                          # Comment
        "FIM",                              # End
        "INTERPOLATION",                    # String interpolation
        "COMMENT_SINGLE_LINE",              # Single line comment
        "COMMENT_MULTI_LINE",               # Multi-line comment
    )

    # Defenição de literais
    literals = ["+", "-", "*", "/", "(", ")", "=", ";", ":", ",", "[", "]"] 
 
    # Caracteres a serem ignorados
    t_ignore = " \t"

    # Define token for single line comments
    def t_COMMENT_SINGLE_LINE(self, t):
        r"--.*"
        t.value = t.value[2:]  # Remove the comment marker
        return t # Return the token
        
    # Define token for multi-line comments
    def t_COMMENT_MULTI_LINE(self, t):
        r"\{\-([\s\S]*?)\-\}"
        return t  # Ignore multi-line comments

    # Define tokens for keywords
    def t_PROGRAM(self, t):
        r"[Pp][Rr][Oo][Gg][Rr][Aa][Mm][Aa]"
        return t

    # Define token for input function
    def t_ENTRADA(self, t):
        r"[Ee][Nn][Tt][Rr][Aa][Dd][Aa]"
        return t

    # Define token for random function
    def t_ALEATORIO(self, t):
        r"[Aa][Ll][Ee][Aa][Tt][Oo][Rr][Ii][Oo]"
        return t

    # Define token for function keyword
    def t_FUNC(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]"
        return t

    # Define token for print function
    def t_PRINT(self, t):
        r"[Ee][Ss][Cc][Rr][Ee][Vv][Ee][Rr]"
        return t
    
    #define token for variable
    def t_VAR(self, t):
        r"[Vv][Aa][Rr]"
        return t
    
    # Define token for constant
    def t_CONST(self, t):
        r"[Cc][Oo][Nn][Ss][Tt]"
        return t

    # Define token for function "map"
    def t_MAP(self, t):
        r"[Mm][Aa][Pp]"
        return t

    # Define token for function "fold"
    def t_FOLD(self, t):
        r"[Ff][Oo][Ll][Dd]"
        return t

    # Define token for "fim"
    def t_FIM(self, t):
        r"[Ff][Ii][Mm]"
        return t

    # Define token for string literals
    def t_STRING(self, t):
        r"\"([^\\\"]|\\.)*\""
        t.value = t.value[1:-1]  # Remove the quotation marks
        return t

    # Define token for identifiers
    def t_VARID(self, t):
        r"[a-zA-Z_][a-zA-Z0-9_]*[?!]?"
        return t

    # Define token for numbers
    def t_NUM(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    # Define token for concatenation operator
    def t_CONCAT(self, t):
        r"<>"
        return t

    # Define token for string interpolation
    def t_INTERPOLATION(self, t):
        r"\#\{[a-zA-Z_][a-zA-Z0-9_]*\}"
        t.value = t.value[2:-1]  # Extract the variable name
        return t

    # Define tokens for function definitions
    def t_FUNC_DEF(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*,:"
        t.type = "FUNC" 
        return t

    # Define tokens for multi-line function definitions
    def t_FUNC_DEF_MULTILINE(self, t): 
        r"[Ff][Uu][Nn][Cc][Aa][Oo]\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*:"
        t.type = "FUNC"
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
