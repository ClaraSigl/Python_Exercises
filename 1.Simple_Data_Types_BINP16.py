'''
Created: 05/Feb/2023
Author: Clara Sigl

This script contains the answers for a number of exercises concerning simple data types from the course BINP16 (Programming in Python).
BINP16 is thaugt at Lund University, and the exercies were obtained from autumn 2022.

'''
import random
import re

'''
Exercise: Ask the user for a nucleotide sequence, mutate a random (real random) nucleotide and print it. 
'''
#Of note, true randomness cannot be achieved in Python.

def mutate_seq(rna_seq = False):
    inp_seq = input("Enter a nucleotide sequence: ")
    non_nucleotides = re.compile("[^ACGTUacgtu]")
    check_for_none_nt = re.findall(non_nucleotides, inp_seq)
    if len(check_for_none_nt) != 0:
        print("Please enter a nucleotide sequence.")
        return None

    inp_seq = inp_seq.upper()
    out_seq = list(inp_seq)
    nucleotides = "ACGT"
    mutation_occured = False #Changes into True when a mutation has occured.

    while mutation_occured == False: #This loop ensures that the old nucleotide is not replaced with an identical one.
        pos = random.randrange(0, len(inp_seq)) #pos = position of nucleotide which will mutate in the input sequence.
        new_nt = random.choice(nucleotides) #The nucleotide which the old nucleotide will mutate into.
        if out_seq[pos] != new_nt: #If there will be a noticable mutation, then break the loop and mutate the output sequence.
            mutation_occured = True
            out_seq[pos] = new_nt
            out_seq = "".join(out_seq)
    
    if rna_seq == True: #If you define rna_seq as true then convert every T to U.
        inp_seq = re.sub("T", "U", inp_seq)
        out_seq = re.sub("T", "U", out_seq)
    print("Input sequence: {}\nOutput sequence: {}".format(inp_seq, out_seq))

'''
Exercise: Print every prime number with a value less than or equal to a given value n.
'''
def print_prime(n):
    #A prime number is an integer above 1 that is not a product of two smaller natural numbers.
    numbers = list(range(1, n+1))
    for i in range(len(numbers)):
        is_prime = True
        lower_numbers = list(range(2, i+1))
        for j in range(len(lower_numbers)):
            if numbers[i]%lower_numbers[j] == 0: #If the current number is divisible by any number below it.
                is_prime = False
                break
        if is_prime == True and numbers[i] != 1: #1 is not a prime number.
            print(numbers[i])

