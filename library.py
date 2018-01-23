#CONTEXT
#Implements software for the local library. The user of the software will be the
#librarian, who uses your program to issue library cards, check books out to patrons, check
#books back in, send out overdue notices, and open and close the library.

#Objects, Classes, Methods

#Srihari Menon
######################################################################################################################################


class Calendar:
    """To deal with the passage of time, so this is to keep track of dates. This means the initial date is "0". This class needs only a couple methods"""

    def __init__(self):
        """Sets the date to 0. time is the same for everyone"""
        self.date=0

    def get_date(self):
        """Returns (as an integer) the current date."""
        return(self.date)

    def advance(self):
        """Increment the date (move ahead to the next day), and returns the new date."""
        self.date=self.date+1


class Book:
    
    """A book has these attributes (instance variables): id, title, author (only one author per book), and due_date. The due date is None if the book is
    not checked out."""

    def __init__(self, i_d, title, author):
        """The constructor. Saves the provide information. When created, the book is not checked out."""
        self.id=i_d
        self.title=title
        self.author=author
        self.due_date=None
        
    def get_id(self):
        
        """Returns theis book's unique identification number."""

        return(self.id)

    def get_title(self):
        """Returns this book's title."""

        return(self.title)

    def get_author(self):
        """Returns this books author."""

        return(self.author)

    def get_due_date(self):    
        """Returns the date (as an integer) that this book is due."""
    
        return(self.due_date)
        

    def check_out(self, due_date):
        """Sets the due date of this Book. Does not return anything."""

        self.due_date=due_date

    def check_in(self):
        """Sets the due date of this Book to None. Does not return anything."""

        self.due_date=None


    def __str__(self):
        """Returns a string of the form "id: title, by author". """

        tempid=self.id
        temp=str(tempid)+": "+self.title+", by "+self.author
        return(temp)


class Patron:
    """A patron is a "customer" of the library. A patron must have a library card in order to check out books. A patron with a card may have no more
    than three books checked out at any time."""

    def __init__(self, name, library):
        """Constructs a patron with the given name, and no books. The patron must also have a reference to the Library object that he/she uses. So that
        this patron can later be found by name."""
        self.name=name
        self.library=library
        self.books=[]
        
    
    def get_name(self):
        """Returns this patron's name."""
        return(self.name)

    def check_out(self, book):
        """Adds this Book object to the set of books checked out by this patron."""
        self.books.append(book)
        
        
    def give_back(self, book):
        """Removes this Book object from the set of books checked out by this patron."""
        for i in range(0,len(self.books)-1):

            if self.books[i].id==book.id:
                del self.books[i]
        
    def get_books(self):
        """Returns the set of Book objects checked out to this patron (may be the empty set, set([]) )."""
        return(self.books)

    def get_overdue_books(self):
        """Returns the set of OVERDUE Book objects checked out to this patron (may be the empty set, set([]) )."""

        overdue_books=[]

        for book in self.books:
            if book.get_due_date()<self.library.time.get_date():
                overdue_books.append(book)

        return(set(overdue_books))


