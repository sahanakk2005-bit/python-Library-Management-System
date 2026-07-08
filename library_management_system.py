print("="*40)
print("       Library Management System       ")
print("="*40)
books=[{"id":1000,"title":"Harry Potter","author":"J.K. Rowling","status":"Available"},
       {"id":1001,"title":"The Great Gatsby","author":"F. Scott Fitzeraald","status":"Available"},
       {"id":1002,"title":"To Kill A Mockingbird","author":"Harper Lee","status":"Borrowed"},
       {"id":1003,"title":"1984","author":"George Orwell","status":"Available"},
       {"id":1004,"title":"Pride And Prejudice","author":"Jane Austen","status":"Available"}
]
while True:
    print("1. View All Books")
    print("2. View Available Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Add Book")
    print("7. Remove Book")
    print("8. Library Statistics")
    print("9. Exit")
    print("="*40)
    choice=int(input("Please enter your choice"))


    match choice:
        case 1:
            #View All Books
            print("List of books in the library:")
            for index,book in enumerate(books):
                print("="*25)
                print(f"Book {index+1}")
                print("="*25)
                print(f'id     : {book["id"]}')
                print(f'Title  : {book["title"]}')
                print(f'Author : {book["author"]}')
                print(f'Status : {book["status"]}')
                print()

        case 2:
            # View Available Books
            print("List of books in the library:")
            available_books=[book for book in books if book["status"]=="Available"]
            if available_books:
                print("Available books")
                for index,book in enumerate(available_books):
                    print("--------------------")
                    print(f"Book {index+1}")
                    print("--------------------")
                    for key,value in book.items():
                        print(f"{key}    :{value}")
                    print()
            else:
                print("No books available in the library")



        case 3:
            #Search book
            search_book=input("Enter the book name you want to search: ").title()
            for book in books:
                if search_book==book["title"]:
                        if book["status"]=="Available":
                            for key,value in book.items():
                                print(f"{key}:{value}")
                            break
                                
                        else:
                            print(f'sorry "{search_book}" book is currently borrowed')
                            break
            else:
                print(f'Sorry "{search_book}" was not available in library')
            print()

        
        case 4:
            #Borrow Book
            borrow_book=int(input("Enter the book id you want to borrow: "))
            for book in books:
                if borrow_book==book["id"]:
                    if book["status"]=="Available":
                        book["status"]="Borrowed"
                        print(f'"{book["title"]}" has been borrowed successfully')
                        break
                    else:
                        print(f'sorry "{book["title"]}" book is currently borrowed')
                        break
            else:
                print(f'Sorry "{borrow_book}" was not available in library')


        case 5:
            #Return Book
            return_book=int(input("Enter the book id you want to return"))
            for book in books:
                if return_book==book["id"]:
                    if book["status"]=="Borrowed":
                        book["status"]="Available"
                        print(f'"{book["title"]}" returned successfully')
                        break
                    else:
                        print(f'"{book["title"]}" is already available')
                        break
                        
            else:
                print(f"book id {return_book} is not available")
            


        case 6:
            #Add Book
            add_book=input("Do you want to add a book in library (yes/no)").lower()
            new={}
            if add_book=="yes":
                id=int(input("Enter id"))
                title=input("Enter title").title()
                author=input("Enter author").title()
                
                while True:
                    status=input("Enter status (available/borrowed)").title()
                    if status=="Available" or status=="Borrowed":
                        
                        new={"id":id,"title":title,"author":author,"status":status}
                        for book in books:
                            if id==book["id"]:
                                print(f"{id} is already available")
                                break
                        else:
                            books.append(new)
                            print(f"{title} has been added successfully")
                            break
                    else:
                        print("Please enter status correctly")
            else:
                print("Thank you")
           

            
        case 7:
            #Remove Book
            remove_book=int(input("Enter the book id you want to remove"))
            for book in books:
                if remove_book==book["id"]:
                    while True:
                        confirm=input(f'Do you want to delete "{book["title"]}" permanently from library (yes/no)').lower() 
                        if confirm=="yes":
                            books.remove(book)
                            print(f'"{book["title"]}" removed successfully')
                            break
                        else:
                            if confirm=="no":
                                print(f'"{book["title"]}" is not removed')
                                break
                        print("please enter your response correctly")
                    break
            else:
                print(f"book id {remove_book} is not available")



        case 8:
            #Library Statistics 
            available_books=[book for book in books if book["status"]=="Available"]
            borrowed_books=[book for book in books if book["status"]=="Borrowed"]
            book_id=[book["id"] for book in books]
            print(" ========== Library Statistics ==========")
            print("Total books           :",len(books))
            print("Available books       :",len(available_books))
            print("Borrowed books        :",len(borrowed_books))
            print("Highest book id       :",max(book_id))
            print("Lowest book id        :",min(book_id))
            print(f"available percentage :{(len(available_books)/len(books))*100}%")
            print(f"Borrowed percentage  :{(len(borrowed_books)/len(books))*100}%")

        case 9:
            print("Thank you for using Library Management System.")
            print("Goodbye!")
            break

        case  _:print("Please enter your choice correctly")



    