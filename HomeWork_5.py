class Animal:
    want_to_eat = 100  # %


    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def hungry(self, feed):
        self.want_to_eat -= feed  # Количество корма указываем в %


class Bird(Animal):
    eggs = 0

    def give_egg(self):
        self.eggs += 1
        self.want_to_eat += 20

    def collect_eggs(self):
        my_eggs += self.eggs
        self.eggs = 0


class AnimalGiveMilk(Animal):
    have_milk = 10  # Литры

    def milk(self):
        self.have_milk = 0
        my_milk += have_milk


class Sheep(Animal):
    say = 'Бе-бе'
    need_to_cut = 10  # см

    def cut(self, length):
        self.need_to_cut = self.need_to_cut - length
        my_wool += length * .2  # предположим, что каждый сантиметра шерсти, сбритый с поверхности овцы дает 200 грамм



class Cow(AnimalGiveMilk):
    say = 'Mууу'


class Goat(AnimalGiveMilk):
    say = 'Ме-ме'


class Goose(Bird):
    say = 'Га-га'


class Chiken(Bird):
    say = 'Ко-ко'


class Duck(Bird):
    say = 'Кря-кря'


goose_gray = Goose(4, 'Серый')
goose_white = Goose(3, 'Белый')

cow = Cow(350, 'Манька')

sheep_barashek = Sheep(150, 'Барашек')
sheep_kudryash = Sheep(170, 'Кудрявый')

chiken_ko = Chiken(2, 'Ко-Ко')
chiken_ku = Chiken(2.5, 'Кукареку')

goat_roga = Goat(80, 'Рога')
goat_kopyta = Goat(75, 'Копыта')

duck = Duck(2, 'Кряква')

animals = [goose_gray, goose_white, cow, sheep_barashek, sheep_kudryash, chiken_ko, chiken_ku, goat_roga, goat_kopyta,
           duck]

print ('Курица голодна на {} %'.format(chiken_ko.want_to_eat),'\n')

print ('Вызвали метод кормить','\n')

chiken_ko.hungry(30)

print ('Курица голодна на {} %'.format(chiken_ko.want_to_eat))

print ('У курицы {} яиц'.format(chiken_ko.eggs),'\n')

chiken_ko.give_egg()

print ('Вызвали метод, курица снесла яйцо','\n')

print ('Курица голодна на {} %'.format(chiken_ko.want_to_eat))

print ('У курицы {} яиц'.format(chiken_ko.eggs),'\n')


all_weight = 0
max_weight = 0
for animal in animals:
    all_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        heaviest_animal = animal.name

print('Суммарный вес всех животных {} кг'.format(all_weight))
print('Самое тяжелое животное {} весит {} кг.'.format(heaviest_animal, max_weight),'\n')


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


