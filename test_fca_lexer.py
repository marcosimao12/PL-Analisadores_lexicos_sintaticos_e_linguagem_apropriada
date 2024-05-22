from fca_lexer import FCALexer

exemplos = [
    "PROGRAMA exemplo",
    "CONST x = 10;",
    "VAR y;",
    "x = 5 + 3 * (2 + 1);",
    "\"Hello, World!\"",
]

for frase in exemplos:
    print(f"----------------------")
    print(f"frase: '{frase}'")
    lexer = FCALexer()
    lexer.build()
    lexer.input(frase)
    print('tokens: ', end="")
    while True:
        tk = lexer.token()
        if not tk:
            break
        print(tk, end="")
    print()
