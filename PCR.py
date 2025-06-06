from random import randint

proteins = ["A", "T", "G", "C", "*"]

comp_dna_seq = []
clone_dna = []

print("This PCR can create, analyze, and clone DNA of length 25 only.")
print("------------------------------------------------------------------------------------")

def DNA_seq_creator(chain=25):
    dna_seq = []
    for _ in range(chain):
        dna_seq.append(proteins[randint(0, 4)])
    return dna_seq

print("Random DNA sample generated for conducting PCR.")
print("Conducting PCR (Step 1 of 3: Denaturation):")
print("Cranking up heat upto 95 degrees celsius.....Success")
print("------------------------------------------------------------------------------------")

def perform_denat():
    while True: #creating infinite loop here
        dna_seq = DNA_seq_creator()
        defec = dna_seq.count("*")
        ndefec = len(dna_seq) - defec

        if (defec / ndefec) <= 0.25:
            print("Separating double strands.....Success")
            print("----------------------------------------------------------------------------")
            return dna_seq  # Breaking the loop here. So only return successful DNA.
        else:
            print("Separating double strands.....Failure")
            print("Re-executing the process...") 
            print("----------------------------------------------------------------------------")
            # Loop not broken here. So again...

dna_seq = perform_denat()

print("Your DNA sample is:\n" + "".join(dna_seq))

for protein in dna_seq:
    if protein == "A":
        comp_dna_seq.append("T")
    elif protein == "T":
        comp_dna_seq.append("A")
    elif protein == "G":
        comp_dna_seq.append("C")
    elif protein == "C":
        comp_dna_seq.append("G")
    else:
        comp_dna_seq.append("*")

comp_dna_seq_str = str("".join(comp_dna_seq))

def perform_anl():
    while True:
        primer = input("Enter Primer for cloning: ").upper()

        if primer in comp_dna_seq_str:
            print("Cloning location found. >>> Continuing PCR (Step 2 of 3: Annealing)")
            print("Lowering heat to 60 degrees celsius.....Success")
            print("Attaching Primer to DNA.....Success")
            print("----------------------------------------------------------------------------")
            clone_point = comp_dna_seq_str.find(primer)
            return clone_point
        else:
            print("No suitable location for PCR continuation with given primer")
            print("Please enter a different primer.")
            print("----------------------------------------------------------------------------")


clone_point = perform_anl()

def perform_ext():
    clone_dna = "".join(comp_dna_seq[clone_point:]) #performing extension
    print("Polymerase has been introduced. Continuing PCR (Step 3 of 3: Extension)")
    if "*" in clone_dna:    
        print("Error genome found. Conducting Immediate DNA cleavage.....Success")
        print("Healthy DNA sequence single clone creation.....Success")
        print("----------------------------------------------------------------------------")
        error_point = clone_dna.find("*")
        clone_dna_fin = clone_dna[:error_point]
        return clone_dna_fin
    else:
        print("Healthy DNA sequence single clone creation.....Success")
        print("----------------------------------------------------------------------------")
        return clone_dna    
    
req_dna = perform_ext()

rpt = int(input("How many cycle do you need to perform? \n"))


print("------------------------------------------------------------------------------------")
for i in range(rpt):
    print(req_dna)
print("------------------------------------------------------------------------------------")
print("Time taken =", str(rpt * 2.5), "minutes")