# Ask the user for a number and print its square (the product of the number times itself).

def main():

    

    num = float(input("Enter a number to square: "))
    
    sq_num = num * num

    print(f"The square of {num} is {sq_num}.")



if __name__ == '__main__':
    main()