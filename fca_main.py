# fca_main.py
from fca_grammar import FCAGrammar                  # Importa a classe FCAGrammar
from fca_eval import FCAEval                        # Importa a classe FCAEval
import sys                                          # Importa o módulo sys
from pprint import PrettyPrinter                    # Importa a classe PrettyPrinter


pp = PrettyPrinter(sort_dicts=False)
lg = FCAGrammar()
lg.build()


if len(sys.argv) == 2:                              # Se houver dois argumentos
    with open(sys.argv[1], "r") as file:            # Abre o arquivo para leitura
        contents = file.read()                      # Lê o conteúdo do arquivo
        try:
            tree = lg.parse(contents)               # Faz o parsing do conteúdo do arquivo
            pp.pprint(tree)                         # Imprime a árvore sintática
            resultado = FCAEval.evaluate(tree)      # Avalia a árvore sintática
            print(f"<< {resultado}")                # Imprime o resultado
        except Exception as e:                      # Em caso de exceção
            print(e, file=sys.stderr)               # Imprime a exceção
else:
    try:
        while True:
            expr = input(">> ")                     # Lê a expressão
            if not expr.strip():                    # Se a expressão estiver vazia
                break
            try:
                ast = lg.parse(expr)                # Faz o parsing da expressão
                pp.pprint(ast)                      # Imprime a árvore sintática
                resultado = FCAEval.evaluate(ast)   # Avalia a árvore sintática
                print(f"<< {resultado}")            # Imprime o resultado
            except Exception as e:                  # Em caso de exceção
                print(e)
    except (KeyboardInterrupt, EOFError):           # Em caso de interrupção ou fim de arquivo
        print("\nSaindo...")

