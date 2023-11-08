import os
from pprint import pprint

from infrastructure.pdf_to_digidoc_mapper import pdf_to_digidoc_mapper


def extract_all_files():
    pass

if __name__ == '__main__':
    # Ejemplo de uso
    pdf_file = 'smart_bin/American McGee - Art of Alice_ Madness Returns-Dark Horse Books (2011).pdf'
    pdf_file = 'smart_bin/reporteSemanasCotizadas_461.pdf'

    digi_doc = pdf_to_digidoc_mapper(pdf_file)
    pprint(digi_doc)


