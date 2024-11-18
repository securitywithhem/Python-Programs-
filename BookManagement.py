'''Declare a class called Book having book title & author name as members.Create a sub-class of it, called Book Details having price & current stock of book as members. 
Create an array for storing details of n books. Define methods to achieve the following:   
a. Initialization of members   
b. To query availability of a book by author name / book title 
c. To update stock of a book on purchase and sell  
Define main method to show usage of above methods '''

class Book:
    def _init_(self, title, author):
        self.title=title
        self.author=author
class BookDetails(Book):
    def _init_(self,title,author,price,stock):
        super()._init_(title,author)
        self.price=price
        self.stock=stock
    def query(self,term):
        return self.title.lower()==term.lower() or self.author.lower()==term.lower
    def update(self,quantity,operation):
        if operation==1:
            if self.stock>=quantity:
                self.stock-=quantity
                print(f"Sold {quantity} copies of '{self.title}'. Remaining stock: {self.stock}")
            else:
                print(f'Not enough stock to sell {quantity} copies of {self.title}.')
        elif operation==2:
            self.stock+=quantity
            print(f'Purchased {quantity} copies of {self.title}.New stock: {self.stock}')
        else:
            print('Invalid operation')
    def display(self):
        print(f'Title: {self.title}, Author: {self.author}, Price: {self.price}, Stock: {self.stock}')

def main():
    n=int(input("Enter no. of books:"))
    books=[]
    for i in range(n):
        title=input("Enter book title:")
        author=input("Enter book author:")
        price=float(input("Enter book price:"))
        stock=int(input("Enter book stock:"))
        books.append(BookDetails(title,author,price,stock))
    while True:
        print('\n Options:')
        print('1. Query a book by title and author')
        print('2. Update stock of a book')
        print('3. Display all books')
        print('4. Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            term=input("Enter term to search:")
            found=False
            for book in books:
                if book.query(term):
                    book.display()
                    found=True
            if not found:
                print('Book not found')
        elif choice==2:
            title=input("Enter book title:")
            for book in books:
                if book.query(title):
                    operation=int(input("Enter operation (1 for sell/2 for purchase):"))
                    quantity=int(input("Enter quantity:"))
                    book.update(quantity,operation)
                    break
                else:
                    print('Book not found')
        elif choice==3:
            print("Book Details:")
            for book in books:
                book.display()
        elif choice==4:
            print("Exiting")
            break
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()