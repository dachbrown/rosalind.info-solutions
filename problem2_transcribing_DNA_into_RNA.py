#/usr/bin/python3

# Problem: Given a DNA string, transcribe an RNA string, replacing all 'T' with 'U'

# Instantiate empty variables
DNA_data = ''
RNA_data = ''

# Open the file and read it in.
with open('rosalind_rna.txt', 'r') as file1:
  DNA_data = file1.read()

# Transcribe the string
RNA_data = DNA_data.replace('T', 'U')

# Output answer
print(RNA_data)
