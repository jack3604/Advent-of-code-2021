def main():
    nums = []
    with open("day1input.txt") as file:
        nums = [int(x.strip('\n')) for x in file.readlines()]

    windows = [[] for x in nums[:-2]]

    for i in range(len(nums[:-2])):
        windows[i].append(nums[i])
        windows[i].append(nums[i+1])
        windows[i].append(nums[i+2])
    
    sums = [sum(x) for x in windows]
    
    count = 0
    for i, n in enumerate(sums[1:]):
        if n > sums[i]:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
