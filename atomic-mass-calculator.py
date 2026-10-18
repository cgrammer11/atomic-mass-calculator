print("                                               ")
print("------------------------------ATOMIC MASS CALCULATOR------------------------------")
print("                                               ")

# this segment has the user enter in the details of how many
# subatomic particles they want for all three
amount_of_protons = int(input("Enter the amount of PROTONS: "))
amount_of_electrons = int(input("Enter the amount of ELECTRONS: "))
amount_of_neutrons = int(input("Enter the amount of NEUTRONS: "))

compute_atomic_number = (amount_of_protons)
compute_mass_number = (amount_of_protons + amount_of_neutrons)
compute_net_charge = (amount_of_protons - amount_of_electrons)

# this is a library containing ten elements from the periodic table of elements
# there are only ten to keep the program lightweight and easy to manage and edit
periodic_table = {
    "H": {"Name": "Hydrogen", "number": 1, "mass": 1.008},
    "He": {"Name": "Helium", "number": 2, "mass": 4.003},
    "C": {"Name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"Name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"Name": "Oxygen", "number": 8, "mass": 15.999},
    "Na": {"Name": "Sodium", "number": 11, "mass": 22.990},
    "Mg": {"Name": "Magnesium", "number": 12, "mass": 24.305},
    "Al": {"Name": "Aluminum", "number": 13, "mass": 26.982},
    "Si": {"Name": "Silicon", "number": 14, "mass": 28.085},
    "Fe": {"Name": "Iron", "number": 26, "mass": 55.845}
}


element_name = "Unknown Element (Not in our Top 10)"

# this segment determines the element depending on how subatomic particles there are
for symbol, data in periodic_table.items():
    if data["number"] == compute_atomic_number:
        element_name = data["name"]
        break


# this segment prints out the element, atomic number, mass number and the net charge
print("                                               ")
print("---------------------------------RESULTS---------------------------------")
print("Identified Element: {element_name}")
print("Atomic Number:      {compute_atomic_number}")
print("Atomic Mass Number: {compute_mass_number}")
print("Net Charge:         {compute_net_charge}")
print("-------------------------------------------------------------------------")
print("                                               ")


