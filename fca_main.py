# fca_main.py
from fca_grammar import FCAGrammar  # Importa a classe FCAGrammar
from fca_eval import FCAEval
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

lg = FCAGrammar()
lg.build()

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            tree = lg.parse(contents)
            pp.pprint(tree)
            resultado = FCAEval.evaluate(tree)
            print(f"<< {resultado}")
        except Exception as e:
            print(e, file=sys.stderr)
else:
    try:
        while True:
            expr = input(">> ")
            if not expr.strip():
                break
            try:
                ast = lg.parse(expr)
                pp.pprint(ast)
                resultado = FCAEval.evaluate(ast)
                print(f"<< {resultado}")
            except Exception as e:
                print(e)
    except (KeyboardInterrupt, EOFError):
        print("\nSaindo...")

