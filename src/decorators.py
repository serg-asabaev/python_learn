from mmap import error
from functools import wraps


def write_to_file(filename: str, str_data: str):
    with open(filename, 'w', encoding='utf-8') as file:
        content_file = str_data
        file.write(content_file)


def log(predicate, filename: str = ''):

    def wrapper(func):

        @wraps(func)
        def inner(*args, **kwargs):
            log_text = 'Начало работы функции ' + func.__name__ + '\n'
            res = 0

            try:
                res = func(*args, **kwargs)
                log_text += func.__name__ + ' ok\n'
            except Exception as e:
                this_args = list(args)
                this_args_res = []
                log_text += func.__name__ + ' error: ' + str(type(e).__name__) + '. '

                for arg in this_args:
                    str_arg = str(arg)
                    this_args_res.append(str_arg)

                log_text += 'Inputs: (' + ', '.join(this_args_res) +'), {}\n'

            log_text +=  'Конец работы функции ' + func.__name__

            if len(filename) > 0:
                predicate(filename, log_text)
            else:
                print(log_text)

            return res

        return inner
    return wrapper