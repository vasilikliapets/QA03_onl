def count_sill(text):
    """
    this function count repeateble letters
    "cccbba" == "c3b2a"
    """
    count = 1
    x = 1
    j = text[x:x + 1]
    for i in text:
        if i in j:
            count += 1

        else:
            print(i, end='')
            if count > 1:
                print(count, end='')
                count = 1
        x += 1
        j = text[x:x + 1]


# count_sill("cccbba")
# count_sill("abeehhhhhccced")
count_sill("aaabbceedd")
# count_sill("abcde")
# count_sill("aaabbdefffff")
