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

    health_modifier = 1
    defense_modifier = 1


class Warrior(Person):
    """Воин."""

    attack_modifier = 1
