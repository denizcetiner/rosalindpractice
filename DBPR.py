from Bio import ExPASy
from Bio import SwissProt

def run(user_input="""Q5SLP9"""):
    uniprot_id = user_input.strip()
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)

    gene_onotology = list(filter(lambda x: x[0] == "GO", record.cross_references))
    bio_processes = list(filter(lambda x: str(x[2]).startswith("P:"), gene_onotology))
    process_names = [str(process[2])[2:] for process in bio_processes]
    print(process_names)

    result = "\n".join(process_names)
    print(result)
    return result
