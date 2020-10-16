from sys import argv

script_name = argv[0]
first_param = argv[1]
second_param = argv[2]
third_param = argv[3]


def func_salary(first_param, second_param, third_param):
    first_param = int(first_param)
    second_param = int(second_param)
    third_param = int(third_param)
    s = first_param * second_param + third_param
    return s


print('Название скрипта: ', script_name)
print('Выработка в часах: ', first_param)
print('Ставка в час: ', second_param)
print('Премия: ', third_param)
print(func_salary(first_param, second_param, third_param))
