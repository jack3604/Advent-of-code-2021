def main():
    with open("day1input.txt") as file:
        nums = [int(x.strip('\n')) for x in file.readlines()]
        count = 0
        for i, n in enumerate(nums[1:]):
            if n > nums[i]:
                count += 1
        print(count)


if __name__ == "__main__":
    main()
