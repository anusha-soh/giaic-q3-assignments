# Simulate rolling two dice, and prints results of each roll as well as the total.
import random
def main():

    roll1 = random.randint(1 , 6)
    roll2 = random.randint(1 , 6)

    total = roll1 + roll2

    print(f"""
          Roll 1 is '{roll1}'
          Roll 2 is '{roll2}'
          total of two dice is {total}. 
          """)




if __name__ == '__main__':
    main()