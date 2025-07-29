class Gladiator:
    def __init__(self, data):
        self.n = data[0]
        self.power = data[1]
        self.friend = data[2]
        self.enemies = data[3:]

    @property
    def is_alive(self):
        return self.power > 0

    @staticmethod
    def get_gladiator(n):
        return gladiators[n - 1]

    def buff(self):
        target = self.get_gladiator(self.friend)
        if target.is_alive:
            target.power += self.power
            print(f'{self} buffed {target}')
        else:
            print(f'{self} friend is already DEAD')

    def fight_all(self):
        if self.is_alive:
            self.buff()
            for i in self.enemies:
                enemy = self.get_gladiator(i)
                self.fight(enemy)
        else:
            print(f'{self} is already DEAD')

    def fight(self, target):
        if self.is_alive and target.is_alive:
            if self.power == target.power:
                print(f'{self} and {target} are both in VALHALLA')
                self.power = target.power = 0
                return
            elif self > target:
                winner = self
                looser = target
            else:
                winner = target
                looser = self

            print(f'{winner} defeated {looser}')
            looser.power = 0
            winner.power -= winner.power // 3

    def __repr__(self):
        return f'<Gladiator #{self.n} with power={self.power}>'

    def __gt__(self, other):
        return self.power > other.power

    def __eq__(self, other):
        return self.n == other.n


with open('26_19599.txt') as file:
    gladiators = [None] * int(file.readline())
    for line in file:
        fighter = Gladiator([int(i) for i in line.split()])
        gladiators[fighter.n - 1] = fighter

for fighter in gladiators:
    fighter.fight_all()

alive = [g for g in gladiators if g.power > 0]
strongest = max(alive)

print(f'fallen={len(gladiators) - len(alive)} {strongest=}')
