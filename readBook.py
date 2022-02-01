class ReadBook(object):
    def __init__(self, bookName=None, freeTime=None, bookmark=None, rating=None):
        self.bookName = bookName
        self.freeTime = freeTime
        self.bookmark = bookmark
        self.rating = rating
    def StartBook(self, bookName, freeTime):
        if freeTime == "Yes":
            print("You have started reading " + bookName)
    def PauseReading(self, bookmark):
        self.bookmark = bookmark
        print("You have paused at page " + bookmark)
    def ContinueReading(self, bookmark):
        if bookmark != None:
            print("You have resumed from page " + bookmark)
            self.bookmark = None
    def FinishedReading(self, rating):
        print("You have finished " + self.bookName + " and you gave it " + rating)

book = ReadBook("These Violent Delights", "Yes")
print(book.StartBook(book.bookName, book.freeTime))
print(book.PauseReading("50"))
print(book.ContinueReading(book.bookmark))
print(book.FinishedReading("4.5 stars"))