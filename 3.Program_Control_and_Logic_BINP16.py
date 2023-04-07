'''
Created: 7/Apr/2023
Last Updated: 7/Apr/2023
Author: Clara Sigl

This script contains the answers for a number of exercises concerning collection data types from the course BINP16 (Programming in Python).
BINP16 is thaugt at Lund University, and the exercies were obtained from autumn 2022.
Note that the exercises have been modified somewhat to fit as standalone exercises (and not as a continuation of a previous exercise).

Exercise: You have received the following mRNA sequence, that consists of 10 codons: 
UAUAAACGAUACCAUUACUAUGACCAUGGG
You are interested in those codons that encode tyrosine. Knowing that they are "UAU" and "UAC", find out in which positions in the sequence
(what is the number of the codon, out of 10) tyrosine is encoded.
'''
def find_tyrosine(mRNA):
    if type(mRNA) == "str":
        codon_list = []
        position_list = []

        for a in range(0, len(mRNA), 3): #Divide the string into a codon list, with three amino acids in each element.
            codon_list.append(mRNA[a:a+3])
        
        if len(mRNA) % 3: #If the mRNA string is not divisible by 3, then remove the last codon (which contains less than three amino acids)
            codon_list = codon_list[0:-1]

        for iteration, codon in enumerate(codon_list, start=1): #start=1 means that the iteration will have a value of 1 at the start instead of 0.
            if codon == "UAU" or codon == "UAC":
                position_list.append(iteration)

        print(codon_list)
        print("The codons which encode tyrosine can be found in the following positions: {}".format(position_list))
    else:
        print("Please ensure that the input mRNA is a string.")

"""
Exercise: Write a script that asks the user to provide a DNA sequence and raises an exception if any non-nucleotide letter is found in the sequence.
The user is prompted to re-enter a DNA sequence until all of the nucleotides are valid. Display a message once a valid sequence has been entered successfully.
"""
def check_DNA(): 
    dna = input("Please type a DNA sequence: ")
    dna = dna.upper()
    acceptable_nucleotides = "ACGT"
    sequence_acceptable = False

    while sequence_acceptable == False:
        for iteration, amino_acid in enumerate(dna):
            if amino_acid not in acceptable_nucleotides: #If the current element in the string is not an acceptable amino acid.
                print("Your sequence contains an invalid nucleotide. Please try again.")
                dna = input("Please type a DNA sequence: ")
                break
            if iteration == len(dna)-1 and amino_acid in acceptable_nucleotides: #If the last element in the string is an acceptable amino acid.
                print("You have entered a valid DNA sequence.")
                sequence_acceptable = True
                break