class Library():
    """This is the "master" class. It has a number of methods which are called by the "librarian" (the user), not by patrons. The librarian does
    all the work. Since these methods (other than the contstructor) will be typed in by the librarian, all the paramters must be strings or numbers, not
    objects (how would you type in a Book object?). Furthermore, to reassure the librarian that his/her action has worked, all these methods should return
    a result, for example, "Library card issued to Amy Gutmann." """

    def __init__(self):
        """Constructs the Library object"""

        print("founding library...")
        
        import ast
        
        file_id=open("collection.txt",'r') 
        temp=file_id.read()
        
        collection=ast.literal_eval(temp)

        lib_books=[]
        book_ref=0

        for tup in collection:
            book_ref=book_ref+1
            lib_books.append(Book(book_ref,tup[0],tup[1]))

        self.books=lib_books

        self.time=Calendar()

        self.patrons={}

        self.openclose=0 #close is 0 open is 1

        self.current_pat=None

        print("\t\tWELCOME. THE LIBRARY HAS NOW BEEN SET UP. LET THE LEARNING BEGIN")

        
        

    def open(self):
        """If the library is already open, raises an Exception with the message "The library is already open!" Otherwise, starts the day by advancing the
        Calendar, and setting the flag to indicate that the library is open. ().   Returns: The string "Today is day n. "  """

        if self.openclose==1:
            print("The library is already open!")
        else:
                self.openclose=1
                self.time.advance()

        return("today is day "+str(self.time.get_date()))       
        

    def find_all_overdue_books(self):
        """Returns a nicely formatted, multiline string, listing the names of patrons who have overdue books, and for each such patron, the books that are
        overdue. Or, it returns the string "No books are overdue." """

        temp2=""
        
        for pat in self.patrons:
            overdue_books=self.patrons[pat].get_overdue_books()
            overdue_books=list(overdue_books)
            temp=""

            if overdue_books!=[]:
                for book in overdue_books:
                    temp=temp+book.get_title()+", "
                
                temp2=temp2+pat+":"+temp+'\n'

        if temp2=="":
            temp2="No books are overdue."

        return(temp2)
                
                

        

    def issue_card(self, name_of_patron):
        """Issues a library card to the person with this name. However, no patron should be permitted to have more than one library card. Returns
        either "Library card issued to name_of_patron." or "name_of_patron already has a library card." Possible Exception: "The library is not open." """
        
        if self.openclose==0:
            return("The library is not open.")

        counter=0
        
        for pat in self.patrons:
            if pat==name_of_patron:
                counter=counter+1

        if counter==0:
            self.patrons[name_of_patron]=Patron(name_of_patron,self)
            return("Library card issued to "+name_of_patron+".")
        else:
                return(name_of_patron+" already has a library card.")
        

        
    def serve(self, name_of_patron):
        """Specifies which patron is about to be served (and quits serving the previous patron, if any).
        The purpose of this method is so that you don't have to type in the person's name again and again for every book that is to be checked in or checked out.
        What the method should actually do is to look up the patron's name in the dictionary, and save the returned Patron object in an instance variable of this library.
        Returns either "Now serving name_of_patron."or " name_of_patron does not have a library card." ."""

        
        for pat in self.patrons:
            if pat==name_of_patron:
                self.current_pat=self.patrons[pat]
                return("Now serving "+name_of_patron+".")
        return(name_of_patron+" does not have a library card.")
                
        
        

    def find_overdue_books(self):
        """Returns a multiline string, each line containing one book (as returned by the book's __str__ method), of the books that have been cheecked out
        by the patron currently being served, and which are overdue. If the patron has no overdue books, the value None is returned. May raise an Exception
        with an appropriate message: "The Library is not open." or "No patron is currently being served." """

        if self.openclose==0:
            return("The Library is not open.")

        try:
            overdue_books=list(self.current_pat.get_overdue_books())
        except:
            return("No patron is currently being served.")

        temp=""

        if overdue_books==[]:
            return(None)

        for book in overdue_books:
            temp=temp+book.__str__()+"\n"

        return(temp)

        

    def check_in(self, *book_ids):
        """The books are bing returned by the patron currently being served, so return them to the collection and remove them from the set of books currently
        checked out to the patron. The books_ids are taken from the list teturned by the get_books method in the Patron object. Checking in a Book will
        involve bOTH telling the Book that its is checked in AND If successful, returns "name_of_patron has returned n books."  May raise an Exception with
        an appropriate message: "The library is not open" or "No patron is currenly being served" or "The patron does not have book id"."""

        if self.openclose==0:
            return("The Library is not open.")

        try:
            pat_books=self.current_pat.get_books()
        except:
            return("No patron is being currently served.")

        tot_books=0

        for bid in book_ids:

            foundbook=0
            
            for book in pat_books:

                if bid==book.get_id():
                    book.check_in()
                    self.current_pat.give_back(book)
                    foundbook=1
                    break

            if not(foundbook):
                print("The patron does not have book "+str(bid))
            else:
                tot_books=tot_books+1

        return(self.current_pat.get_name()+" has returned "+str(tot_books)+" books.")



    def search(self, string):
        """Finds those Book s whose title or author (or both) contains this string. For example, the
        string "tact" might return, among other things, the book Contact, by Carl Sagan. The
        search should be case-insensitive; that is, "saga" would also return this book. Only
        books which are currently available (not checked out) will be found. If there is more than
        one copy of a book (with the same title and same author), only one will be found. In
        addition, to keep from returning too many books, require that the search string be at least
        4 characters long.
        Returns one of:"No books found.","Search string must contain at least four characters.",
        A multiline string, each line containing one book (as returned by the book's __str__ method.)"""

        import re

        if len(string)<4:
            return("Search string must contain at least four characters.")
        

        temp=""

        for book in self.books:
            if re.search(string,book.get_title(),re.IGNORECASE) or re.search(string,book.get_author(),re.IGNORECASE):
                if not(book.get_title()+", by "+book.get_author() in temp):
                    temp=temp+book.__str__()+"\n"

        if temp=="":
            temp="No books found."

        return(temp)
               

    def check_out(self, *book_ids):
        """ Checks out the books"""

        if self.openclose==0:
            return("The Library is not open.")

        try:
            len(self.current_pat.get_books())
        except:
            return("No patron is being currently served.")
        
        tot_books=0

        for bid in book_ids:

            foundbook=0
            
            for book in self.books:
                if bid==book.get_id() and book.get_due_date()==None:

                    if (len(self.current_pat.get_books())>=3):
                        return("Patron cannot have more than three books. First "+str(tot_books)+" books have been checked out to "+self.current_pat.get_name())
                    else:
                        book.check_out(self.time.get_date()+6)
                        self.current_pat.check_out(book)
                        foundbook=1
                        break
            if not(foundbook):
                print("the library does not have book "+str(bid))
            else:
                tot_books=tot_books+1

        return(str(tot_books)+" books have been checked out to "+self.current_pat.get_name())
                
        

    def renew(self, *book_ids):
        """renews books given to patrons"""

        if self.openclose==0:
            return("The Library is not open.")

        try:
            pat_books=self.current_pat.get_books()
        except:
            return("No patron is being currently served.")

        tot_books=0

        for bid in book_ids:

            foundbook=0
            
            for book in pat_books:

                if bid==book.get_id():
                    book.check_out(self.time.get_date()+6)
                    foundbook=1
                    break

            if not(foundbook):
                print("The patron does not have book "+str(bid))
            else:
                tot_books=tot_books+1

        return(str(tot_books)+" books have been renewed for "+self.current_pat.get_name())

        

    def close(self):
        if self.openclose==0:
            return("The Library is not open.")

        self.current_pat=None
        
        self.openclose=0
        return("good night")

    def quit(self):
        """The mayor, citing a budget crisis, has stopped all funding for the library. Can happen at any time. Returns the string "The library is now closed
        for renovations." """

        self.openclose=0
        return("The library is now closed for renovations.")

