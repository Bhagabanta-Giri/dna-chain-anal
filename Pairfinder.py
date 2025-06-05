# 💘 Pair Finder: Like Tinder, but for lonely nucleotides.

org_dna_seq = input("Please input the DNA sequence: ")

# Our matchmaker's toolkit
comp_dna_seq = []
def_protein = 0

# Swipe right on every base in the input string
for protein in org_dna_seq:
    if protein == "A" or protein == "a":
        comp_dna_seq.append("T")
    elif protein == "T" or protein == "t":
        comp_dna_seq.append("A")
    elif protein == "G" or protein == "g":
        comp_dna_seq.append("C")
    elif protein == "C" or protein == "c":
        comp_dna_seq.append("G")
    else:
        comp_dna_seq.append("*")
        def_protein += 1

# Reveal the results of the matchmaking process
print("The complement of input DNA sequence is :\n" + str(comp_dna_seq))

# Evaluate the relationship status
if def_protein == 0:
    print("It's a perfectly healthy DNA! No drama here. 💖")
else:
    print("The DNA is defective at", str(def_protein), "points.")
    print("Immediate DNA cleavage is recommended 🔪🧬")