def main():
    lines = []
    x = 0
    y = 0
    with open("day2input.txt") as file:
        lines = [x.strip('\n').split() for x in file.readlines()]

    for set in lines:
        n = int(set[1])
        if set[0] == 'forward':
            x += n
        if set[0] == 'up':
            y -= n
        if set[0] == 'down':
            y += n

    print(x * y)


if __name__ == "__main__":
    main()
