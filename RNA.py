def run(dna_sequence = "GATGGAACTTGACTACGTAAATT"):
    dna_sequence_highlighted = dna_sequence.replace("T", " T ")
    rna_sequence_highlighted = dna_sequence.replace("T", " U ")
    rna_sequence = dna_sequence.replace("T", "U")

    print(dna_sequence_highlighted)
    print(rna_sequence_highlighted)

    return rna_sequence
