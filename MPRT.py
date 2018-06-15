import urllib.request
from helpers import extract, find_motif


def get_http_request(url):
    contents = urllib.request.urlopen(url).read()
    return bytes(contents).decode("utf-8")


def run(inputs="""A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST"""):
    protein_names = [item.strip() for item in inputs.splitlines()]
    print(protein_names)

    motif = "N[^P][ST][^P]"

    dna_name_strings = {}
    url_format = "http://www.uniprot.org/uniprot/{0}.fasta"
    for protein in protein_names:
        url = url_format.format(protein)
        url_response = get_http_request(url)
        extracted_dict = extract(url_response)
        dna_name_string = {protein: list(extracted_dict.values())[0]}
        dna_name_strings.update(dna_name_string)

    for name, strand in dna_name_strings.items():
        print("name  :{0}".format(name))
        print("strand:{0}".format(strand))

    dna_name_motif_positions = {}
    for name, strand in dna_name_strings.items():
        motif_positions = find_motif(strand, motif)
        dna_name_motif_positions[name] = list(motif_positions.keys())

    for name, positions in dna_name_motif_positions.items():
        print("name: {0}".format(name))
        print("pos : {0}".format(positions))

    result = ""
    for name, positions in dna_name_motif_positions.items():
        if len(positions) > 0:
            result += "{0}\n{1}\n".format(name, " ".join(str(pos+1) for pos in positions))

    print(result)
    return result
