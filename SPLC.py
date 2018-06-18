from helpers import extract, transcribe_rna_aminoacids


def run(user_input=""">Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""):
    dict_name_strand = extract(user_input)
    list_strands = list(dict_name_strand.values())
    main_strand = list_strands[0]
    introns = list_strands[1:]

    for intron in introns:
        main_strand = main_strand.replace(intron, "")
    main_strand_rna = main_strand.replace("T", "U")

    main_strand_transcribed = transcribe_rna_aminoacids(main_strand_rna)

    transcribed_string = "".join(n for n in main_strand_transcribed if n != "Stop")

    print(transcribed_string)
    return transcribed_string