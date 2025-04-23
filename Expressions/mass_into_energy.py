# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

def mass_to_energy():
    """
    This program gives the value when mass is converted into Energy 
    E = m * c**2

    Here c = 299792458 m/s is constant which is speed of light.
    """
    mass = float(input("Enter the mass of object in Kg: "))
    C = 299792458
    c_sqr = C**2

    energy = mass * c_sqr



    print(f"""
    e = m * C^2...
    m = {mass} kg
    C = 299792458 m/s

{mass} Kg of Mass converts to {energy} joules of energy.


""")

def main():
 
 mass_to_energy()

if __name__ == '__main__':
    main()