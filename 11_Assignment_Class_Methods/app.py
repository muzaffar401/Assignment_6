# Book class banayi jisme har bar new book add hone par total count barhta hai

class Book:
    total_books = 0  # ye class variable hai, sab books ke liye common hai

    @classmethod  # ye decorator batata hai ke ye class method hai
    def increment_book_count(cls):  # cls ka matlab hota hai class khud
        cls.total_books += 1  # class ka variable badha rahe hain

# Jab bhi book add karte hain, to method call karke count badhate hain

Book.increment_book_count()  # pehli book
Book.increment_book_count()  # doosri book
Book.increment_book_count()  # teesri book

print("Total books added:", Book.total_books)  # Output: 3
