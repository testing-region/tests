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


#test
if __name__ == '__main__':
    pdf_file_path = 'FERMI ESTIMATION MINI PROJECT.pdf'
    doc_file_path = 'test.docx'
    convert_pdf_to_doc(pdf_file_path, doc_file_path)
    result = docx2txt.process(doc_file_path)
    print(result)
    tts = gTTS(text=result, lang='en-GB')
    tts.save("test.mp3")
    print("done")