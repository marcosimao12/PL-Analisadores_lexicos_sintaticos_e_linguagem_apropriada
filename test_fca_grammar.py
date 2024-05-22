from fca_grammar import FCAGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

parser = FCAGrammar()

exemplos = [
    "PROGRAMA exemplo VAR x; x = 5 + 3 * (2 + 1);",
    "PROGRAMA exemplo CONST x = 10; VAR y; y = x + 20;",
    "PROGRAMA exemplo x = 10; y = x * 2; ESCREVER y;",
    "PROGRAMA exemplo x = (3 + 4) * 2; y = x + 1;",
]

for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    result = parser.parse(frase)
    print("resultado: ")
    pp.pprint(result)
