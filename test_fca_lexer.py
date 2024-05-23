from fca_lexer import FCALexer

exemplos = [  # exemplos a avaliar de forma independente... 
    "(3-6)+9",
    "num+2",
    "ESCREVER Z;",
    """ x = 10  ; 
    y = 10 + 20 * 30;
    z = x * 100 ; 
    b =  a + 1 ; """
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
        print(tk, end=" ")
    print()
