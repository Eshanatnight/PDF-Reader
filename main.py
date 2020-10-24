import pyttsx3
import PyPDF2
from extra import *

if __name__ == "__main__":
    print("[Starting]: Reader is starting")
    # initializing speaker object
    speaker = pyttsx3.init()
    nameOfBook = str(input("Enter The Name(without extension) with the Path to the file: "))
    book = open(nameOfBook + ".pdf", 'rb')
    reader = PyPDF2.PdfFileReader(book)
    speaker.setProperty('rate', 175)

    print("Press 1 to start Reading \n")
    print("Press 2 to start Reading from a specific page \n")

    choice = int(input())

    if choice == 1:
        startFull(reader, speaker)

    elif choice == 2:
        pageNumber = int(input("Enter Page Number to start from: "))
        startFrom(reader, speaker, pageNumber)

    print("[Finished]: Process Finished")