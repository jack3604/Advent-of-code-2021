class sub:
    def __init__(self, x, y, aim):
        self.x = x
        self.y = y
        self. aim = aim

    def forward(self, n):
        self.x += n
        self.y += self.aim * n

    def up(self, n):
        self.aim -= n

    def down(self, n):
        self.aim += n


def main():
    lines = []
    x = 0
    y = 0
    aim = 0
    test_sub = sub(x, y, aim)

    with open("day2input.txt") as file:
        lines = [x.strip('\n').split() for x in file.readlines()]

    for set in lines:
        n = int(set[1])
        if set[0] == 'forward':
            test_sub.forward(n)
        if set[0] == 'up':
            test_sub.up(n)
        if set[0] == 'down':
            test_sub.down(n)

    print(test_sub.x * test_sub.y)


if __name__ == "__main__":
    main()
