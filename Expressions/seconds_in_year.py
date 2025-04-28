# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

def main():
    year = int(input("Enter no of year(s): "))

    sec_in_year = year*365*24*60*60
    
    print(f"There are {sec_in_year} seconda in {year} year(s)")

if __name__ == '__main__':
    main()