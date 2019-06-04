#!/usr/bin/python3
# Problem: count the number of occurrences of each nucleotide base in a given string.
# Instantiate empty variables
data = ''
base_a = ''
base_c = ''
base_g = ''
base_t = ''

# Open dataset, using the read() method to bring in the entire file as a string.
with open('rosalind_dna.txt', 'r') as file1:
  data = file1.read()

# Count the different nucleotide bases
base_a = data.count('A')
base_c = data.count('C')
base_g = data.count('G')
base_t = data.count('T')

# Return or print statement
print(base_a, base_c, base_g, base_t)
