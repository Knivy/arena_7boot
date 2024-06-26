"""Игра Арена."""

from random import randint, choice
from colorama import init, Fore
from faker import Faker


init()
fake = Faker()


class Thing:
    """
    Вещи.

    Класс содержит в себе следующие параметры - название,
    процент защиты, атаку и жизнь; Это могут быть предметы одежды, магические
    кольца, всё что угодно)
    """

    default_names = ['Кольцо запуска в космос',
                     'Плащ суперхита',
                     'Ожерелье красной ковровой дорожки',
                     'Браслет фанатов',
                     'Серьги славы',
                     'Кулон оскаровской статуэтки',
                     'Медальон с автографом королевы',
                     'Перстень с бриллиантом',
                     'Подвеска таблоидов',
                     'Брошь пресс-конференций',
                     'Заколка голливудской улыбки',
                     'Диадема модных показов',
                     'Тиара музыкальных фестивалей',
                     'Ободок дружбы',
                     'Венец популярности',
                     'Гребень таланта',
                     'Шпилька стиля',
                     'Зажим уверенности',
                     'Бантик социальных сетей',
                     'Резинка для волос трудолюбия',
                     'Барретка общения',
                     'Повязка для волос энергии',
                     'Лента скромности',
                     'Заколка благодарности',                                                                    
                     ]

    def __init__ (self, name, defense, attack, health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.health = health

        
class Person:
    """
    Класс персонажа.

    Персонаж: class Person Класс, содержащий в себе следующие параметры:
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. 
    Параметры передаются через конструктор; метод, принимающий на вход 
    список вещей set_things(things); метод вычитания жизни на основе 
    входной атаки, а также методы для выполнения алгоритма, представленного ниже;
    Паладин: class Paladin Класс наследуется от персонажа, при этом количество 
    присвоенных жизней и процент защиты умножается на 2 в конструкторе;
    Воин: class Warrior Класс наследуется от персонажа, при этом атака 
    умножается на 2 в конструкторе.
    """

    health_modifier = 1
    defense_modifier = 1
    attack_modifier = 1

    def __init__(self, name, health, base_attack, base_defense):
        self.name = name
        self.base_health = self.health_modifier * health
        self.base_attack = base_attack * self.attack_modifier
        self.base_defense = base_defense * self.defense_modifier  # %.
        self.things = []
        self.set_things(self.things)

    def set_things(self, things):
        self.things.extend(things)
        self.things = sorted(self.things, key=lambda x: x.defense)
        self.set_final_protection()
        self.set_final_attack()
        self.set_final_health()

    def remove_thing(self):
        thing = self.things.pop()
        self.set_final_protection()
        self.set_final_attack()
        self.set_final_health()  
        return thing     

    def set_final_protection(self):
        """
        Вычисляет защиту.

        Общий процент защиты (finalProtection) вычисляется по формуле 
        (базовый процент защиты + процент защиты от всех надетых вещей)
        """
        things_defense = sum([thing.defense for thing in self.things])
        self.final_protection = self.base_defense + things_defense

    def set_final_attack(self):
        things_attack = sum([thing.attack for thing in self.things])
        self.final_attack = self.base_attack + things_attack

    def set_final_health(self):
        things_health = sum([thing.health for thing in self.things])
        self.health = self.base_health + things_health

    def receive_attack_damage(self, attack_damage):
        """
        Вычисляет оставшееся здоровье.

        Жизнь вычитается по формуле 
        (HitPoints - (attack_damage - attack_damagefinalProtection)),
        где finalProtection - коэффициент защиты в десятичном виде;
        """
        final_damage = int(attack_damage * (1 - self.final_protection))
        self.health -= final_damage
        return final_damage


class Paladin(Person):
    """Паладин."""
    default_names = ['Paladin1', 'Paladin2', 'Paladin3', 'Paladin4', 'Paladin5']
    health_modifier = 1
    defense_modifier = 1


class Warrior(Person):
    """Воин."""
    default_names = ['Warrior1', 'Warrior2', 'Warrior3', 'Warrior4', 'Warrior5']

    attack_modifier = 1

    
#Алгоритм проведения боя
def main():
    """
    Шаг 1 - создаем произвольное количество вещей с различными параметрами,
    процент защиты не должен превышать 10%(0.1). Сортируем по проценту защиты,
    по возрастанию;
    """
    things_list = []
    persons_list = []

    for _ in range(randint(10, 20)):
        name = choice(Thing.default_names)
        defense = randint(0, 10)/100
        attack = randint(0, 100)/100
        health = randint(0, 100)/100
        thing = Thing(name, defense, attack, health)
        things_list.append(thing)
    
    for _ in range(10):
        health = randint(50, 100)
        base_attack = randint(50, 100)
        base_defense = randint(0, 10) / 100

        if randint(0, 1) == 1:
            name = fake.first_name_male()
            person = Warrior(name, health, base_attack, base_defense)
        else:
            name = fake.first_name_female()
            person = Paladin(name, health, base_attack, base_defense)

        persons_list.append(person)
    
    for person in persons_list:
        things = [choice(things_list) for _ in range(randint(1, 4))]
        person.set_things(things)

    while len(persons_list) > 1:
        event = choice([1, 2, 3])
        flag_event3 = False
        attacker = choice(persons_list)
        if event == 1:
            defender = attacker
        else:
            defense_pool = persons_list[:]
            defense_pool.remove(attacker)
            defender = choice(defense_pool)
            if event == 3:
                defense_pool.remove(defender)
                if len(defense_pool) > 0:
                    second_attacker = choice(defense_pool)
                    flag_event3 = True
        if event == 2:
            person = choice([attacker, defender])
            if len(person.things) > 0:
                thing = person.remove_thing()
                print(f'Подул ветер и {person.name} теряет вещь: {thing.name}.')
        damage = defender.receive_attack_damage(attacker.final_attack)
        if event == 1:
            print(f'{attacker.name} неуклюже ранит себя на {damage} урона.')
        else:
            print(f'{attacker.name} наносит удар по {defender.name} на {damage} урона.')
        if defender.health <= 0:
            print(Fore.RED + f'{defender.name} покидает арену.' + Fore.RESET)
            persons_list.remove(defender)
        if flag_event3 and defender in persons_list:
            damage = defender.receive_attack_damage(second_attacker.final_attack)
            print(f'{second_attacker.name} решает присоединиться и наносит {damage} урона.')
            if defender.health <= 0:
                print(Fore.RED + f'{defender.name} покидает арену.' + Fore.RESET)
                persons_list.remove(defender)

    print(Fore.GREEN + f'Побеждает {persons_list[0].name}.')


if __name__ == '__main__':
    main()
