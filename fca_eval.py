class FCAEval:
    symbols = {}
    functions = {}

    operators = {
        '+': lambda args: args[0] + args[1],
        '-': lambda args: args[0] - args[1],
        '*': lambda args: args[0] * args[1],
        '/': lambda args: args[0] / args[1],
        'concat':       lambda args: ''.join(args),
        'seq':          lambda args: args[-1],
        'atribuicao':   lambda args: FCAEval._assign(args),
        'escrever':     lambda args: print(args[0]),
        'literal':      lambda args: args[0],
        'call_func':    lambda args: FCAEval._call_function(args),
        'map':          lambda args: FCAEval._map_function(args),
        'fold':         lambda args: FCAEval._fold_function(args),
        'comentario':   lambda args: None,  # Ignora comentários
        'interpolacao': lambda args: FCAEval._interpolacao(args),
        'entrada':      lambda args: FCAEval._entrada(),
        'aleatorio':    lambda args: FCAEval._aleatorio(args),
        'var':          lambda args: FCAEval._get_var(args),
        'func_param':   lambda args: args,  # Apenas retorna a lista de argumentos
        'list':         lambda args: args  # Suporte a listas
    }

    @staticmethod
    def _assign(args):
        value = args[1]
        FCAEval.symbols[args[0]] = value
        return value

    @staticmethod
    def _get_var(args):
        var_name = args[0]
        if var_name in FCAEval.symbols:
            return FCAEval.symbols[var_name]
        else:
            raise Exception(f"Undefined variable '{var_name}'")

    @staticmethod
    def _call_function(args):
        func_name, func_args = args
        if func_name in FCAEval.functions:
            func_def = FCAEval.functions[func_name] 
            params, body = func_def['parametros'], func_def['corpo'] 
            if len(params) != len(func_args):
                raise Exception(f"Function '{func_name}' expected {len(params)} arguments but got {len(func_args)}")

            # Salvar o escopo atual e criar um novo escopo para a função
            old_symbols = FCAEval.symbols.copy()
            local_symbols = {}

            # Avaliar argumentos e associar aos parâmetros
            for param, arg in zip(params, func_args):
                local_symbols[param['var']] = FCAEval.evaluate(arg)

            # Atualizar o escopo para o escopo local da função
            FCAEval.symbols = local_symbols

            result = FCAEval.evaluate(body)

            # Restaurar o escopo antigo
            FCAEval.symbols = old_symbols

            return result
        else:
            raise Exception(f"Undefined function '{func_name}'")

    @staticmethod
    def _map_function(args):
        func, lst = args
        return list(map(lambda x: FCAEval.evaluate({'op': 'call_func', 'args': [func['var'], [x]]}), lst))

    @staticmethod
    def _fold_function(args):
        func, lst, initial = args
        from functools import reduce
        return reduce(lambda acc, x: FCAEval.evaluate({'op': 'call_func', 'args': [func['var'], [acc, x]]}), lst, initial)

    @staticmethod
    def _interpolacao(args):
        result = ''
        for arg in args:
            result += str(arg)
        return result

    @staticmethod
    def _entrada():
        return input("Digite um valor: ")

    @staticmethod
    def _aleatorio(args):
        import random
        return random.randint(0, args[0])

    @staticmethod
    def _def_func(body, params, args):
        func_name = args[0]
        params = params
        body = body
        FCAEval.functions[func_name] = {'parametros': params, 'corpo': body}
        return None

    @staticmethod
    def evaluate(ast):
        if isinstance(ast, int):  # constant value
            return ast
        if isinstance(ast, dict): # { 'op': ... , 'args': ...}
            return FCAEval._eval_operator(ast)
        if isinstance(ast, str): 
            return ast
        if isinstance(ast, list):  # sequence of statements
            result = []
            for stmt in ast:
                result.append(stmt) # evaluate each statement
            return result
        raise Exception(f"Unknown AST type: {type(ast)}")   

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast and ast['op'] == 'funcao': # function definition
            return FCAEval._def_func(ast['corpo'], ast['parametros'], ast['args']) # define function
        if 'op' in ast: # operator
            op = ast["op"] # operator name
            args = [FCAEval.evaluate(a) for a in ast['args']] # evaluate arguments
            if op in FCAEval.operators: # operator implementation
                func = FCAEval.operators[op] # get operator function
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            varid = ast["var"]
            if varid in FCAEval.symbols:
                return FCAEval.symbols[varid]
            raise Exception(f"error: local variable '{varid}' referenced before assignment")

        raise Exception('Undefined AST')
