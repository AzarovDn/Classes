import weakref


class Animal:
    weight = 0  # kg
    want_to_eat = 'Yes'
    name = 'Unnamed'

    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def hungry(self):
        self.want_to_eat = 'No'


class Birds(Animal):
    eggs = 1  # ps.

    def collect_eggs(self):
        self.eggs = 0


class Animal_give_milk(Animal):
    have_milk = 100  # %

    def milk(self):
        self.have_milk = 0


class Sheeps(Animal):
    say = 'Бе-бе'
    need_to_cut = 100  # %

    def cut(self):
        self.need_to_cut = 0


class Cows(Animal_give_milk):
    say = 'Mууу'


class Goats(Animal_give_milk):
    say = 'Ме-ме'


class Geese(Birds):
    say = 'Га-га'


class Chikens(Birds):
    say = 'Ко-ко'


class Ducks(Birds):
    say = 'Кря-кря'


goose_gray = Geese(4, 'Серый')
goose_white = Geese(3, 'Белый')

cow = Cows(350, 'Манька')

sheep_barashek = Sheeps(150, 'Барашек')
sheep_kudryash = Sheeps(170, 'Кудрявый')

chiken_ko = Chikens(2, 'Ко-Ко')
chiken_ku = Chikens(2.5, 'Кукареку')

goat_roga = Goats(80, 'Рога')
goat_kopyta = Goats(75, 'Копыта')

duck = Ducks(2, 'Кряква')

animals = [goose_gray, goose_white, cow, sheep_barashek, sheep_kudryash, chiken_ko, chiken_ku, goat_roga, goat_kopyta,
           duck]

all_weight = 0
max_weight = 0
for animal in animals:
    all_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        heaviest_animal = animal.name

print('Суммарный вес всех животных {} кг'.format(all_weight))
print('Самое тяжелое животное {} весит {} кг.'.format(heaviest_animal, max_weight))


# вариант 2 решил через модуль, толком про него не чилал, но все работает.
import gc

all_weight_2 = 0
max_weight_2 = 0
heaviest_animal_2 = ''

for obj in gc.get_objects():
    if isinstance(obj, Animal):
        all_weight_2 += obj.weight
        if obj.weight > max_weight_2:
            max_weight_2 = obj.weight
            heaviest_animal_2 = obj.name

print('Вариант 2')
print('Суммарный вес всех животных {} кг'.format(all_weight_2))
print('Самое тяжелое животное {} весит {} кг.'.format(heaviest_animal_2, max_weight_2))


