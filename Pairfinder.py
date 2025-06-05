# 💘 Pair Finder: Like Tinder, but for lonely nucleotides.

org_dna_seq = input("Please input the DNA sequence: ").upper()
print (org_dna_seq)

# Our matchmaker's toolkit
comp_dna_seq = []
def_protein = 0
ndef_protein = 0

# Swipe right on every base in the input string
for protein in org_dna_seq:
    if protein == "A":
        comp_dna_seq.append("T")
        ndef_protein += 1
    elif protein == "T":
        comp_dna_seq.append("A")
        ndef_protein += 1
    elif protein == "G":
        comp_dna_seq.append("C")
        ndef_protein += 1
    elif protein == "C":
        comp_dna_seq.append("G")
        ndef_protein += 1
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


if ndef_protein == 0:
    print("This sequence is straight-up nonsense. No valid bases found. 🤡")
elif (def_protein / ndef_protein) >= 1:
    print("Immediate DNA cleavage is recommended 🔪🧬")
else:
    print("DNA is in safe stage.\nRectification is recommended.")