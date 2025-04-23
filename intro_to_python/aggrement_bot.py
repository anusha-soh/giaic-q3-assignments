#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course). Here's a sample run of the 

def main():

    fav_animal = input("What's your favorite animal? ")
    print(f"My favorite animal is {fav_animal} too!")

if __name__ == '__main__':
    main()