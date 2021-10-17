# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

fio = ['Ivan','Ivanov']
city = 'Minsk'
country = 'Belarus'

fio = ' '.join(fio)

print('\nПривет, {fio}! Добро пожаловать в {city} {country}'.format(fio = fio, city = city, country = country))
