class FCAEval:
    symbols = {}
    functions = {}

    operators = {
        '+':            lambda args: args[0] + args[1],                                # Soma
        '-':            lambda args: args[0] - args[1],                                # Subtração
        '*':            lambda args: args[0] * args[1],                                # Multiplicação
        '/':            lambda args: args[0] / args[1],                                # Divisão
        'concat':       lambda args: ''.join(args),                                    # Concatenação
        'seq':          lambda args: args[-1],                                         # Sequência
        'atribuicao':   lambda args: FCAEval._assign(args),                            # Atribuição
        'escrever':     lambda args: print(args[0]),                                   # Escrever
        'literal':      lambda args: args[0],                                          # Literal
        'call_func':    lambda args: FCAEval._call_function(args),                     # Chamada de função
        'map':          lambda args: FCAEval._map_function(args),                      # Map
        'fold':         lambda args: FCAEval._fold_function(args),                     # Fold
        'comentario':   lambda args: None,                                             # Ignora comentários 
        'interpolacao': lambda args: FCAEval._interpolacao(args),                      # Interpolação
        'entrada':      lambda args: FCAEval._entrada(),                               # Entrada
        'aleatorio':    lambda args: FCAEval._aleatorio(args),                         # Aleatório
        'var':          lambda args: FCAEval._get_var(args),                           # Variável
        'list':         lambda args: args,                                             # Suporte a listas
        'array_vazio':  lambda args: [],                                               # Suporte a listas vazias
    }

    @staticmethod
    def _assign(args): 
        value = args[1]
        FCAEval.symbols[args[0]] = value
        return value

    @staticmethod
    def _get_var(args):                                                                # get variable value
        var_name = args[0]                                                             # get variable name
        if var_name in FCAEval.symbols:                                                # verifica se a variável está definida
            return FCAEval.symbols[var_name]                                           # retorna o valor da variável
        else:                                                                          # caso contrário
            raise Exception(f"Undefined variable '{var_name}'")                        # retorna erro

    @staticmethod
    def _def_func(body, params, args):                                                 # define a function
        func_name = args[0]                                                            # get function name
        params = params if params else []                                              # get function parameters
        body = body                                                                    # get function body
        if func_name not in FCAEval.functions:                                         # se a função não está definida
            FCAEval.functions[func_name] = []                                          # inicializa a função
        FCAEval.functions[func_name].append({'parametros': params, 'corpo': body})     # adiciona a função
        return None 

    @staticmethod
    def _call_function(args):                                                         # call a function
        func_name, func_args = args                                                   # get function name and arguments
        if func_name in FCAEval.functions:                                            # verifica se a função está definida 
            for func_def in FCAEval.functions[func_name]:                             # get function definition
                params, body = func_def['parametros'], func_def['corpo']              # get function parameters and body
                if len(params) == len(func_args):                                     # verifica se o número de argumentos é igual ao número de parâmetros
                    old_symbols = FCAEval.symbols.copy()                              # pega o escopo atual
                    local_symbols = old_symbols.copy()                                # copia o escopo atual
                    
                    for param, arg in zip(params, func_args):                         # itera sobre os parâmetros e argumentos
                        if 'var' in param:                                            # verifica se é uma variável
                            local_symbols[param['var']] = FCAEval.evaluate(arg)       # adiciona a variável ao escopo
                        elif 'op' in param and param['op'] == 'var_array':            # verifica se é um array
                            if len(arg) > 0:                                          # verifica se o array não está vazio
                                local_symbols[param['args'][0]] = arg[0]              
                                local_symbols[param['args'][1]] = arg[1:]             
                            else:                                                     # caso contrário
                                local_symbols[param['args'][1]] = []                  # inicializa o array vazio
                        elif 'op' in param and FCAEval.evaluate(param) == FCAEval.evaluate(arg):  # verifica se é uma variável
                            continue 
                        else:
                            break
                    else:                   
                        FCAEval.symbols = local_symbols  
                        
                        result = FCAEval.evaluate(body)                               # evaluate function body
                       
                        FCAEval.symbols = old_symbols

                        return result 
                   
            raise Exception(f"Function '{func_name}' with {len(func_args)} parameters not defined")     # retorna erro
        else:
            raise Exception(f"Undefined function '{func_name}'")                                        # retorna erro
        
    @staticmethod
    def _map_function(args):                                                                          # map function
        func, lst = args                                                                              # get function and list
        return list(map(lambda x: FCAEval.evaluate({'op': 'call_func', 'args': [func, [x]]}), lst))   # apply function to list
    

    @staticmethod
    def _fold_function(args):                                                                        # fold function
        func = args[0]                                                                               # get function
        array = args[1]                                                                              # get array
        initial = args[2]                                                                            # get initial value
        result = initial                                                                             # set initial value
        for element in array:                                                                        # iterate over array
            result = FCAEval._call_function([func, [result, element]])                               # apply function to element
        return result

    @staticmethod
    def _interpolacao(args):                                                                         # interpolation
        result = ''                                                                                  # initialize result
        for arg in args:                                                                             # iterate over arguments
            result += str(arg)                                                                      
        return result

    @staticmethod
    def _entrada():                                                                                # input function
        return input("Digite um valor: ")                                                          # input function

    @staticmethod
    def _aleatorio(args):                                                                         # random function
        import random                                                                             # import random module
        return random.randint(0, args[0])                                                         # return random value

    @staticmethod  
    def evaluate(ast):                                                                            # evaluate an AST
        if isinstance(ast, int):                                                                  # constant value 
            return ast 
        if isinstance(ast, dict): 
            return FCAEval._eval_operator(ast)                                                    # evaluate operator
        if isinstance(ast, str): 
            return ast
        if isinstance(ast, list):                                                                 # list of statements
            result = []
            for stmt in ast:
                result.append(FCAEval.evaluate(stmt))                                             # evaluate statement
            return result
        raise Exception(f"Unknown AST type: {type(ast)}")                                         # unknown AST type

    @staticmethod
    def _eval_operator(ast):                                                                     # evaluate operator
        if 'op' in ast and ast['op'] == 'funcao':                                                # function definition
            return FCAEval._def_func(ast['corpo'], ast['parametros'], ast['args'])               # define function   
        if 'op' in ast:                                                                          # operator
            op = ast["op"]                                                                       # get operator
            args = [FCAEval.evaluate(a) for a in ast['args']]                                    # evaluate arguments 
            if op in FCAEval.operators:                                                          # check if operator is defined
                func = FCAEval.operators[op]                                                     # get operator function
                return func(args)                                                                # apply operator
            else:
                raise Exception(f"Unknown operator {op}")                                      # unknown operator
        if 'var' in ast:                                                                        # variable
            varid = ast["var"]                                                                  # get variable name
            if varid in FCAEval.symbols:                                                        # check if variable is defined
                return FCAEval.symbols[varid]                                                   # return variable value
            raise Exception(f"error: local variable '{varid}' referenced before assignment")    # variable not defined

        raise Exception('Undefined AST')

