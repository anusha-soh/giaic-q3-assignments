# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def main():

    adj = input("Enter an Adjective: ")
    noun = input("Enter a Noun: ")
    verb = input("Enter a verb: ")

    print(f"I saw {adj}{noun}{verb} tomatos")

if __name__ == '__main__':
    main()