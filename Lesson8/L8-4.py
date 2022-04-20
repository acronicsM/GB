def val_checker(checker):
    def _checker(func):
        def wrapper(arg):
            if checker(arg):
                return func(arg)
            else:
                raise ValueError(f'wrong val {arg}')
        return wrapper
    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
