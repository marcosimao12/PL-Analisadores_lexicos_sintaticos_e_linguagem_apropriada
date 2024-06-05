import sys
from fca_lexer import FCALexer

# Verifica se o nome do arquivo foi passado como argumento
if len(sys.argv) != 2:
    print("Uso: python test_fca_lexer.py ficheiro.fca")
    sys.exit()

# Obtém o nome do arquivo do argumento
filename = sys.argv[1]

# Abre o arquivo e lê as frases
with open(filename, 'r') as file:
    ficheiro = file.readlines()

for frase in ficheiro:
    print(f"----------------------")
    print(f"frase: '{frase.strip()}'")
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
