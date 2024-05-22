class FCAEval:
    symbols = {}

    operators = {
        'plus': lambda args: args[0] + args[1],
        'times': lambda args: args[0] * args[1],
        'assign': lambda args: FCAEval._assign(args),
        'num': lambda args: args[0],
        'id': lambda args: FCAEval._get_id(args)
    }

    @staticmethod
    def _assign(args):
        value = args[1]
        FCAEval.symbols[args[0]] = value
        return value

    @staticmethod
    def _get_id(args):
        var = args[0]
        if var in FCAEval.symbols:
            return FCAEval.symbols[var]
        else:
            raise Exception(f"Undefined variable '{var}'")

    @staticmethod
    def evaluate(ast):
        if isinstance(ast, tuple):
            op = ast[0]
            args = [FCAEval.evaluate(a) for a in ast[1:]]
            if op in FCAEval.operators:
                return FCAEval.operators[op](args)
            else:
                raise Exception(f"Unknown operator '{op}'")
        else:
            return ast

# Exemplo de uso
if __name__ == '__main__':
    ast = ('program', 'exemplo', ('body', [], [('assign', 'x', ('plus', ('num', 5), ('times', ('num', 3), ('num', 2))))]))
    result = FCAEval.evaluate(ast)
    print(result)
