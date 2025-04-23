import random

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    total: int = die1 + die2
    print(f"Dice A = {die1} and B = {die2}")
    print(f"Total of two dice A and B:", total, "\n")

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))


if __name__ == '__main__':
    main()