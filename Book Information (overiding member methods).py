class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    def print_info(self):
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)


class Encyclopedia(Book):
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_volumes
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        Book.__init__(self, title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes

    # TODO: Define a print_info() method that overrides the print_info()
    #       in the Book class
    def print_info(self):
        print('Book Information:')
        print('   Book Title:', self.title)
        print('   Author:', self.author)
        print('   Publisher:', self.publisher)
        print('   Publication Date:', self.publication_date)
        print('   Edition:', self.edition)
        print('   Number of Volumes:', self.num_volumes)


if __name__ == "__main__":
    title = input("Type in a title:")
    author = input("Type in the author:")
    publisher = input("Type in the publisher:")
    publication_date = input("Type in the publication date:")

    e_title = input("Type in the title of the encyclopedia:")
    e_author = input("Type in the author:")
    e_publisher = input("Type in the publisher:")
    e_publication_date = input("Type in the publication date:")
    edition = input("Type in the edition:")
    num_volumes = int(input("Type in the number of volumes:"))

    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()

    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_volumes)
    my_encyclopedia.print_info()
