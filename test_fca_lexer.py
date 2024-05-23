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
    """FUNCAO fib( 0 ),: 0 ;
    FUNCAO fib( 1 ),: 0 ;
    FUNCAO fib( n ):
        a = fib(n-1);
        b = fib(n-2);
        a + b;
    FIM""",
    "fib5 = fib(5);",
    "lista = [ 1, 2, 3 ] ;",
    "ESCREVER( lista ); -- [1,2,3]",
    "vazia = [] ;",
    "FUNCAO mais2( x ),: x + 2 ;",
    "FUNCAO soma( a, b ),: a + b ;",
    "lista1 = map( mais2, [] ); -- []",
    "lista2 = map( mais2, [ 1, 2, 3 ] ); "
    "-- [ mais2(1),mais2(2),mais2(3)] = [3,4,5]",
    "lista3 = fold( soma, [ 1, 2, 3 ], 0 );",
    "-- = soma( 1, soma(2, soma ( 3, 0)))",
    "-- = soma( 1, soma(2, 3 ))",
    "-- = soma( 1, 5)",
    "-- = 6",
    "FUNCAO somatorio( [] ),: 0 ;",
    """FUNCAO somatorio( x:xs ),: x + somatorio(xs) ;
        resultado = somatorio([1,2,3]);""",
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
