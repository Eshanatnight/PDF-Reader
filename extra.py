
def startFrom(reader, speaker, pageNumber):

    numberOfPages = reader.getNumPages()

    for _page in range(pageNumber, numberOfPages):
        page = reader.getPage(_page)
        pageText = page.extractText()
        speaker.say(pageText)

    speaker.runAndWait()

    return



def startFull(reader, speaker):

    numberOfPages = reader.getNumPages()

    for _page in range(0, numberOfPages):
        page = reader.getPage(_page)
        pageText = page.extractText()
        speaker.say(pageText)

    speaker.runAndWait()

    return