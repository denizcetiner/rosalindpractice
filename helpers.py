import re
import itertools

def extract(dna_strings=""):
    dna_dict = {}
    current_dna_name = ""
    for line in dna_strings.splitlines():
        if line.startswith(">"):
            current_dna_name = line.replace(">", "")
            dna_dict[current_dna_name] = ""
        else:
            dna_dict[current_dna_name] += line.strip()
    return dna_dict


def find_motif(strand="GATATATGCATATACTT", motif="ATAT"):
    positions = {}
    strand_index = 0
    while re.search(motif, strand[strand_index:]) is not None:
        m = re.search(motif, strand[strand_index:])
        start = strand_index + m.start()
        content = m.group()
        if start not in positions:
            positions[start] = content
        strand_index = start + 1
    return positions


def sort_dict(input_dict={}):
    result = {}
    for key in sorted(input_dict.keys()):
        result[key] = input_dict[key]
    return result


def get_codon_protein_dict():
    dict_codon_protein = {}
    with open("rna_codon_table", "r") as codon_file:
        codons_names = codon_file.read().split()
    for i in range(0, len(codons_names), 2):
        codon = codons_names[i]
        name = codons_names[i + 1]
        dict_codon_protein[codon] = name
    # print(codon_dict)
    return dict_codon_protein


def get_protein_codon_dict():
    dict_protein_codon = {}
    with open("rna_codon_table", "r") as codon_file:
        codons_names = codon_file.read().split()
    for i in range(0, len(codons_names), 2):
        codon = codons_names[i]
        protein = codons_names[i + 1]
        if protein in dict_protein_codon:
            dict_protein_codon[protein].append(codon)
        else:
            dict_protein_codon[protein] = [codon]
    # print(codon_dict)
    return dict_protein_codon


def get_complement(dna_strand) -> str:
    complements = get_complement_dict()

    complement_strand = []
    for nt in dna_strand:
        complement_strand.append(complements[nt])
    return "".join(complement_strand)


def get_complement_dict():
    complements = {"A": "T", "G": "C"}
    revd = dict()
    for i in complements.items():
        revd[i[1]] = i[0]
    complements.update(revd)
    return complements


def find_start_codon(reading_frame="", start=0) -> int:
    start_codon = get_protein_codon_dict()["M"]

    for pos in range(start, len(reading_frame) - 3):
        try_codon = reading_frame[pos:pos + 3].replace("T", "U")
        if try_codon in start_codon:
            return pos
    return -1


def transcribe_until_stop(reading_frame="", start=0):
    proteins = []
    protein_codon_dict = get_protein_codon_dict()
    codon_protein_dict = get_codon_protein_dict()
    stop_codons = protein_codon_dict["Stop"]
    for pos in range(start, len(reading_frame), 3):
        codon = reading_frame[pos:pos + 3].replace("T", "U")
        if codon in stop_codons:
            break
        else:
            proteins.append(codon_protein_dict[codon])
    return proteins


def transcribe_rna_aminoacids(rna_string=""):
    codon_name_dict = get_codon_protein_dict()
    aminoacids = []
    for i in range(0, len(rna_string), 3):
        codon = str(rna_string[i:i + 3])
        if codon not in codon_name_dict:
            return None
        else:
            aminoacid = codon_name_dict[codon]
            aminoacids.append(aminoacid)
    if len(aminoacids) == 0 or aminoacids[len(aminoacids)-1] != "Stop":
        return None
    else:
        return aminoacids


def close_at_stop(strand=""):
    codons = []

    stop_codons = get_protein_codon_dict()["Stop"]
    for pos in range(0,len(strand),3):
        codon = strand[pos:pos + 3].replace("T", "U")
        codons.append(codon)
        if codon in stop_codons:
            break

    return "".join(codons)


def get_start_stop_regions(rna_string=""):
    start_stop_regions = []
    pos = 0
    while pos >= 0:
        pos = find_start_codon(rna_string, pos)
        if pos >= 0:
            remaining = close_at_stop(rna_string[pos:])
            start_stop_regions.append(remaining)
            pos += 1
    return start_stop_regions


def get_reading_frames(dna_strand=""):
    possible_reading_frames = []
    for i in range(3):
        possible_reading_frames.append(dna_strand[i:])
    return possible_reading_frames


def get_all_substrings(strand=""):
    length = len(strand)
    substrings = []

    for start in range(length):
        for end in range(start+1,length+1):
            substring = strand[start:end]
            substrings.append(substring)


def get_dict_pos_substring(strand=""):
    length = len(strand)
    dict_pos_substring = {}

    for start in range(length):
        for end in range(start + 1, length + 1):
            substring = strand[start:end]
            if start not in dict_pos_substring:
                dict_pos_substring[start] = [substring]
            else:
                dict_pos_substring[start].append(substring)

    return dict_pos_substring


def get_subsequences_of_length(strand="ABCDEF", length=4):
    perm_source = []
    for i in range(len(strand)):
        perm_source.append(i)

    perms = itertools.permutations(perm_source, length)

    list_perms = []

    for perm in perms:
        list_perm = sorted(list(perm))
        if list_perm not in list_perms:
            list_perms.append(list_perm)

    list_subsequences = []
    for list_perm in list_perms:
        subsequence_characters = []
        for position in list_perm:
            subsequence_characters.append(strand[position])
        list_subsequences.append("".join(subsequence_characters))

    return list_subsequences


def get_subsequences_all_lengths(strand="ABCDEF"):
    all_subseqs = []
    for i in range(1, len(strand)+1):
        all_subseqs.extend(get_subsequences_of_length(strand, i))

    return all_subseqs
