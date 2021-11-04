import time
import decor_8_extra

#1
@decor_8_extra.caching(timeout=2)
def discriminant(*args):
    """Функция вычисления дискриминанта"""
    a = args[0]
    b = args[1]
    c = args[2]
    value = (b ** 2) - (4 * a * c)
    return value

x = discriminant(4, 8, 2)

assert x is discriminant(4, 8, 2)
time.sleep(4)
assert x is not discriminant(4, 8, 2)


#2
lst_2 = [2, 10, 1, 7, 35]
result_2 = lambda x: sorted(x)[::-1] 
    
print(result_2(lst_2))



#3
lst_3 = ['Anton', 'Vikentiy', 'Vlodimir', 'Anna', 'Ekaterina']
result_3 = filter(lambda x: 't' in x, lst_3)
print(list(result_3))
