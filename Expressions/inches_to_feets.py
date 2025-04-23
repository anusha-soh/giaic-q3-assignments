# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

''' 
this program covert inches into feet
'''

inches_per_foot = 12 

user_input = float(input("Enter length in inches: "))

def inch_to_feet():

    number_of_feet = user_input / inches_per_foot

    result = number_of_feet

    if result <= 1:
        print(f"There is {result:.2f} foot in {user_input} inches.") 
    elif result > 1:
        print(f"There are {result:.2f} feet in {user_input} inches.") 
    
    
    

def main():
    inch_to_feet()

if __name__ == '__main__':
    main()