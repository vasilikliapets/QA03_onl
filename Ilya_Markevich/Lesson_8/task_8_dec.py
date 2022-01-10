import time


def dec_1(func):
    """декоратор, который печатает перед и после вызова функции слова “Before” and “After”"""

    def wrapper(*args):
        print("Before")
        res = func(*args)
        print("After")
        return res

    return wrapper
  
  
  def dec_6(func):
    """декоратор, который вычисляет время работы декорируемой функции (timer)"""

    def wrapper(*args):
        start_time = time.perf_counter()
        val = func(*args)
        print('time', time.perf_counter() - start_time)
        return val

    return wrapper



def dec_2(func):
    """функция декоратор, которая добавляет 1 к заданному числу"""

    def wrapper(*args):
        number = func(*args) + 1
        print(number)

    return wrapper


def dec_3(func):
    """Переводит полученную строку в верхний регистр"""

    def wrapper(text):
        print(text.upper())

    return wrapper
  
  

  def dec_5(func):
    """функция принимает все свои не именованные аргументы в порядке, обратном тому, в котором их передали"""

    def wrapper(*args):
        li = args[::-1] 
        return func(li)

    return wrapper



  def dec_4(func):
    """декоратор func_name, который выводит на экран имя функции
    (func.__name__)"""

    def wrapper(*args):
        print(func.__name__)
        print(func(*args))

    return wrapper
  
  
