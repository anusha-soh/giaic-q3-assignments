#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def main():

    temp_in_farenheit = float(input("Enter temperature in farenheit: "))

    temp_in_celc = ((temp_in_farenheit - 32) * 5) / 9

    print(f"{temp_in_farenheit}F  is {temp_in_celc:.2f} Celsius!")


if __name__ == '__main__':
    main()