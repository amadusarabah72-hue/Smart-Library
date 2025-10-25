from operations import *

# Reset data for clean testing
books.clear()
members.clear()

# Book & Member adding
assert add_book("001", "Python Basics", "John Doe", "Fiction", 2) == "Book added!"
assert add_member(1, "Alice") == "Member added!"

# Borrowing logic
assert borrow_book(1, "001") == "Book borrowed!"
assert books["001"]["copies"] == 1  # copies decrease

# Returning
assert return_book(1, "001") == "Book returned!"

print("✅ All tests passed!")
