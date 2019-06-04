#!/usr/bin/python3

# Problem: Given a string of DNA, produce the reverse complement.

#Instantiate empty variables
DNA_string = ''
DNA_list = []
reverse_DNA_string = ''
reverse_complement_list = []
reverse_complement_string = ''

# Open the file and read it in as a string data type
with open('rosalind_revc.txt', 'r') as file1:
  DNA_string = file1.read().rstrip('\n')

# Reverse the input string by converting to a list by doing the following:
DNA_list = list(DNA_string)		# Convert the input string to a list
DNA_list.reverse()			# Reverse that list
reverse_DNA_string = ''.join(DNA_list)	# Join the reversed list into a string

# A generic replace method will not work here, so we must build the complement with a for loop
for i in range(len(reverse_DNA_string)):
  if reverse_DNA_string[i] == 'A':
    reverse_complement_list.append('T')
  elif reverse_DNA_string[i] == 'C':
    reverse_complement_list.append('G')
  elif reverse_DNA_string[i] == 'G':
    reverse_complement_list.append('C')
  elif reverse_DNA_string[i] == 'T':
    reverse_complement_list.append('A')
  else:
    continue

# Join the output list into an output string
reverse_complement_string = ''.join(reverse_complement_list)

# Print output
print(reverse_complement_string)
