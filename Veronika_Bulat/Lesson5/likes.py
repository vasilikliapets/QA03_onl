# 2. Likes

def likes(names):
    if (len(names) != 0):
        names_list = names.split(',')
        if len(names_list) > 3:
            print('{} and {} others like this'.format(','.join(names_list[:2:]), len(names_list) - 2))
        elif len(names_list) > 1:
            print('{} and {} like this'.format(','.join(names_list[:-1:]), names_list[-1].strip()))
        else:
            print('{} likes this'.format(names_list[0]))
    else:
        print('No one likes this')


likes(input('Enter names separated by commas: '))
