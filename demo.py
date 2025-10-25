from operations import *

print(add_book("001", "Python Basics", "John Doe", "Fiction", 5))
print(add_book("002", "AI Future", "Jane Smith", "Sci-Fi", 3))
print(add_member(1, "Alice"))
print(add_member(2, "Bob"))

print("\nSearching for 'Python':")
print(search_books("Python"))

print("\nBorrowing book:")
print(borrow_book(1, "001"))
print(borrow_book(1, "001"))  # Borrow again to show multiple copies

print("\nReturning book:")
print(return_book(1, "001"))

print("\nUpdated Book Info:")
print(books)
print("\nMembers Info:")
print(members)