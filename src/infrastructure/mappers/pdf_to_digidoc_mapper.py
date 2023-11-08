import os
from pdf2image import convert_from_path
import pytesseract
import PyPDF2
from src.domain.digi_doc import DigiDoc

def extract_text_from_pdf(pdf_file, number_of_pages = 1):
    # Convierte el PDF en imágenes
    images = convert_from_path(pdf_file)
    # Inicializa el texto extraído
    extracted_text = ""
    pages = 0
    for image in images:
        print(f'Obteniendo de la página: {pages}')
        # Utiliza Tesseract para extraer texto de la imagen
        text = pytesseract.image_to_string(image, lang='eng')
        extracted_text += text
        pages += 1
        if pages == number_of_pages:
            break
    return [extracted_text, pages]

def get_pdf_metadata(pdf_file):
    metadata = {}
    with open(pdf_file, 'rb') as pdf_file_obj:
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        metadata['Número de páginas'] = len(pdf_reader.pages)
        info = pdf_reader.metadata
        metadata['Título'] = info.title
        metadata['Autor'] = info.author
        metadata['Asunto'] = info.subject
        metadata['Creador'] = info.creator
        metadata['Productor'] = info.producer
        metadata['Fecha de creación'] = info.creation_date
        metadata['Fecha de modificación'] = info.modification_date
    return metadata

def pdf_to_digidoc_mapper(pdf_path: str, number_of_pages = 1) -> DigiDoc:
    extracted_text, pages = extract_text_from_pdf(pdf_path, number_of_pages)
    metadata = get_pdf_metadata(pdf_path)
    metadata['Páginas procesadas con OCR'] = pages
    return DigiDoc(pdf_path, os.path.basename(pdf_path), extracted_text, metadata)