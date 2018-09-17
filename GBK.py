from Bio import Entrez
from Bio import SeqIO

def run(user_input="""Anthoxanthum
2003/7/25
2005/12/27"""):
    params = user_input.splitlines()
    genus_name = params[0]
    first_date = params[1]
    second_date = params[2]

    term = f"({genus_name}[Organism]) AND ({first_date}[Publication Date] : {second_date}[Publication Date])"

    Entrez.email = "deniz.cetiner94@gmail.com"
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    result = record["Count"]
    print(result)

    return result


def get_seq_by_genbank_id(user_input="""JX205496.1"""):
    Entrez.email = "deniz.cetiner94@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=user_input)


run()
