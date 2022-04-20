def type_logger(func):
    def wrapper(*args, **kwargs):
        print(f'Call for: {func.__name__}')

        if len(args) > 0:
            print(f'{args[0]}: {type(args[0])}')

        x = ', '.join([f'{key} = {value}: {type(value)}' for key, value in kwargs.items()])
        if x != '':
            print(x)

        result = func(*args)

        print(f'Rezulst: {result} type: {type(result)}\n')

        return result
    return wrapper


@type_logger
def render_input(*args):
    return 1


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5)
render_input(d=1, a=2, b=True, c="q")
