# Напишите функцию, которая вычисляет сложное математическое выражение и
# оберните ее декоратором из пунктов 1, 2
from task8_1 import decorator_print
from task8_2 import decorator_add


@decorator_print
@decorator_add
def complex_math_expression(x,y):
    result = x ** y / y + x * y * 0.2
    return result


complex_math_expression(5, 7)