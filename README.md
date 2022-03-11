# nuclide-decay-calculator
**Determines the type of particle decay of two elements and the daughter nuclide of an element and a particle**

I made this program to help me with my homework in nuclear pharmacy. For the first function, `type_of_decay`, the user calls the function and inputs two elements
with their mass numbers:

`type_of_decay('S-26', 'P-25')`

The function then prints the corresponing particle decay. This is done by subtracting the mass number and atomic number of the second element to the first element then
matching the result to the particle that has the same values. For the second function, the user calls it by typing in an element with its mass
number and a particle in order to get their daughter nuclide:

`daughter_nuclide('N-10', 'proton')`

