""" Project Storehouse """


class Equipment:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Printer(Equipment):
    def __init__(self, name, count, type_, model):
        super.__init__(name, count)
        self.type_ = type_
        self.model = model


class Scanner(Equipment):
    def __init__(self, name, count, type_, model):
        super.__init__(name, count)
        self.type_ = type_
        self.model = model


class Copier(Equipment):
    def __init__(self, name, count, type_, model):
        super.__init__(name, count)
        self.type_ = type_
        self.model = model


def warehouse():
    features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
    analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
    goods_all = {1: 'принтер', 2: 'сканер', 3: 'копир'}
    another_departments = {'Бухгалтерия': [], 'Дом': [], 'IT-шники': [], 'Директор': []}
    departure = {1: 'Бухгалтерия', 2: 'Дом', 3: 'IT-шники', 4: 'Директор'}
    while True:
        print('\nВыберите действие: ')
        print(' [1] Добавить товары на склад.')
        print(' [2] Переместить товары со склада.')
        print(' [3] Посмотреть наличие товаров на складе.')
        print(' [4] Посмотреть наличие товаров в отделах.')
        print(' [5] Выйти.')

        action = input('\nВыберите пункт: ')
        if action == '5':
            break
        elif action == '1':  # Добавляем на склад
            goods = []
            while True:
                if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
                    break
                for f in features.keys():
                    _ = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
                    try:
                        features[f] = int(_) if (
                                f == 'цена' or f == 'количество') else _  # Меняем тип числовых свойства
                    except ValueError:
                        print("Введите число")
                    analytics[f].append(features[f])  # Добавляем свойство в аналитику
                    goods.append(features)  # Добавляем свойство в список товаров
                print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
                for key, value in analytics.items():
                    print(f'{key[:25]:>30}: {value}')
                print("*" * 30)
        elif action == '2':  # Перемещение товаров со склада
            print('\nВыберите товар: ')
            for i, k in goods_all.items():
                print(f'[{i}] {k}')
            print('[4] Выход.')

            action = input('\nВыберите пункт: ')
            if action == '4':
                break

            print('\nВыберите куда перемещаем: ')
            for i, k in departure.items():
                print(f'[{i}] {k}')
            print('[5] Выход.')

            action_1 = input('\nВыберите пункт: ')

            if action_1 == '5':
                break
            else:
                if goods_all.get(int(action)) in analytics.get('название'):
                    m = analytics.get('название').index(goods_all.get(int(action)))
                    features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
                    for f in features.keys():
                        features[f] = analytics.get(f)[m]
                        tmp_value = analytics.get(f)
                        tmp_value[m] = None
                    print(f'Товары на складе: \n{analytics}')
                else:
                    print("Товар уже перемещен")
                another_departments[departure.get(int(action_1))] = features
                print(f'Товары в других отделах: \n{another_departments}')

        elif action == '3':  # Посмотреть наличие товаров на складе.
            print(analytics)
        elif action == '4':  # Посмотреть наличие товаров в отделах.
            print(another_departments)

    print('\nGoodbye!')


warehouse()
print(warehouse().analytics)
