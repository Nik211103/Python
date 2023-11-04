def binary(list, s_item ):
    low = 0
    high = len(list) - 1
    s_res = False

    while low <= high and not s_res:
        midle = (low + high) // 2
        quess = list[midle]
        if quess == s_item:
            s_res = True
            return s_res
        if quess > s_item:
            high = midle - 1
        else:
            low = midle + 1
    return s_res
list = [3, 5, 11, 12, 15, 23, 25, 43, 67, 86]
value = 4
result = binary(list, value)
if result:
    print("Элемент найден")
else:
    print("Элемент не найден")