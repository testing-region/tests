# Convert pdf to text
# play text as speech using google text to speech

# import PyPDF2
# from gtts import gTTS

# pdfFileObj = open('FERMI ESTIMATION MINI PROJECT.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# mytext = ''

# for pageNum in range(pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     mytext += pageObj.extractText()

# print(mytext)
# pdfFileObj.close()


# tts = gTTS(text=mytext, lang='en')
# tts.save("FERMI ESTIMATION MINI PROJECT.mp3")

# Convert word to text using docx2text module
# and convert text to speech using gTTS

import docx2txt
from gtts import gTTS, tts

docfile = '/home/david/Downloads/FERMI ESTIMATION MINI PROJECT.docx'

result = docx2txt.process(docfile)

print(result)
# tts = gTTS(text=result, lang='en')
# tts.save("FERMI ESTIMATION MINI PROJECT1.mp3")

