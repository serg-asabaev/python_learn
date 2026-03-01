from functools import wraps
from typing import Callable, Union


def log(filename: str = "") -> Callable:
    """
    Декоратор логирующий успешные запуски функции и ошибки.
    Принимаетна вход адрес файла лога, а если он не задан ваводит текст лога в консоль
    """

    def wrapper(func: Callable) -> Callable:

        @wraps(func)
        def inner(
            *args: Union[str, int, float, None], **kwargs: Union[str, int, float, None]
        ) -> Union[str, int, float, None]:
            log_text = "Начало работы функции " + func.__name__ + "\n"
            res = None

            try:
                res = func(*args, **kwargs)
                log_text += func.__name__ + " ok\n"
            except Exception as e:
                this_args = list(args)
                this_args_res = []
                log_text += func.__name__ + " error: " + str(type(e).__name__) + ". "

                for arg in this_args:
                    str_arg = str(arg)
                    this_args_res.append(str_arg)

                log_text += "Inputs: (" + ", ".join(this_args_res) + "), {}\n"

            log_text += "Конец работы функции " + func.__name__

            if len(filename) > 0:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(log_text)
            else:
                print(log_text)

            return res

        return inner

    return wrapper
