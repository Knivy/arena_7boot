# main.py
from random import randint, choice

class Thing:
    """Вещи: class Thing Класс содержит в себе следующие параметры - название,
    процент защиты, атаку и жизнь; Это могут быть предметы одежды, магические
    кольца, всё что угодно)"""
    default_names = ['thing1, thing2, thing3, thing4, thing5']

    def __init__ (self, name, defense, attack, health):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.health = health

#Алгоритм проведения боя
def main():
    pass
    """
    Шаг 1 - создаем произвольное количество вещей с различными параметрами,
    процент защиты не должен превышать 10%(0.1). Сортируем по проценту защиты,
    по возрастанию;
    """
things_list = []

for i in range(randint(2, 5)):
    name = choice(Thing.default_names)
    defense = randint(0, 10)/100
    attack = randint(0, 100)/100
    health = randint(0, 100)/100
    things_list.append(Thing(name, defense, attack, health))
    print(things_list)
