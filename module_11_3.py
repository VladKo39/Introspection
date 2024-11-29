
import pandas as pd
#from pprint import pprint

class Zheu:
    '''
    class Zheu: данные по ЖЭУ
    zheu: список участков
    sq_zheu: жилая площадь участков
    '''

    def __init__(self, *zheu):
        # метод устанавливаем атрибуты
        self.data_zheu = zheu
        self.sq_zheu = 0.00
        return

    def squ_zheu(self, name, *args, **kwargs):
        '''
        squ_zheu для подсчёта жилой прощади участка по запросу
        :param name: наименование участка
        :return: sum_squ - сумма жилой площади по участку
        '''
        self.name = name

        # Подготовка исходных данных по участку
        df_fond = pd.DataFrame(excel_data, columns=['Участок'])
        # удаление дубликатов .drop_duplicates()
        data_zheu = df_fond.drop_duplicates()
        np_array_zheu = data_zheu.to_numpy()
        data = np_array_zheu.tolist()
        data_zheu = []
        for str in data:
            for i in str:
                data_zheu.append(i)

        if not name in data_zheu:
            print("Нет значений")
            exit()

        # для упрощения работы закоментировал
        # licens = input('Считать площадь Зданий с лизензией или без лицензий?\n'
        #               'Введите да -с лизензией, нет-без лицензий ):')
        licens = 'да'
        df_sq_zheu = pd.DataFrame(excel_data, columns=['Участок', 'Общая площадь (кв.м.)',
                                                       'Наличие МКД в лицензии'])
        np_array_sq_zheu = df_sq_zheu.to_numpy()
        data = np_array_sq_zheu.tolist()
        dict_sq_zheu = {}
        for name_zheu in data_zheu:
            name_zheu = name_zheu.strip()
            for i in range(0, len(data)):
                list_data = data[i]
                if list_data[0] == name_zheu:
                    dict_sq_zheu.setdefault(name_zheu, []).append([list_data[1], list_data[2]])

        sum_squ = 0.00

        for element in dict_sq_zheu[self.name]:
            if element[1] == licens:
                sum_squ += element[0]
            else:
                sum_squ = sum_squ
        sum_squ = round(sum_squ, 2)
        return (sum_squ)


class AdressBuild(Zheu):
    def __init__(self, adress_build, *args, **kwargs):
        # метод устанавливаем атрибуты
        self.adress_build = adress_build

    def squ_build(self, adress_build, *args, **kwargs):
        self.adress_build = adress_build

        # Пдготовка исходных данных по участку
        df_fond = pd.DataFrame(excel_data, columns=['Адрес Здание'])
        # удаление дубликатов .drop_duplicates()
        data_build = df_fond.drop_duplicates()
        np_array_build = data_build.to_numpy()
        data = np_array_build.tolist()
        # print(data, type(data))
        data_build = []
        for str in data:
            for i in str:
                data_build.append(i)

        if not adress_build in data_build:
            print("Нет значений")
            exit()

        # для упрощения работы закоментировал
        # licens = input('Считать площадь Зданий с лизензией или без лицензий?\n'
        #               'Введите да -с лизензией, нет-без лицензий ):')
        licens='да'
        df_sq_build = pd.DataFrame(excel_data, columns=['Адрес Здание', 'Участок', 'Общая площадь (кв.м.)',
                                                        'Наличие МКД в лицензии'])
        np_array_sq_build = df_sq_build.to_numpy()

        data = np_array_sq_build.tolist()
        dict_sq_build = {}
        for name_build in data_build:
            name_build = name_build.strip()
            for i in range(0, len(data)):
                list_data = data[i]
                if list_data[0] == name_build:
                    dict_sq_build.setdefault(name_build, []).append([list_data[1], list_data[2], list_data[3]])

        sum_squ = 0.00

        for element in dict_sq_build[adress_build]:
            if element[2] == licens:
                sum_squ += element[1]
            else:
                sum_squ = sum_squ
        sum_squ = round(sum_squ, 2)
        return (sum_squ)


class AdressHouse(AdressBuild):
    def __init__(self):
        # метод устанавливаем атрибуты
        AdressBuild.__init__(self)
        return

    def sq_house(self):
        pass


class AdressFloat(AdressHouse):
    def __init__(self):
        # метод устанавливаем атрибуты
        AdressHouse.__init__(self)
        return


def data_base():
    '''
    считывание данных с файла xls для обсчёта в классах
    :return: excel_data
    '''
    global excel_data
    excel_data = pd.read_excel('Fond.xlsx')
    return excel_data


data_base()

instance_zheu = Zheu()
instance_build = AdressBuild(Zheu)
print('Запрос на общую жилую площадь по участкам:')
print(instance_zheu.squ_zheu('ЖЭУ "Сельма"'))
# print(instance_zheu.squ_zheu(input('Ведите участок(ЖЭУ "Невский",ЖЭУ "Сельма", ЖЭУ 11):')))
print()
print('Запрос на общую жилую площадь по Зданиям:')
print(instance_build.squ_build('ул. Береговая, д.16'))
# print(instance_build.(input.squ_build('Ведите адрес здания(Пример Вставить:ул. Береговая, д.16):')))

import inspect

def introspection_info(obj):
    '''
    возвращает словарь содержащий тип, модуль, атрибуты и методы объекта
    '''
    info = {'type': type(obj).__name__,
            'attributes': [],
            'methods': [],
            'module': []}

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

    print(f'{'*' * 20} Zheu  {'*' * 40}')
    pprint(introspection_info(Zheu), compact=True)

    print('*'*20, 'AdressBuild', '*'*20)
    pprint(introspection_info(AdressBuild(Zheu)), compact=True)

    print('*'*20, 'AdressHouse', '*'*20)
    pprint(introspection_info(AdressHouse), compact=True)
