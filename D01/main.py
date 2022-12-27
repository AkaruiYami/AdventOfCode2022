import os


def solution1(data):
    print(max(data))


def solution2(data):
    data.sort(reverse=True)
    print(sum(data[:3]))


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().split("\n\n")

    elves = [eval(_data.replace("\n", "+")) for _data in data]

    solution1(elves.copy())
    solution2(elves.copy())
