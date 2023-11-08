from pprint import pprint

from src.use_cases.multiple_files import multiple_files
from src.use_cases.single_file import single_file


def extract_all_files():
    pass

if __name__ == '__main__':
    # Ejemplo de uso
    print("Ejecutando single_file")
    pdf_file = 'smart_bin/reporteSemanasCotizadas_461.pdf'
    digi_doc = single_file(pdf_file, 2)
    pprint(digi_doc)

    print("Ejecutando multiple_files")
    pdf_dir = 'smart_bin'
    docs = multiple_files(pdf_dir)
    for digi_doc_a in docs:
        pprint(digi_doc_a)



