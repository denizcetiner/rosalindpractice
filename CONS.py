def create_matrix(name_dna_dict = {}):
    length = len(list(name_dna_dict.values())[0])
    matrix = []
    for name, dna in name_dna_dict.items():
        current_dna = []
        for i in range(length):
            current_dna.append(dna[i])
        matrix.append(current_dna)
    return  matrix

def create_profile_dict(dna_matrix = [[]]):
    columns = len(dna_matrix[0])
    rows = len(dna_matrix)
    profile_dict = {"A": [0] * columns, "C": [0] * columns, "G": [0] * columns, "T": [0] * columns}
    for col in range(columns):
        for row in range(rows):
            current_nucleotide = dna_matrix[row][col]
            profile_dict[current_nucleotide][col] += 1
    print(profile_dict)
    return profile_dict


def create_consensus_string(profile_dict = {}):
    consensus = []
    columns = len(list(profile_dict.values())[0])
    for col in range(columns):
        max_nucleotide = ""
        max_frequency = -1
        for nucleotide, frequencies in profile_dict.items():
            col_frequency = frequencies[col]
            if col_frequency > max_frequency:
                max_nucleotide = nucleotide
                max_frequency = col_frequency
        consensus.append(max_nucleotide)
    print(consensus)
    return consensus


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

def run(input = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""):
    lines = extract(input)
    matrix = create_matrix(lines)
    print(matrix)
    profile_dict = create_profile_dict(matrix)
    consensus_string = create_consensus_string(profile_dict)
    print(consensus_string)

    result = "".join(consensus_string) + "\n"
    print(result)
    for name, frequencies in profile_dict.items():
        line = "{0}: {1}\n".format(name, " ".join(str(freq) for freq in frequencies))
        print(line)
        result += line
    print(result)
    return result

run()
