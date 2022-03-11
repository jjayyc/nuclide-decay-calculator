""" Determines the type of particle decay of two elements and the daughter
nuclide of an element and a particle """

periodic_table = ["0", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
"Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr",
"Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
"Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
"Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu",
"Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os",
"Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac",
"Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No",
"Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc",
"Lv", "Ts", "Og"]
particles = {'4, 2' : 'alpha', '0, -1' : 'beta', '0, 1' : 'positron', '1, 0' :
'neutron', '1, 1' : 'proton', '0, 0' : 'gamma'}
particles_2 = {'alpha' : '4, 2', 'beta' : '0, -1', 'positron' : '0, 1',
'neutron': '1, 0', 'proton' : '1, 1', 'gamma': '0, 0'}

def type_of_decay(left_element, right_element):
    """
    Prints the type of decay of two elements

        Parameters:
                left_element (str): An element and its mass number (e.g. S-26)
                right_element (str): An element and its mass number (e.g. P-25)

        Prints:
                type of decay (str; e.g. proton)
    """
    left_element_split = left_element.split("-")
    atomic_number_left = periodic_table.index(left_element_split[0])
    mass_number_left = left_element_split[1]

    right_element_split = right_element.split("-")
    atomic_number_right = periodic_table.index(right_element_split[0])
    mass_number_right = right_element_split[1]

    atomic_difference = atomic_number_left - atomic_number_right
    mass_difference = int(mass_number_left) - int(mass_number_right)
    decay_number = str(mass_difference) + ", " + str(atomic_difference)

    for x in particles:
        if x == decay_number:
            print(particles[x])

def daughter_nuclide(left_element, particle):
    """
    Prints the daughter nuclide of an element and a particle

        Parameters:
                left_element (str): An element and its mass number (e.g. N-10)
                particle (str): A nuclear particle (e.g. proton)

        Prints:
                daughter nuclide element (str; e.g. C-9)
    """
    left_element_split = left_element.split("-")
    atomic_number_left = periodic_table.index(left_element_split[0])
    mass_number_left = left_element_split[1]

    particle = particles_2[particle]
    particle_split = particle.split(", ")
    mass_number_particle = particle_split[0]
    atomic_number_particle = particle_split[1]

    mass_number_dn = int(mass_number_left) - int(mass_number_particle)
    atomic_number_dn = atomic_number_left - int(atomic_number_particle)
    print(periodic_table[atomic_number_dn] + "-" + str(mass_number_dn))

# Should print 'proton' and 'C-9' respectively.
type_of_decay('S-26', 'P-25')
daughter_nuclide('N-10', 'proton')
