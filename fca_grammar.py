import ply.yacc as yacc
from fca_lexer import FCALexer

class FCAGrammar:
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    def __init__(self):
        self.lexer = FCALexer()
        self.lexer.build()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)

    def parse(self, data):
        self.lexer.input(data)
        return self.parser.parse(lexer=self.lexer.lexer)

    # Definir as regras de produção
    def p_program(self, p):
        """program : PROGRAMA ID declarations statements"""
        p[0] = ('program', p[2], p[3], p[4])

    def p_declarations(self, p):
        """declarations : declarations declaration
                        | declaration"""
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_declaration(self, p):
        """declaration : CONST ID EQUALS NUMBER SEMICOLON
                       | VAR ID SEMICOLON"""
        if len(p) == 6:
            p[0] = ('const_decl', p[2], p[4])
        else:
            p[0] = ('var_decl', p[2])

    def p_statements(self, p):
        """statements : statements statement
                      | statement"""
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_statement(self, p):
        """statement : assignment
                     | print_stmt"""
        p[0] = p[1]

    def p_assignment(self, p):
        """assignment : ID EQUALS expression SEMICOLON"""
        p[0] = ('assign', p[1], p[3])

    def p_print_stmt(self, p):
        """print_stmt : ESCREVER ID SEMICOLON"""
        p[0] = ('print', p[2])

    def p_expression(self, p):
        """expression : expression PLUS term
                      | expression MINUS term
                      | term"""
        if len(p) == 4:
            p[0] = (p[2], p[1], p[3])
        else:
            p[0] = p[1]

    def p_term(self, p):
        """term : term TIMES factor
                | term DIVIDE factor
                | factor"""
        if len(p) == 4:
            p[0] = (p[2], p[1], p[3])
        else:
            p[0] = p[1]

    def p_factor(self, p):
        """factor : NUMBER
                  | ID
                  | LPAREN expression RPAREN"""
        if len(p) == 2:
            p[0] = ('num', p[1]) if isinstance(p[1], int) else ('id', p[1])
        else:
            p[0] = p[2]

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}'")
        else:
            print("Syntax error at EOF")

# Exemplo de uso
if __name__ == '__main__':
    parser = FCAGrammar()
    data = '''
    PROGRAMA exemplo
    VAR x;
    x = 5 + 3 * (2 + 1);
    '''
    result = parser.parse(data)
    print(result)
