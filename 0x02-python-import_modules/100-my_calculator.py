#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def main():
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    num1, operator, num2 = map(int, argv[1:4])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
