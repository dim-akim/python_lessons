class Arena:
    def __init__(self, n):
        self.gladiators = [None] * n

    def add(self, fighter):
        self.gladiators[fighter.n - 1] = fighter

    @property
    def strongest(self):
        return max(self.gladiators)

    def start_battle_for(self, gladiator):
        if gladiator.is_alive:
            gladiator.buff()
            gladiator.fight_all()

    def battle(self):
        for gladiator in self.gladiators:
            self.start_battle_for(gladiator)

    @property
    def winner(self):
        strongest = self.strongest
        return f'{strongest}'

    @property
    def dead(self):
        return len(self.gladiators) - len([fighter for fighter in self.gladiators if fighter.power > 0])

    def get_gladiator(self, n):
        return self.gladiators[n - 1]


class Gladiator:
    def __init__(self, data):
        self.n = data[0]
        self.power = data[1]
        self.friend = data[2]
        self.enemies = data[3:]

    @property
    def is_alive(self):
        return self.power > 0

    def buff(self):
        target = arena.get_gladiator(self.friend)
        if target.is_alive:
            target.power += self.power
            print(f'{self} buffed {target}')
        else:
            print(f'{self} friend is already DEAD')

    def fight_all(self):
        if self.is_alive:
            for i in self.enemies:
                enemy = arena.get_gladiator(i)
                self.fight(enemy)
        else:
            print(f'{self} is already DEAD')

    def fight(self, target):
        if self.is_alive and target.is_alive:
            if self.power > target.power:
                winner = self
                looser = target
            elif self.power == target.power:
                winner = looser = self
            else:
                winner = target
                looser = self
            if winner == looser == self:
                print(f'{self} and {target} are both in VALHALLA')
                self.power = target.power = 0
            else:
                print(f'{winner} defeated {looser}')
                looser.power = 0
                winner.power -= winner.power // 3

    def __repr__(self):
        return f'<Gladiator #{self.n} with power={self.power}>'

    def __lt__(self, other):
        return self.power < other.power

    def __gt__(self, other):
        return self.power > other.power

    def __eq__(self, other):
        return self.n == other.n

with open('26_19599.txt') as file:
    arena = Arena(int(file.readline()))
    for line in file:
        arena.add(Gladiator([int(i) for i in line.split()]))

print(len(arena.gladiators))
print(arena.gladiators)

arena.battle()
print(f'{arena.dead=} {arena.winner=}')
