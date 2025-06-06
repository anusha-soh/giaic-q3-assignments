# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):


def main():

    anton = 21

    beth = anton + 6  

    chen = beth + 20

    drew = chen + anton

    ethan = chen


    print(f"Anton is {anton} years old.")
    print(f"Beth is years {beth} old.")
    print(f"Chen is years {chen} old.")
    print(f"Drew is years {drew} old.")
    print(f"Ethen is years {ethan} old.")


if __name__ == '__main__':
    main()