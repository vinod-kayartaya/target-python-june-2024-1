#! .venv/bin/python


class Book:
    def __init__(self, title=None, author=None, price=0.0) -> None:
        self.title = title
        self.author = author
        self.price = price

    def __str__(self) -> str:
        """
        This function's return value textually represents the invoking object
        """
        return f'Book(title="{self.title}", author="{self.author}", price={self.price})'

    def print(self):
        print('Book details: ')
        print(f'Title       : {self.title}')
        print(f'Author      : {self.author}')
        print(f'Price       : ₹{self.price}')
        print()
    
def main():
    b1 = Book('Let us C', 'Y Kanitkar', 395)
    print(b1.__str__())  # OO approach
    print(Book.__str__(b1))  # Procedural approach
    print(b1)  # print() method is trying to treat `b1` as a str, automatically calls the `b1.__str__()`
    # print(dir(b1))

    b2 = Book('Python unleashed', 'John doe', 989)
    print(b2)

    b1.print()
    b2.print()

    b2.price = -2922
    b2.print()
    
    print()


if __name__ == '__main__':
    main()

