from datetime import datetime
import os

path = 'C:\\Users\\julko\\PycharmProjects\\decor'


def param_decor(parameter):
    def decor(old_function):
        def new_function(*args, **kwargs):
            with open(os.path.join(parameter, 'data.txt'), 'a', encoding="utf-8") as file:
                time = str(datetime.now())
                function_name = new_function.__name__
                result = old_function(*args, **kwargs)
                string = f'В {time} вызвана функция {function_name} со следующими аргументами {args}. ' \
                         f'Результат работы функции равен {result}'
                file.write(string + '\n')
                return result
        return new_function
    return decor



nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

@param_decor(parameter=path)
def flat_generator(nested_list):
    for el in sum(nested_list, []):
        yield el

for item in  flat_generator(nested_list):
	print(item)