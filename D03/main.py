import os
import string


def split_half(str1):
    n = len(str1)
    half = n // 2
    return str1[:half], str1[half:]


def get_priority(char1):
    letters = string.ascii_letters
    return letters.find(char1) + 1


def solution1(data):
    total = 0
    for line in data:
        compartment1, compartment2 = split_half(line)
        common = set(compartment1).intersection(set(compartment2))
        total += get_priority(common.pop())
    print(total)


def solution2(data):
    total = 0
    for i in range(0, len(data), 3):
        line1 = set(data[i])
        line2 = set(data[i + 1])
        line3 = set(data[i + 2])
        common = line1.intersection(line2, line3)
        total += get_priority(common.pop())
    print(total)


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()

    solution1(data)
    solution2(data)
