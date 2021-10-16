fraza1 = 'dogcat'
fraza2 = 'doGCat'

list = []
for i in fraza1:
    if i.isupper():
        list.append(i)
if len(list) == 0:
    print(True, list)
else:
    print(False, list)

list2 = []
for i in fraza2:
    if i.isupper():
        list2.append(i)
if len(list2) == 0:
    print(True, list2)
else:
    print(False, list2)