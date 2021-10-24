# convert pdf file to doc file
# using pdf2docx module


from pdf2docx import parse
from typing import Tuple
import docx2txt
from gtts import gTTS


def convert_pdf_to_doc(pdf_file_path: str, doc_file_path: str) -> Tuple[str, str]:
    """
    convert pdf file to doc file
    :param pdf_file_path: pdf file path
    :param doc_file_path: doc file path
    :return: doc file path
    """
    parse(pdf_file_path, doc_file_path)
    return doc_file_path


pdf_file_path = input("Enter pdf file path: ")
doc_file_path = pdf_file_path.replace(".pdf", ".doc")
convert_pdf_to_doc(pdf_file_path, doc_file_path)
tts = gTTS(text=docx2txt.process(doc_file_path), lang="en")
tts.save(pdf_file_path.replace(".pdf", ".mp3"))

print("Done")
