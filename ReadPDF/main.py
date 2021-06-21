# import pyttsx3

# engine = pyttsx3.init()

# rate = engine.getProperty('rate')

# print (rate)

# engine.setProperty('rate', 125)

# volume = engine.getProperty('volume')

# print (volume)

# engine.setProperty('volume',1.0)

# voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[1].id)

# engine.say('Hello Mohmad Gamal Ali')

# engine.runAndWait()


from gtts import gTTS

import PyPDF2

from playsound import playsound

book = open("bash.pdf" ,  'rb')

pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages

x = 1

allText = []

while x <= pages - 1:

	allText.append(" ")

	allText.append(pdfReader.getPage(x).extractText())

	allText.append(" ")

	print("Num Of Pages ==> " + " " + str(x))

	# print(allText)

	x = x + 1

# print(pages)

print(allText)

print(len(allText))

s = ""

for item in allText:
	s += item

# page = pdfReader.getPage(10)

# text = page.extractText()

# text = pdfReader.extractText()

tts1 = gTTS(s)

# tts2 = gTTS('مرحبا محمد جمال علي محمد عامل اي يسطا ليك وحشه' , lang="ar")

tts1.save("hello.mp3")

# playsound("hello.mp3")
