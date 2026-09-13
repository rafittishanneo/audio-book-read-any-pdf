import pyttsx3
import PyPDF2

#Change voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#edit your book name with extention (.pdf)
book = open('YOUR BOOK NAME.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

print("Number of pages:", pages)

# Extract text from ALL pages
all_text = ""

for num in range(pages):
    page = pdfReader.pages[num]
    text = page.extract_text()

    if text:
        print(f"Extracting page {num + 1}/{pages}")
        all_text += text + "\n\n"

book.close()

print("All pages extracted.")
print("Starting audiobook...")

# Initialize text-to-speech
friend = pyttsx3.init()

# Read the complete PDF
friend.say(all_text)
friend.runAndWait()

print("Audiobook finished!")
