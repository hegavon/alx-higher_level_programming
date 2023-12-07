#!/usr/bin/python3

def main():
rint("This Program illustrates a chaotic function")    x = eval(input("Enter a nuumber between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()
