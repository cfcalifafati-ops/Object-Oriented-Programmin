class User:
    """Base class demonstrating encapsulation of user identifiers."""
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id  # Encapsulated protected attribute
        self.name = name

    def get_details(self) -> str:
        """Base method to be overridden by derived classes (Polymorphism)."""
        return f"ID: {self._user_id} | Name: {self.name}"


class Member(User):
    """Derived class representing a library member (Inheritance)."""
    def __init__(self, user_id: str, name: str):
        super().__init__(user_id, name)
        self._borrowed_books = []  # Encapsulated list enforcing rule

    def borrow_book(self, book_title: str) -> str:
        """Enforces maximum 5-book constraint."""
        if len(self._borrowed_books) >= 5:
            return "Error: Borrowing limit reached (Max 5 books)."
        self._borrowed_books.append(book_title)
        return f"Success: Borrowed '{book_title}'."

    def get_details(self) -> str:
        """Polymorphic override displaying member loan status."""
        return f"[Member] ID: {self._user_id} | Name: {self.name} | Borrowed: {len(self._borrowed_books)}/5"


class Librarian(User):
    """Derived class representing staff (Inheritance)."""
    def __init__(self, user_id: str, name: str, employee_id: str):
        super().__init__(user_id, name)
        self._employee_id = employee_id

    def get_details(self) -> str:
        """Polymorphic override displaying librarian staff details."""
        return f"[Librarian] ID: {self._user_id} | Name: {self.name} | Staff ID: {self._employee_id}"


if __name__ == "__main__":
    print("--- SLMS Execution Demo ---")
    
    # Instantiate objects
    member = Member("M101", "Alex")
    librarian = Librarian("L201", "Sarah", "EMP99")

    # Dynamic Polymorphism
    system_users = [member, librarian]
    for u in system_users:
        print(u.get_details())

    print("\n--- Testing 5-Book Limit ---")
    for i in range(1, 7):
        result = member.borrow_book(f"Book {i}")
        print(f"Attempt {i}: {result}")

    print("\nFinal State:")
    print(member.get_details())
