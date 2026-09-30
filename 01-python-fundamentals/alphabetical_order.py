books =["Physics","Chemistry","Maths","Python","artificial Intelligence"]
books_upper=[book.upper() for book in books]
new_books= sorted(books_upper)

new_reversed=list(reversed(books_upper))
print("Reversed List is :",new_reversed)
print("Sorted List is :",new_books)

print("Books in alphabetical order:")
for j in new_books:
    print(j)
    
print(books[2].capitalize())
