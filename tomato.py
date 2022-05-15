class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Перевод томата на следующую фазу созревания
    def grow(self):
        self._change_state()

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    # Проверяем, созрел ли томат (достиг последней стадии созревания)
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _print_state(self):
        print(f'Томат {self._index} - {Tomato.states[self._state]}')

class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил работу')

    # Собираем урожай
    def harvest(self):
        print('Сбор урожая...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен')
        else:
            print('Слишком рано! Ваше растение зеленое и незрелое.')

    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''В идеале время сбора урожая томатов должно наступать,
когда плод становится зрелым зеленым, а затем ему дают
созреть на лозе. Это предотвращает расщепление или 
образование синяков и позволяет в определенной степени
контролировать процесс созревания.''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()