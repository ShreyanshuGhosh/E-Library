import time


class Library:
    def __init__(self, lib_name, book, cus_list):

        self.lib_name = lib_name
        self.book = book
        self.cus_list = cus_list

    def display(self):
        print(self.book)
        print(" ")
        print(f'Books which are not available are: {self.cus_list}')
        time.sleep(4)

    def lend(self, book_name):
        if book_name in self.book:
            print('Thank you', a, f'for taking {book_name}. Please return it within a week.')
            self.book.remove(book_name)
            self.cus_list.append(book_name)
            time.sleep(4)

        elif book_name in self.cus_list:
            print('Sorry, that book is already taken ')
            time.sleep(4)
        else:
            print("sorry we don't have that book")
            time.sleep(4)

    def add(self, book_name):
        if book_name not in self.book:
            print("Thank you", d, " for giving us a new book. This means a lot to us.")
            self.book.append(book_name)
            time.sleep(4)
        else:
            print("Thank you but this book is already with us.")
            time.sleep(4)

    def give_back(self, book_name):
        if book_name in self.cus_list:
            print(f"Thank you {f} for returning the book")
            self.book.append(book_name)
            self.cus_list.remove(book_name)
            time.sleep(4)
        elif book_name in self.book:
            print('This  book is not taken. How can you return it?')
            time.sleep(4)
        else:
            print('Invalid input. Either the book name or customer name is incorrect ')
            time.sleep(4)


lib = Library("SG Library", ['Ring of fire', 'Harry potter series', 'Artemis fowl series', 'NCERT 10',
                             'IIT foundation series std. 10', 'Lord of the rings', 'Percy Jackson series'], [])

if __name__ == "__main__":
    print(f'Welcome to {lib.lib_name}', )
    print("It is requested to all the ones who are present in library to maintain the library etiquette")

    while True:
        ask = input('> To get info. of books available, press "d"\n'
                    '> To lend a book, press "l"\n'
                    '> To give a new book, press "a"\n'
                    '> To return a book, press "g"\n'
                    '> To exit from library, press "e"\n'
                    '==>')

        if ask == "d":
            lib.display()

        elif ask == "l":
            a = input('Enter your name:')
            b = input("enter the book you want to take:")
            lib.lend(b)

        elif ask == "a":
            c = input('Enter the book you wanna give: ')
            d = input('Enter your name: ')
            lib.add(c)

        elif ask == "g":
            e = input('Enter the book you are returning:')
            f = input('Enter your name with which you have issued the book: ')
            lib.give_back(e)

        elif ask == "e":
            print('Thank you for visiting')
            break
        else:
            print('Invalid input ')
            time.sleep(2)
