from random import randint
class Soldier:
    def __init__(self, idt, team):
        self.idt = idt
        self.team = team

    def follow_hero(self, other):
        return self.idt, other.idt

class Hero:
    def __init__(self, idt, teambelong):
        self.idt = idt
        self.teambelong = teambelong
        self.level = 0
        self.team = []

    def __str__(self):
        return f'{self.idt}'

    def level_up(self):
        self.level += 1

h1 = Hero(123, 1)
h2 = Hero(789, 2)
idt = 0
for i in range(1, 9):
    a = randint(1, 2)
    if a == 1:
        h1.team.append(Soldier(idt, 1))
    else:
        h2.team.append(Soldier(idt, 2))
    idt += 1

if len(h1.team)>len(h2.team):
    h1.level_up()
else:
    h2.level_up()
print(h1.level)
print(h2.level)
print(h1.team)
print(h2.team)
print(h1.team[0].follow_hero(h1))