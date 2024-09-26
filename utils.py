def timer(func):
    def wrapper(*args, **kwargs):
        # Q1: args 和 kwargs 是什么？
        # A1: *args 和 **kwargs 是 python 中的可变参数，*args 表示任意多个无名参数，类型为 tuple；**kwargs 表示关键字参数，类型为 dict
        import time
        print(f'Function {func.__name__} input: {args}')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('Func{} run time: {}'.format(func.__name__, round(end_time-start_time),2))
        print(f'Function {func.__name__} output: {result}')
        return result
    return wrapper