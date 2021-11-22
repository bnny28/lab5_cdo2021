my_dict = {'key1': 1, 'key2': 2, 'key3': 3}
while True:
    key = input('Введите ключ словаря, или ~ для выхода: ')
    if key == '~':
        break
    else:
        val = my_dict.get(key)
        if val is None:
            print(f'В словаре нет значения для ключа "{key}"')
        else:
            print(f'Значение для ключа "{key}": ', val)
