# ex-3-lena-fiedor

import requests
import re
import json
from collections import namedtuple


def get_prot_info(protein: dict) -> namedtuple:

    """
    This function picks:
    - protein ID
    - date of creation
    - full name of the protein
    - full gene name
    - gene synonyms
    from a database entry containing one protein (dict) and packs it into a namedtuple (class __main__.ProtInfo).
    """

    synonyms = protein['gene'][0].get('synonyms', [])
    synonym = synonyms[0]['value'] if synonyms else 'No synonyms'
    return ProtInfo(protein['accession'],
                    protein['info']['created'],
                    protein['protein']['recommendedName']['fullName']['value'],
                    protein['gene'][0]['name']['value'],
                    synonym)


def print_prot_info(protein: namedtuple):
    
    """This function prints out all the properties of a class __main__.ProtInfo."""

    print(f'Protein ID : {protein.id}')
    print(f'Created on : {protein.date_created}')
    print(f'Full protein name : {protein.full_name}')
    print(f'Gene name : {protein.gene_name}')
    print(f'Gene name synonyms : {protein.gene_synonyms}')


STATUS_CODE_SUCCESS = 200

# create a query of type requests.models.Response
url = 'https://rest.uniprot.org/uniprotkb/stream?format=json&query=%28%28protein_name%3A%22transcription+factor+SOX%22%29%29+AND+%28model_organism%3A10090%29+AND+%28reviewed%3Atrue%29'
query = requests.get(url)

# if operation has succeeded, create a dictionary with only one key - results, and extract it into a list
if query.status_code == STATUS_CODE_SUCCESS:
    data = query.json()
    protein_list = data['results']
    # each protein is itself a nested dictionary

# extract protein IDs from obtained list
protIDs = [protein['primaryAccession'] for protein in protein_list]

# create an url for ncbi with a string containing protein IDs separated by coma
url_ncbi = 'https://www.ebi.ac.uk/proteins/api/proteins?&accession=' + ','.join(protIDs)

# make a query to ncbi
query_ncbi = requests.get(url_ncbi, headers={"Accept" : "application/json"})

# create a new class which inherits from a tuple in order to easily pick necessary properties
ProtInfo = namedtuple('ProtInfo', 'id date_created full_name gene_name gene_synonyms')

# if operation has succeeded, iterate through a list of entries to get and print their properties
if query_ncbi.status_code == STATUS_CODE_SUCCESS:
    protein_list = query_ncbi.json()
    for protein in protein_list:
        prot_info = get_prot_info(protein)
        print_prot_info(prot_info)
        print()
