class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id  # Encapsulated private attribute
        self.name = name

    def get_details(self) -> str:
        """Base polymorphic method."""
        return f"User ID: {self._user_id}, Name: {self.name}"


class Member(User):
    def __init__(self, user_id: str, name: str):
        super().__init__(user_id, name)
        self.borrowed_books = []  # Tracks active loans (Max 5)

    def borrow_book(self, book_title: str) -> str:
        if len(self.borrowed_books) >= 5:
            return "Borrowing limit reached (Max 5 books)."
        self.borrowed_books.append(book_title)
        return f"Successfully borrowed '{book_title}'."

    # Polymorphic Override
    def get_details(self) -> str:
        return f"[Member] ID: {self._user_id} | Name: {self.name} | Borrowed: {len(self.borrowed_books)}/5"


class Librarian(User):
    def __init__(self, user_id: str, name: str, employee_id: str):
        super().__init__(user_id, name)
        self._employee_id = employee_id

    # Polymorphic Override
    def get_details(self) -> str:
        return f"[Librarian] ID: {self._user_id} | Name: {self.name} | Staff ID: {self._employee_id}"


# Execution Example
if __name__ == "__main__":
    users = [
        Member("M101", "Alex"),
        Librarian("L201", "Sarah", "EMP99")
    ]

    # Dynamic Polymorphism demonstration
    for u in users:
        print(u.get_details())
