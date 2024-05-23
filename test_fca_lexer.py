from fca_lexer import FCALexer

# exemplos = [  # exemplos a avaliar de forma independente... 
#     "ESCREVER(valor);   -- conteudo de valor e apresentado",
#     "ESCREVER(365 * 2); -- 730",
#     "ESCREVER(\"Ola Mundo\"); -- Ola, Mundo!",
#     "curso = \"ESI\";",
#     "ESCREVER(\"Ola, \"<> curso); -- Ola, ESI",
#     """ x = 10  ; 
#     y = 10 + 20 * 30;
#     z = x * 100 ; 
#     b =  a + 1 ; """,
#     "x = 5 + 3 * (2 + 1);",
#     "\"Hello, World!\"",
# ]

exemplos = [  # exemplos a avaliar de forma independente... 
    "ESCREVER(valor);   -- conteudo de valor e apresentado",
    "ESCREVER(365 * 2); -- 730",
    "ESCREVER(\"Ola Mundo\"); -- Ola, Mundo!",
    "curso = \"ESI\";",
    "ESCREVER(\"Ola, \"<> curso); -- Ola, ESI",
    "\"Hello, World!\"",
    "\"Hello, World!\" {- teste comentario -}",
    "FUNCAO soma(a,b),: a+b ;",
    "FUNCAO soma2(c) : c = c+1 ; c+1 ; FIM",
    "fib5 = fib(5);",
    "seis = soma(4,2);",
    "oito = soma2(seis);",
    """FUNCAO area_retangulo(a, b):
    a * b;
    FIM""",
    """FUNCAO area_quadrado(a):
        area_retangulo(a, a);
    FIM""",
    "a = area_retangulo(10, 20);",
    "b = area_quadrado(30);",
]

for frase in exemplos:
    print(f"----------------------")
    print(f"frase: '{frase}'")
    lexer = FCALexer()
    lexer.build()
    lexer.input(frase)
    print('tokens: ', end="")
    while True:
        tk_type = lexer.token()
        if not tk_type:
            break
        print(tk_type, end=" ")
    print()
