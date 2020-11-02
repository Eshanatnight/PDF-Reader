import tkinter.filedialog as fstream
from threading import Thread
import pyttsx3
import PyPDF2

status = False


# Opens File Dialog Window
def openfilewindow():
    book = fstream.askopenfilename()
    return book


class GUI(Thread):

    def __init__(self):
        super().__init__()
        self.book = ''
        self.reader = ''
        self.numberOfPages = 0
        self.speaker = pyttsx3.init()
        self.speaker.setProperty('rate', 175)

    # Basic run for Thread
    def run(self):
        global status
        self.book = openfilewindow()
        self.reader = PyPDF2.PdfFileReader(self.book)
        self.numberOfPages = self.reader.getNumPages()
        status = True

        for _page in range(0, self.numberOfPages):
            page = self.reader.getPage(_page)
            pageText = page.extractText()
            self.speaker.say(pageText)
        self.speaker.runAndWait()

    # Stops Reading
    def end(self):
        global status
        if status:
            self.speaker.stop()
        elif not status:
            return
