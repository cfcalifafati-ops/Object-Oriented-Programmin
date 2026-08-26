CLASS User
    PRIVATE user_id : STRING
    PUBLIC name : STRING

    CONSTRUCTOR(user_id, name)
        SET self.user_id = user_id
        SET self.name = name
    END CONSTRUCTOR

    METHOD get_details()
        RETURN "User ID: " + self.user_id + ", Name: " + self.name
    END METHOD
END CLASS

CLASS Member INHERITS User
    PRIVATE borrowed_books : LIST OF STRING

    CONSTRUCTOR(user_id, name)
        CALL SUPER(user_id, name)
        SET self.borrowed_books = EMPTY LIST
    END CONSTRUCTOR

    METHOD borrow_book(book_title)
        IF LENGTH(self.borrowed_books) >= 5 THEN
            RETURN "Error: Borrowing limit reached (Max 5)."
        END IF
        
        APPEND book_title TO self.borrowed_books
        RETURN "Success: Borrowed " + book_title
    END METHOD

    OVERRIDE METHOD get_details()
        RETURN "[Member] ID: " + self.user_id + " | Name: " + self.name + " | Borrowed: " + LENGTH(self.borrowed_books)
    END METHOD
END CLASS

MAIN PROGRAM
    CREATE member AS Member("M101", "Alex")
    PRINT member.get_details()
    
    FOR i FROM 1 TO 6 DO
        PRINT member.borrow_book("Book " + i)
    END FOR
END MAIN
