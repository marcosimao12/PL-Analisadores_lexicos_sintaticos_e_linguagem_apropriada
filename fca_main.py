from fca_grammar import FCAGrammar
from fca_eval import FCAEval
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

parser = FCAGrammar()

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            tree = parser.parse(contents)
            pp.pprint(tree)
            resultado = FCAEval.evaluate(tree)
            print(f"<< {resultado}")
        except Exception as e:
            print(e, file=sys.stderr)
else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            tree = parser.parse(expr)
            resultado = FCAEval.evaluate(tree)
            print(f"<< {resultado}")
        except Exception as e:
            print(e)