def main():
    librarian=Library()


    day=10

    print(librarian.open())

    while day==10:
        

        try:
            op=int(input(" 0->start day,\t\t 1 ->new patron,\t 2 ->serve patron,\n 3->search books,\t 4->check out books,\t 5->check in books,\n 6->find overdue books,\t 7->renew books,\t 8->find all overdue books,\n 9->end day,\t\t 10->close library\t Enter choice:"))
        except:
            print("enter a number between 0 and 10 only!")
            continue

        if op==0:
            print(librarian.open())

        if op==1:
            patname=str(input("name?"))
            print(librarian.issue_card(patname))
        if op==2:
            patname=str(input("name?"))
            print(librarian.serve(patname))
        if op==3:
            searchterm=str(input("searchterm?"))
            print(librarian.search(searchterm))
        if op==4:
            bid=[int(x) for x in input("book ids?").split( )]
            print(librarian.check_out(*bid))
        if op==5:
            bid=[int(x) for x in input("book ids?").split( )]
            print(librarian.check_in(*bid))
        if op==6:
            print(librarian.find_overdue_books())
        if op==7:
            bid=[int(x) for x in input("book ids?").split( )]
            print(librarian.renew(*bid))
        if op==8:
            print(librarian.find_all_overdue_books())
        if op==9:
            print(librarian.close())
        if op==10:
            print(librarian.quit())
            dummy=input("press any key to close")
            day=0
            
main()        

