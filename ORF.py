from helpers import extract, find_motif, get_reading_frames, get_complement, transcribe_rna_aminoacids, get_start_stop_regions


def run(user_input=""">Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""):
    dict_name_strand = extract(user_input)
    strand = list(dict_name_strand.values())[0]
    reverse_complement = get_complement(strand)[::-1]

    orfs = []
    orfs.extend(get_reading_frames(strand))
    orfs.extend(get_reading_frames(reverse_complement))

    start_stop_regions = []

    for orf in orfs:
        # print("ORF:" + orf)
        orf_start_stop_regions = get_start_stop_regions(orf)
        for start_stop_region in orf_start_stop_regions:
            if start_stop_region not in start_stop_regions:
                start_stop_regions.append(start_stop_region)
                # print("STR:" + start_stop_region)


    for start_stop_region in start_stop_regions:
        print(transcribe_rna_aminoacids(start_stop_region))

    transcribed_strings = []

    for start_stop_region in start_stop_regions:
        transcribed = transcribe_rna_aminoacids(start_stop_region)
        if transcribed is not None:
            transcribed_string = "".join([y for y in transcribed if y != "Stop"])
            if transcribed_string not in transcribed_strings:
                transcribed_strings.append(transcribed_string)

    result = ""
    for transcribed_string in transcribed_strings:
        print(transcribed_string)
        result += "{0}\n".format(transcribed_string)
    return result
