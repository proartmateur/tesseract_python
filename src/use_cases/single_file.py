from src.domain.digi_doc import DigiDoc
from src.infrastructure.mappers.pdf_to_digidoc_mapper import pdf_to_digidoc_mapper


def single_file(pdf_path: str, number_of_pages = 1) -> DigiDoc:
    return pdf_to_digidoc_mapper(pdf_path, number_of_pages)