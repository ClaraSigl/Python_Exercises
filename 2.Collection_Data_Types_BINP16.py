'''
Created: 12/Mar/2023
Last Updated: 13/Mar/2023
Author: Clara Sigl

This script contains the answers for a number of exercises concerning collection data types from the course BINP16 (Programming in Python).
BINP16 is thaugt at Lund University, and the exercies were obtained from autumn 2022.
Note that the exercises have been modified somewhat to fit as standalone exercises (and not as a continuation of a previous exercise).

Exercise: Create a list of all codons using the string "ACGT".
Codon: https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables
'''

def create_codon_table():
    #Each codon is three nucleotides (letters) long.
    #There are 64 codons in total.
    #16 of those codons will start with an A, 16 other with a C, and so on.
    nucleotides = "ACGT"
    codon_list = []
    for i in nucleotides:
        for j in nucleotides:
            for k in nucleotides:
                codon = str(i+j+k)
                codon_list.append(codon)
    return codon_list

'''
Exercise: Create a function which joins two dictionaries. The dictionaries should have the following structure: {string:int, string:int} where the integer represents the 
number of a given string. Ex: {"Bananas:5}
If the same key appears in both dictionaries, the integer should be the sum of the integers from each dictionary.
'''

def aggregate_dict(dict_1, dict_2):
    if type(dict_1) != dict or type(dict_2) != dict:
        return "Please enter two dictionaries as arguments."
    new_dict = {}
    try:
        for i in dict_1:
            new_dict[i] = dict_1[i]
        for j in dict_2:
            if j in new_dict: #If the key is in the new dictionary (and can thus also be found in dict_1)
                new_dict[j] += dict_2[j] #Update the value in the new dictionary.
            else:
                new_dict[j] = dict_2[j] #Add the new key to the new dictionary
        return new_dict
    except:
        return "Please make sure that both dictionaries have one digit as value per key."

"""
Exercise: Create a tab-separated text file containing the following two columns:
ProteinID ProteinSeq
prot1 AGSATGDASD
prot4 ASLWASLD
prot9 PPASDSADSAD
prot2 XXSWKJXS
prot8 PSOASSADASD

Then iterate through the file, printing only the protein IDs who's peptides has a tryptophane (W) in them.
"""

def create_tab_separated_file():
    tab_file = open("tab_file.txt", "w")
    tab_dict = {"ProteinID" : "ProteinSeq",
                "prot1" : "AGSATGDASD",
                "prot4" : "ASLWASLD",
                "prot9" : "PPASDSADSAD",
                "prot2" : "XXSWKJXS",
                "prot8" : "PSOASSADASD"}
    for proteinID in tab_dict:
        tab_file.write("{}\t{}\n".format(proteinID, tab_dict[proteinID])) #Write the key, a tab, the value of the key, then a newline.
    tab_file.close()

def print_W_IDs(inp_file):
    try:
        tab_file = open(inp_file)
        for line in tab_file:
            line = line.split("\t") #Separate the string (current line) into a list, separated at the tab.
            if "W" in line[1]: #If the protein sequence has a tryptophane.
                print(line[0])
        tab_file.close()
    except:
        return "Please make sure that the input is a tab-separated text file."
