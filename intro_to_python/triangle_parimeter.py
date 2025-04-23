# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).


def main():

    print("Find out parimeter of your triangle!!") 

    s1 = float(input("What is the length of side 1: "))
    s2 = float(input("What is the length of side 2: "))
    s3 = float(input("What is the length of side 3: "))

    parimeter = s1 + s2 + s3

    print(f"he perimeter of the triangle is {parimeter}")

    

if __name__ == '__main__':
    main()