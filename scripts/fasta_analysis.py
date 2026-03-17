def read_fasta(filename):
    seq = ""
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq

sequence = read_fasta("data/sequence.fasta")
print(sequence)

def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    gc = (g + c) / len(seq) * 100
    return gc

print("GC content:", gc_content(sequence))
