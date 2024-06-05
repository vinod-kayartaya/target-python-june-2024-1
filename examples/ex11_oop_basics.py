#! .venv/bin/python


class Book:
    def __init__(self) -> None:
        """
        This method is very important since we create member variables here. The variable received `self`
        has access to the memory reserved for this object (which is currently empty). We can create new
        data members (attributes) in that memory location.
        """
        # we are adding/creating new attributes to this particular object
        self.title = ''
        self.author = ''
        self.price = 0.0
        # print(f'Book.__init__() called with {self = }')


def main():
    b1 = Book()  # b1 = new Book()
    # When an object of Book is created, Python allocates some memory in the heap for the new object,
    # invokes the __init__ method (if exists), and supplies the reference to the newly constructed object to __init__
    # and then returns the same reference, which is assigned to `b1`
    print(b1)
    print(id(b1))
    print(dir(b1))
    b1.print()


if __name__ == '__main__':
    main()

