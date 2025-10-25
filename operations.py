# Data structures
genres = ("Fiction", "Non-Fiction", "Sci-Fi")

books = {}  # key: ISBN
members = []  # list of dicts

# Helper function to find member
def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None

# CRUD + Borrow/Return functions

def add_book(isbn, title, author, genre, copies):
    if isbn in books:
        return "ISBN already exists!"
    if genre not in genres:
        return "Invalid genre!"

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "copies": copies
    }
    return "Book added!"

def add_member(member_id, name):
    if find_member(member_id):
        return "Member already exists!"

    members.append({
        "id": member_id,
        "name": name,
        "borrowed_books": []
    })
    return "Member added!"

def search_books(keyword):
    results = []
    for isbn, book in books.items():
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
            results.append((isbn, book))
    return results

def update_book(isbn, title=None, author=None, genre=None, copies=None):
    if isbn not in books:
        return "Book not found!"

    if genre and genre not in genres:
        return "Invalid genre!"

    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if copies is not None: books[isbn]["copies"] = copies

    return "Book updated!"

def borrow_book(member_id, isbn):
    member = find_member(member_id)
    if not member:
        return "Member not found!"
    if isbn not in books:
        return "Book not found!"
    if books[isbn]["copies"] <= 0:
        return "No copies available!"
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached!"

    member["borrowed_books"].append(isbn)
    books[isbn]["copies"] -= 1
    return "Book borrowed!"

def return_book(member_id, isbn):
    member = find_member(member_id)
    if not member:
        return "Member not found!"
    if isbn not in member["borrowed_books"]:
        return "This member did not borrow that book!"

    member["borrowed_books"].remove(isbn)
    books[isbn]["copies"] += 1
    return "Book returned!"
