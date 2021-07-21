from gtts import gTTS
import PyPDF2 as pdf
import os

book = open('UnmeritedFavor.pdf', 'rb')
pdf_reader = pdf.PdfFileReader(book)
page = pdf_reader.getPage(8)
data = page.extractText()

tts = gTTS(data)
os.save('page1.mp3')