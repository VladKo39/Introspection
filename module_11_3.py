import inspect

def introspection_info(obj):
    '''
    возвращает словарь содержащий тип, модуль, атрибуты и методы объекта
    '''
    info = {'type': type(obj).__name__,
            'attributes': [],
            'methods': []}

    for name in dir(obj):
        if callable(getattr(obj, name)):
            info['methods'].append(name)
        else:
            info['attributes'].append(name)

    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        info['module'] = __name__
    else:
        info['module'] = obj_module.__name__

    return info


if __name__ == '__main__':
    from pprint import pprint

    print(f'{'*'*20} 42 {'*'*40}')
    pprint(introspection_info(42), compact=True)
    print()

    print(f'{'*' * 20} introspection_info {'*' * 40}')
    pprint(introspection_info(introspection_info), compact=True)
    print()

    import gkh

    print(f'{'*' * 20} gkh  {'*' * 40}')
    pprint(introspection_info(gkh), compact=True)

    print('*'*20, 'float', '*'*20)
    pprint(introspection_info(float), compact=True)

''' Сохранение для дальнейшей обработки
 # print('Запрос на общую жилую площадь по участкам:')
    # zapr_zhey=gkh.instance_zheu.squ_zheu
    # print(zapr_zhey(input('Ведите участок(ЖЭУ "Невский",ЖЭУ "Сельма", ЖЭУ 11):')))
    # print()
    # print('Запрос на общую жилую площадь по Зданиям:')
    # zapr_build = gkh.instance_build.squ_build
    # print(zapr_build(input('Ведите адрес здания(Пример Вставить:ул. Береговая, д.16):')))

'''