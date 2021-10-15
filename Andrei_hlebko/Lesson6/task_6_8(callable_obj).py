# написать функцию, которая проверяет есть ли в списке объект, которые можно вызвать
def callable_obj(text):
    for i in text:
        if callable(i):
            return True


print(callable_obj([1, 2, "a", (1, 2), "b", int]))#True
print(callable_obj([1, 2, "a", (1, 2), "b"]))#None
