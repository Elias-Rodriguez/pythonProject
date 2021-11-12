# TODO: Import math module
import math


def quadratic_formula(a, b, c):
    # TODO: Compute the quadratic formula results in variables x1 and x2

    # Split Quadratic Formula in parts
    part1 = -(b)
    part2 = b ** 2
    part3 = 4 * a * c
    part4 = math.sqrt(part2 - part3)
    part5 = part1 + part4
    part6 = part1 - part4

    # Put Parts together to compute easier
    x1 = part5 / (2 * a)
    x2 = part6 / (2 * a)

    return (x1, x2)


def print_number(number, prefix_str):
    if float(int(number)) == number:
        print("{}{:.0f}".format(prefix_str, number))
    else:
        print("{}{:.2f}".format(prefix_str, number))


if __name__ == "__main__":
    input_line = input("Give the three values of variables a , b , and c:")
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    print("Solutions to {:.0f}x^2 + {:.0f}x + {:.0f} = 0".format(a, b, c))
    print_number(solution[0], "x1 = ")
    print_number(solution[1], "x2 = ")