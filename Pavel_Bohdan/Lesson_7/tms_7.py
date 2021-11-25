import imp_7
import imp_7_2
#import imp_7 as bank_run
import random


#vibor = str(input('Выберите программу: Bank либо Shifr '))


def choice():
    
    vibor = str(input('Выберите программу: Bank либо Shifr '))
    if vibor == 'Bank':
        imp_7.run_bank()
    elif vibor == 'Shifr':
        imp_7_2.run_code()
    else:
        print('Выбрана несуществующая программа')       


count = 1
flag = True
while flag:
    if count <= 3:
        vibor = str(input('Выберите программу: Bank либо Shifr '))
        if vibor == 'Bank':
            imp_7.run_bank()
            choice()
        elif vibor == 'Shifr':
            imp_7_2.run_code()
            choice()
        else:
            count += 1
            print('Выбрана несуществующая программа')
    else:
        flag = False
        random.choice([imp_7.run_bank, imp_7_2.run_code])()







  
   

