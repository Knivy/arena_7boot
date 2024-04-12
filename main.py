from random import randint, choice

class Thing:
    """
    Вещи
    
    Класс содержит в себе следующие параметры - название,
    процент защиты, атаку и жизнь; Это могут быть предметы одежды, магические
    кольца, всё что угодно)
    """
    default_names = ['thing1, thing2, thing3, thing4, thing5']

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
        self.health = self.health_modifier * health
        self.base_attack = base_attack * self.attack_modifier
        self.base_defense = base_defense * self.defense_modifier  # %.
        self.things = []

    def set_things(self, things):
        self.things.extend(things)

    def set_final_protection(self):
        """
        Вычисляет защиту.

        Общий процент защиты (finalProtection) вычисляется по формуле 
        (базовый процент защиты + процент защиты от всех надетых вещей)
        """
        things_defense = sum([thing.defense for thing in self.things])
        self.final_protection = self.base_defense + things_defense

    def receive_attack_damage(self, attack_damage):
        """
        Вычисляет оставшееся здоровье.

        Жизнь вычитается по формуле 
        (HitPoints - (attack_damage - attack_damagefinalProtection)),
        где finalProtection - коэффициент защиты в десятичном виде;
        """
        self.set_final_protection()
        final_damage = attack_damage * (1 - self.final_protection())
        self.health -= final_damage
        return final_damage


class Paladin(Person):
    """Паладин."""
    default_names = ['Paladin1, Paladin2, Paladin3, Paladin4, Paladin5']
    health_modifier = 1
    defense_modifier = 1


class Warrior(Person):
    """Воин."""
    default_names = ['Warrior1, Warrior2, Warrior3, Warrior4, Warrior5']

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
        health = randint(0, 100)
        base_attack = randint(0, 100)
        base_defense = randint(0, 100)

        if randint(0, 1) == 1:
            name = choice(Warrior.default_names)
            person = Warrior(name, health, base_attack, base_defense)
        else:
            name = choice(Paladin.default_names)
            person = Paladin(name, health, base_attack, base_defense)

        persons_list.append(person)
    
    for person in persons_list:
        things = [choice(things_list) for _ in range(randint(1, 4))]
        person.things = things

main()