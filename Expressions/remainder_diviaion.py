# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
import math
def div():
    num1 : float = float(input("Enter 1st num: "))
    num2 : float = float(input("Enter 2nd num: "))

    div: int = num1 // num2
    rem: float = num1 % num2

    print(f"{num1} divided by {num2} is {div} and its remainder is {rem}")
        


def main():
    div()
if __name__ == '__main__':
    main()