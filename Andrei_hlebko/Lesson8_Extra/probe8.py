#
# stroka = lambda  name: f"Hello {name}"
# print(stroka("Vasil"))


# names = ["Andry","Vasya","Oleg","Sasha","Masha","Maxim"]
# check_t = filter(lambda lit: if check_t in names,)
# print(check_t("i"))
#
#
# func_l3 = (lambda list_names: [f"Hello {i}" for i in names])
# print(func_l3(names))


# result = map(lambda x: x + 4, [1, 2, 3, 4, 5, 6])
# print(list(result))


# spisok = [1, 2, 3, 4, 5, 6, 7]
# result = map(lambda x: str(x), spisok)
# print(list(result))

# result = filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9])
# print(list(result))


# names = ["Andry","Veronika","Oleg","Sasha","Masha","Maxim"]
#
# result = filter(lambda x: 'i' in x, names)
# print(list(result))

def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                time.sleep(4)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)


#
# #@caching(timeout=3)
# import time
#
#
# def func(x):
#     return {x: 42}
#
#
# x = func(2)
# assert x is func(2)
# time.sleep(4)
# assert x is not func(2)