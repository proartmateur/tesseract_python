import os
from typing import List
from src.domain.digi_doc import DigiDoc
from src.infrastructure.mappers.pdf_to_digidoc_mapper import pdf_to_digidoc_mapper


def multiple_files(pdf_dir: str, number_of_pages = 1) -> List[DigiDoc]:
    result = []
    for root, dirs, files in os.walk(pdf_dir, topdown=False):
        for name in files:
            pdf_file = os.path.join(root, name)
            print(f'Procesando: {pdf_file}')
            result.append(pdf_to_digidoc_mapper(pdf_file, number_of_pages))
    return result